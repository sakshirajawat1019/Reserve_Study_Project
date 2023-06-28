from flask import Flask, request, render_template, redirect, send_file
from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as connection

mydb = connection.connect(host="localhost", database = "reserve_study", user = "root", password = "Tushar0420&", use_pure=True)

app = Flask(__name__)

@app.route("/generated_pdf", methods = ["GET", "POST"])
def generated_pdf():

    # all_data = []
    
    # for i in range(len(request.json)):

    #     result = {}
    #     print(request.json)
    #     data = request.json[i]

    #     result["Revenues"] = (data["Common Expension"][" HOA Common Expenses Dues "] * data["Common Expension"]["Number of Units"]) * 12
    #     result["Minus_Delinquent"] = result["Revenues"] * .02
    #     result["Gross_Profit"] = result["Revenues"] - result["Minus_Delinquent"] 
    #     print("\nRevenues:- {}, \nMinus_Delinquent:- {}, \nGross_Profit:- {}".format(result["Revenues"], result["Minus_Delinquent"], result["Gross_Profit"]))

    #     result["Common_Expenses_subtotal"] = sum(data["Common Expenses (Year)"].values())
    #     print("\nCommon_Expenses_subtotal:- {}".format(result["Common_Expenses_subtotal"]))

    #     result["Common_Expenses_NET_Profit_Loss"] = result["Gross_Profit"] - result["Common_Expenses_subtotal"]
    #     print("Common_Expenses_NET_Profit_Loss:- {}".format(result["Common_Expenses_NET_Profit_Loss"]))

    #     result["Reserve_Account_Expenses"] = sum(data['REPLACEMENT RESERVES (Replacement between 13 months and 30 years time, as well as exterior painting)'].values())
    #     result["Income_from_Reserve_Dues"] = (data['Replacement Reserves']['HOA Replacement Reserve Dues']* data["Common Expension"]["Number of Units"]) * 12
    #     print(f'\nReserve_Account_Expenses:- {result["Reserve_Account_Expenses"]}, \nIncome_from_Reserve_Dues:- {result["Income_from_Reserve_Dues"]}')

    #     result["Reserves"] = 14560 - result["Income_from_Reserve_Dues"] - result["Reserve_Account_Expenses"]
    #     print("\nReserves:- {}".format(result["Reserves"]))

    #     result["MY_Total_MONTHLY_Dues"] = sum(data["Total Dues"].values())
    #     print(f'\nMY_Total_MONTHLY_Dues:- {result["MY_Total_MONTHLY_Dues"]}')

    #     data.update(result)
    #     print(data)
    #     all_data.append(data)

    # # Read data in pandas from json to structured format
    # dfItem = pd.json_normalize(all_data)
    # dfItem["Year"] = pd.to_datetime(dfItem["Year"], format="%Y")
    # dfItem.to_csv("data.csv")

    # # plot using
    # plt.fill_between(dfItem["Year"], dfItem["temp_graph2"])
    # plt.fill_between(dfItem["Year"], dfItem["temp_graph1"])
    # for pos in ['right', 'top', 'bottom', 'left']:
    #     plt.gca().spines[pos].set_visible(False)    
    # plt.xticks(dfItem["Year"], [2018, 2019, 2020])
    # plt.savefig('plot.png',bbox_inches='tight')
    # plt.close()
    

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
        ("YEAR CONSTRUCTED", 2018),
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

    # 3rd Page
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    
    pdf.image("Image.png", x = 160, w = 30, h = 26)

    pdf.set_text_color(216,109,2)
    pdf.cell(w = 0,h =10, txt="FULL FUNDING PLAN | SUMMARY", ln=1)
    pdf.ln(8)

    print(mydb.is_connected())
    cur = mydb.cursor()

    cur.execute("select * from common_expenses_major")
    result = cur.fetchall()
    
    page_width = pdf.w - 2 * pdf.l_margin

    pdf.set_font('Courier', '', 11)
    pdf.set_text_color(255, 255, 255)
    
    col_width = page_width/8
    print(col_width)
    
    pdf.ln(0)
    
    th = pdf.font_size
    print(th)

    txt = "Year"
    print(txt.center(38))
    pdf.multi_cell(col_width, th, txt.center(32), fill = True)
    pdf.set_xy(pdf.get_x()+col_width, pdf.get_y()-th*5)
    txt = "Common Expenses Dues"
    print(txt.center(32))
    pdf.multi_cell(col_width, th,txt.center(32), fill = True)
    pdf.set_xy(pdf.get_x()+col_width * 2, pdf.get_y()-th*5)
    txt = "Number of Units"
    print(txt.center(38))
    pdf.multi_cell(col_width, th, txt.center(38), fill = True)
    pdf.set_xy(pdf.get_x()+col_width * 3, pdf.get_y()- th*5)
    txt = "Revenues"
    print(txt.center(32))
    pdf.multi_cell(col_width, th, txt.center(32), align="C", fill = True)
    pdf.set_xy(pdf.get_x()+col_width * 4, pdf.get_y()-th*5)
    txt = "Minus Delinquent Payments"
    print(txt.center(32))
    pdf.multi_cell(col_width, th, txt.center(32) , align="C", fill = True)
    pdf.set_xy(pdf.get_x()+col_width * 5, pdf.get_y()-th*5)
    txt = "Gross Profit"
    print(txt.center(32))
    pdf.multi_cell(col_width, th, txt.center(36), align="C", fill = True)
    pdf.set_xy(pdf.get_x()+col_width * 6, pdf.get_y()-th*5)
    txt = "Common Expenses Subtotal"
    print(txt.center(32))
    pdf.multi_cell(col_width, th, txt.center(32), align="C", fill = True)
    pdf.set_xy(pdf.get_x()+col_width * 7, pdf.get_y()- th*5)
    txt = "Common Expenses NET Profit/Loss"
    print(txt.center(32))
    pdf.multi_cell(col_width, th, txt.center(32), align="C", fill = True)

    pdf.set_text_color(0,0,0)
    
    for row in result:
        print(row[7])
        pdf.cell(col_width, th, str(row[7]), align= "C")
        pdf.cell(col_width, th, str(row[0]), align= "C")
        pdf.cell(col_width, th, str(row[1]), align= "C")
        pdf.cell(col_width, th, "$" + str(row[2]), align= "C")
        pdf.cell(col_width, th, "$" + str(row[3]), align= "C")
        pdf.cell(col_width, th, "$" + str(row[4]), align= "C")
        pdf.cell(col_width, th, "$" + str(row[5]), align= "C")
        pdf.cell(col_width, th, "$" + str(row[6]), align= "C")
        pdf.ln(th)
    
    pdf.ln(10)
    
    pdf.set_font('Times','',10.0) 
    pdf.cell(page_width, 0.0, '- end of report -', align='C')

    pdf.output("flask/example.pdf", "F")

    return send_file("example.pdf")

@app.route("/app", methods = ["GET", "POST"])
def first():
    return render_template("index.html")

@app.route("/table", methods = ["GET", "POST"])
def table():
    print(mydb.is_connected())
    cur = mydb.cursor()

    if request.method == "GET":
        cur.execute("select * from common_expenses_major")
        output = cur.fetchall()

        cur.execute("select Expenses_Name, round(Price), Years from common_expenses_year")
        output1 = cur.fetchall()

        cur.execute("select * from replacement_reserve")
        output2 = cur.fetchall()

        cur.execute("select * from replacement_reserve_major")
        output3 = cur.fetchall()  

        return render_template("table.html", common_expenses_major = output, common_expenses_year = output1, replacement_reserve = output2, replacement_reserve_major = output3)
    
    elif request.method == "POST":
        start_year = int(request.form["start_year"])
        end_year = int(request.form["end_year"])

        cur.execute(f"select * from common_expenses_major where Years between {start_year} and {end_year}")
        output = cur.fetchall()

        cur.execute(f"select Expenses_Name, round(Price), Years from common_expenses_year where Years between {start_year} and {end_year}")
        output1 = cur.fetchall()

        cur.execute(f"select * from replacement_reserve where Years between {start_year} and {end_year}")
        output2 = cur.fetchall()

        cur.execute(f"select * from replacement_reserve_major where Years between {start_year} and {end_year}")
        output3 = cur.fetchall()  

        return render_template("table.html", common_expenses_major = output, common_expenses_year = output1, replacement_reserve = output2, replacement_reserve_major = output3)

@app.route("/calculate", methods = ["POST"])
def calculate_common():
    print(mydb.is_connected())
    cur = mydb.cursor()
    if request.method == "POST":

        data = request.form
        print(data)
    
        common_ex = {}
        replacement_re = {}

        for i in data.keys():
            if "key" in i :
                # print(i.split("key")[1])
                if int(i.split("key")[1]) <= 100:
                    common_ex[data[i]] = data["value"+i.split("key")[1]]
                elif int(i.split("key")[1]) >= 500:
                    replacement_re[data[i]] = data["value"+i.split("key")[1]]
        
        result = {}
        #calculation for common expenses
        result["Revenues"] = round(int(data['common_expenses Dues']) * int(data['number_units']) * 12)

        if data["minus_delinquent_payment"] == "Yes":
            print(float(data["delinquent_rate"])/100)
            result["Minus_Delinquent"] = round(result["Revenues"] * (float(data["delinquent_rate"])/100))
        else:
            result["Minus_Delinquent"] = result["Revenues"] * 0

        result["Gross_Profit"] = result["Revenues"] - result["Minus_Delinquent"]

        result["Common_Expenses_subtotal"] = round(sum(map(int,common_ex.values())))
        result["Common_Expenses_NET_Profit_Loss"] = result["Gross_Profit"] - result["Common_Expenses_subtotal"]

        #calculation for replacement reserves
        result["Reserve_Account_Expenses"] = round(sum(map(int, replacement_re.values())))
        result["Income_from_Reserve_Dues"] = round((int(data['replacement_reserve_dues']) * int(data["number_units"])) * 12)
        result["Reserves"] = 14560 + result["Income_from_Reserve_Dues"] - result["Reserve_Account_Expenses"]
        
        #total dues
        result["MY_Total_MONTHLY_Dues"] = round(sum(list((int(data["common_expenses Dues"]), int(data["replacement_reserve_dues"])))))

        # Insert data into databases
        val = (int(data["common_expenses Dues"]),int(data["number_units"]),int(result["Revenues"]),int(result["Minus_Delinquent"]),int(result["Gross_Profit"]), int(result["Common_Expenses_subtotal"]), int(result["Common_Expenses_NET_Profit_Loss"]) ,int(data["year"]))
        print("strt")
        cur.execute("""Insert into common_expenses_major values (%s,%s,%s,%s,%s,%s,%s,%s)""", val)
        mydb.commit()
        cur.execute("select * from common_expenses_major")
        print("SQL data:-",cur.fetchall())

        val1 = list(common_ex.items())
        print("data", val1)
        year = int(data["year"])
        cur.executemany(f"Insert into common_expenses_year values (%s,%s,{year})", val1)
        mydb.commit()
        print("SQL data:-", )

        val2 = list(replacement_re.items())
        cur.executemany(f"Insert into replacement_reserve values (%s,%s,{year})", val2)
        mydb.commit()
        print("SQL data:-","done")

        val3 = (int(data["replacement_reserve_dues"]), result["Reserve_Account_Expenses"], result["Income_from_Reserve_Dues"], result["Reserves"], result["MY_Total_MONTHLY_Dues"], year)
        cur.execute(f"Insert into replacement_reserve_major values (%s,%s,%s,%s,%s,%s)", val3)
        mydb.commit()

        for i in range(1,int(data["projection_year"])+1):
            
            cur.execute(f"Select * from common_expenses_major where Years = {year}")
            pre_year = cur.fetchall()[0][:-3]
            print(pre_year)

            cur.execute(f"Select Expenses_Name, Price from common_expenses_year where Years = {year}")
            data1 = cur.fetchall()
            print(data1)
            
            year += 1
            new = [ (j[0],round(j[1] + (j[1] * (float(data["inflation_rate"])/100)),2)) for j in data1 ]
            print("new:- ", new)
            print(year)
            cur.executemany(f"Insert into common_expenses_year values (%s,%s,{year})", new)
            mydb.commit()

            cur.execute(f"select sum(Price) from common_expenses_year where Years = {year}")
            common_subtotal = round(cur.fetchall()[0][0])
            print(common_subtotal)
            common_profit_loss =  round(common_subtotal - pre_year[-1])

            sum_data = pre_year + (common_subtotal, common_profit_loss, year)
            print(sum_data)

            cur.execute(f"Insert into common_expenses_major values (%s,%s,%s,%s,%s,%s,%s,%s)", sum_data)     
            mydb.commit()

        return redirect("/table")
        # cur.execute("select * from common_expenses_major")
        # output = cur.fetchall()

        # cur.execute("select * from common_expenses_year")
        # output1 = cur.fetchall()

        # cur.execute("select * from replacement_reserve")
        # output2 = cur.fetchall()

        # cur.execute("select * from replacement_reserve_major")
        # output3 = cur.fetchall()
        # # mydb.close()    

        # return render_template("table.html", common_expenses_major = output, common_expenses_year = output1, replacement_reserve = output2, replacement_reserve_major = output3)

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