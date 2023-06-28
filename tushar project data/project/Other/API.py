from flask import Flask, jsonify, request
from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/getdata", methods = ["GET", "POST"])
def get_data():

    all_data = []
    for i in range(len(request.json)):

        result = {}
        print(request.json)
        data = request.json[i]

        result["Revenues"] = (data["Common Expension"][" HOA Common Expenses Dues "] * data["Common Expension"]["Number of Units"]) * 12
        result["Minus_Delinquent"] = result["Revenues"] * .02
        result["Gross_Profit"] = result["Revenues"] - result["Minus_Delinquent"] 
        print("\nRevenues:- {}, \nMinus_Delinquent:- {}, \nGross_Profit:- {}".format(result["Revenues"], result["Minus_Delinquent"], result["Gross_Profit"]))

        result["Common_Expenses_subtotal"] = sum(data["Common Expenses (Year)"].values())
        print("\nCommon_Expenses_subtotal:- {}".format(result["Common_Expenses_subtotal"]))

        result["Common_Expenses_NET_Profit_Loss"] = result["Gross_Profit"] - result["Common_Expenses_subtotal"]
        print("Common_Expenses_NET_Profit_Loss:- {}".format(result["Common_Expenses_NET_Profit_Loss"]))

        result["Reserve_Account_Expenses"] = sum(data['REPLACEMENT RESERVES (Replacement between 13 months and 30 years time, as well as exterior painting)'].values())
        result["Income_from_Reserve_Dues"] = (data['Replacement Reserves']['HOA Replacement Reserve Dues']* data["Common Expension"]["Number of Units"]) * 12
        print(f'\nReserve_Account_Expenses:- {result["Reserve_Account_Expenses"]}, \nIncome_from_Reserve_Dues:- {result["Income_from_Reserve_Dues"]}')

        result["Reserves"] = 14560 - result["Income_from_Reserve_Dues"] - result["Reserve_Account_Expenses"]
        print("\nReserves:- {}".format(result["Reserves"]))

        result["MY_Total_MONTHLY_Dues"] = sum(data["Total Dues"].values())
        print(f'\nMY_Total_MONTHLY_Dues:- {result["MY_Total_MONTHLY_Dues"]}')

        data.update(result)
        print(data)
        all_data.append(data)

    # Read data in pandas from json to structured format
    dfItem = pd.json_normalize(all_data)
    dfItem["Year"] = pd.to_datetime(dfItem["Year"], format="%Y")
    dfItem.to_csv("data.csv")

    # plot using
    plt.fill_between(dfItem["Year"], dfItem["temp_graph2"])
    plt.fill_between(dfItem["Year"], dfItem["temp_graph1"])
    for pos in ['right', 'top', 'bottom', 'left']:
        plt.gca().spines[pos].set_visible(False)    
    plt.xticks(dfItem["Year"], [2018, 2019, 2020])
    plt.savefig('plot.png',bbox_inches='tight')
    plt.close()
    

    # Generate PDF  
    m = 22   #Margin
    pw = 210 - 2*m    #page width: width of A4 is 210mm
    ch = 10   #cell height

    pdf = FPDF()
    pdf.l_margin = m
    pdf.r_margin = m
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)

    def table_data(data, heading, d):
        pdf.set_font("Arial", "B", 12)
        pdf.set_text_color(255,255,255)
        pdf.set_fill_color(0, 51, 102)
        pdf.set_top_margin(10)
        pdf.cell(w = 0, h= 10, txt = heading, ln = 1, fill = True)

        epw = pdf.w - 2*pdf.l_margin
        col_width = epw/d
        th = pdf.font_size
        pdf.set_font("Arial","", 10)
        pdf.set_text_color(0,0,0)

        for row in data:
            for data_1 in row:
                pdf.cell( col_width, 10, str(data_1))
            pdf.ln(8)
        return "Done"


    pdf.image("Image.png", x = 160, w = 30, h = 26)

    pdf.set_text_color(216,109,2)
    pdf.cell(w = 0,h =10, txt="EXECUTIVE SUMMARY", ln=1)
    pdf.ln(8)

    # PROPERTY SUMMARY
    data = (
        ("ASSOCIATION NAME", "Sample Condominium Association"),
        ("LOCATION", "Seattle, WA98104"),
        ("YEAR CONSTRUCTED", data["Year"]),
        ("NUMBER OF UNITS", 100),
        ("FINANCIAL YEAR", "2017(Januart 1, 2017 - December 31, 2017"),
        ("REPORT LEVEL", "Level 1 Full Study with site Visit")
    )
    table_data(data, "PROPERTY SUMMARY", 3)
    pdf.ln(8)

    # Reserve Fund
    data = (
        ("PROJECTED STARTING BALANCE", "$103.613"),
        ("FULL FUNDED BALANCE, IDEAL", "$163.017"),
        ("PERCENT FUNDED", "64%"),
        ("INTEREST EARNED", "1.00%"),
        ("INFLATION RATE", "3.00%"),
    )
    table_data(data, "RESERVE FUND", 2)
    pdf.ln(8)

    # RESERVE CONTRIBUTIONS
    data = (
        ("CURRENT RESERVE FUND CONTRIBUTION", "$87.753"),
        ("FULL FUNDED MAXIMUM CONTRIBUTION", "$198.866"),
        ("BASELINE FUNDING, MINIMUM CONTRIBUTION", "$100.617"),
        ("SPECIAL ASSESSMENT", "$0"),
    )
    table_data(data, "RESERVE CONTRIBUTIONS", 2)
    pdf.ln(8)

    # 2ND Page of PDF
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)

    pdf.image("Image.png", x = 160, w = 30, h = 26)

    pdf.set_text_color(216,109,2)
    pdf.cell(w = 0,h =10, txt="KEY INSIGHTS", ln=1)
    pdf.ln(8)
    pdf.set_text_color(0,25,51)
    pdf.set_font("Arial", "B", 25)
    pdf.cell(w = pw/3, h=10, txt="$103,613", ln=0, align= 'C')
    pdf.cell(w = pw/3, h=10, txt="$87,753", ln=0, align="C")
    pdf.cell(w = pw/3, h=10, txt="$5,102,536", ln=1, align="C")

    pdf.set_text_color(216,109,2)
    pdf.set_font("Arial", "B", 10)

    pdf.multi_cell(w = pw/3, h = 10, txt= "Reserve Account Balance",align= "C")
    pdf.line(pdf.get_y(), 84,pdf.get_y(), 54)
    print(pdf.get_x(), pdf.get_y())
    pdf.set_xy(pdf.get_x()+pw/3, pdf.get_y()-10)
    pdf.multi_cell(w = pw/3, h = 10, txt= "Annual Reserve Contribution", align="C")
    print(pdf.get_x(), pdf.get_y())
    pdf.line(pdf.get_y()+ pw/3 + 4, 84,pdf.get_y()+pw/3 + 4, 54)
    pdf.set_xy(pdf.get_x()+(2*pw/3), pdf.get_y()-10)
    pdf.multi_cell(w = pw/3, h = 10, txt= "Projected Exprenses over 30 years",align= "C")
    pdf.ln(8)

    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(216,109,2)
    pdf.cell(w = 0,h =10, txt="FULL FUNDING STRATEGY", ln=1)
    pdf.ln(8)
    pdf.image("plot.png", x = 30, w = 150, h = 80)

    pdf.output("example.pdf", "F")

    return all_data


if __name__ == '__main__':
    app.run(debug = True)




# {
#     "Common Expension":
#         {
#             " HOA Common Expenses Dues ":174,
#             "Number of Units": 8
#         }
#     ,
#     "Common Expenses (Year)": 
#         {
#             "Bank fees": 45,
#             "Contractor Repairs": 1920,
#             "In-house Maintenance": 500
#         },
#     "Replacement Reserves": {
#         "HOA Replacement Reserve Dues": 30
#     },
#     "REPLACEMENT RESERVES (Replacement between 13 months and 30 years time, as well as exterior painting)":{
#         "Paint the Metal Fence & Gates": 1750,
#         "Update 3 south facing doors": 1200,
#         "roof": 0
#     },
#     "Total Dues":{
#         "HOA Common Expenses Dues": 174,
#         "HOA Replacement Reserve Dues": 30
#     }
# }