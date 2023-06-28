from flask import Flask, request
import mysql.connector as connection

app = Flask(__name__) 

mydb = connection.connect(host="localhost", database = "reserve_study_db", user = "root", password = "Tushar0420&", use_pure=True)


@app.route("/app", methods = ["POST"])
def start():
    if request.method == "POST":
       cursor = mydb.cursor() 
       data = request.form
       values = list(data.values())
       cursor.execute("insert into component_table (category_name, component_name, descriptions, useful_life, remaining_useful_life, current_replacement_cost, assessment, fund_component) values (%s, %s, %s, %s, %s, %s, %s, %s)", values)
       mydb.commit()
    #    print(data)
       return data

    
@app.route("/getdata", methods = ["GET"])
def getdata():
    if request.method == "GET":
        cursor = mydb.cursor()
        cursor.execute("Select * from component_table")
        data = cursor.fetchall()
        return data

@app.route("/individual_components", methods = ["GET"])
def individual_component():
    if request.method == "GET":
        cursor = mydb.cursor()
        cursor.execute("Select * from component_table a left join component_details_table b on a.component_id = b.component_id")
        data = cursor.fetchall()
        return data
    
@app

if __name__ == "__main__":
    app.run(debug=True)
