from flask import Flask, render_template, json, request, redirect, jsonify
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
from datetime import datetime
  
app = Flask(__name__)
  
app.secret_key = "caircocoders-ednalan-2020"
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Tushar0420&'
app.config['MYSQL_DB'] = 'reserve_study_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
  
@app.route('/')
def main():
    return redirect('/useradmin')
    
@app.route('/useradmin')
def useradmin():
   cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

   cur.execute("SELECT * FROM component_table")
   component_data = cur.fetchall()

   cur.execute("Select * From loan_expenditues")
   loan_other = cur.fetchall()

   cur.execute("Select max(initial_id) as id from initial_parameters")
   initial_id = int(cur.fetchall()[0]["id"]) + 1
   print(initial_id)

   cur.execute("Select * from unit_variable")
   unit = cur.fetchall()

   cur.execute("Select * from special_assessments")
   special_assessments = cur.fetchall()

   data = [special_assessments[:10],special_assessments[10:20],special_assessments[20:30]]

   cur.execute("Select category_name from category_table")
   category_name = cur.fetchall()
   # category_name = [i["category_name"] for i in category_name ]
   
   print(list(category_name))
   # print(component_data, loan_other)
   return render_template('data_entry.html', component_data=component_data, loan_other=loan_other, 
   initial_id = initial_id, unit = unit, special_assessments = data, category_name = str(list(category_name)))

@app.route("/initialparameter", methods = ["POST"])
def initial_parameter():
   data = request.form
   print(data)
   value = [
      data["fiscal_year_start"], data["fiscal_year_end"], data["starting_balance"], 
      data["current_yearly_reserve_contribution"], data["proposed_yearly_reserve_contribution"],
      data["inflation"], data["number_of_units"], data["default_interest_rate"], data["total_assessment_amount_per_month"]
   ]
   cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

   cur.execute("Insert into initial_parameters(fiscal_year_start, fiscal_year_end, starting_balance, current_year_reserve_contribution, proposed_year_reserve_contribution, inflation, number_of_unit, default_interest_rate, total_assessment_amount_per_month) value(%s,%s,%s,%s,%s,%s,%s,%s,%s)", value)
   mysql.connection.commit()       
   cur.close()
   return jsonify("new record inserted")

@app.route("/updateinitial", methods = ["POST"])
def update_initial():
   data = request.form
   print(data)
   cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

   value = [data['fiscal_year_start'], data['fiscal_year_end'], data['starting_balance'],data['current_yearly_reserve_contribution'], data['inflation'], data['proposed_yearly_reserve_contribution'], data['number_of_units'], data['default_interest_rate'],data['total_assessment_amount_per_month'], data['string'] ]
   cur.execute("Update initial_parameters set fiscal_year_start=%s, fiscal_year_end=%s, starting_balance= %s, current_year_reserve_contribution=%s, proposed_year_reserve_contribution=%s, inflation=%s, number_of_unit=%s, default_interest_rate=%s, total_assessment_amount_per_month=%s where initial_id = %s", value)
   mysql.connection.commit()       
   cur.close()
   
   return jsonify("new record inserted")

@app.route("/addunit", methods= ["POST", "GET"])
def add_unit():
   data= request.form
   cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

   value = [data["unit"], data["building"], data["address"], data["square_footage"], data["percentage"]]
   cur.execute("Insert into unit_variable(unit, building, address, square_footage, percentage) value(%s, %s, %s, %s, %s)", value)
   mysql.connection.commit()
   cur.close()
   return jsonify("new inserted")

@app.route("/updateunit", methods= ["POST", "GET"])
def update_unit():
   data = request.form
   cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
   pk = request.form['pk']
   name = request.form['name']
   value = request.form['value']

   if name == "unit":
      cur.execute("update unit_variable set unit=%s where unit_id=%s", (value, pk))
   elif name == "address":
      cur.execute("update unit_variable set address= %s where unit_id= %s", (value, pk))
   elif name == "building":
      cur.execute("update unit_variable set building=%s where unit_id=%s", (value, pk))
   elif name == "square_footage":
      cur.execute("update unit_variable set square_footage=%s where unit_id=%s", (value, pk))
   elif name == "percentage":
      cur.execute("update unit_variable set percentage=%s where unit_id=%s", (value, pk))
   mysql.connection.commit()
   cur.close()
   return jsonify("record updated")


@app.route("/ajax_add",methods=["POST","GET"])
def ajax_add():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        data = request.form
        print(data)
        category_name = data["category"]
        component_title = data["component_title"]
        description = data["description"]
        useful_life = data["useful_life"]
        remaining_useful_life = data["remaining_useful_life"]
        current_replacement_cost = data["current_replacement_cost"]
        assessment = data["assessment"]
        fund_component = data["fund_component"]
        notes = data["notes"]

        value = [category_name, component_title, description, useful_life, remaining_useful_life, current_replacement_cost, assessment, fund_component, notes]

        print(request.form)

        cur.execute("Insert into component_table(category_name,component_name, descriptions, useful_life, remaining_useful_life, current_replacement_cost,assessment, fund_component, notes) values(%s, %s, %s, %s, %s, %s, %s, %s,%s)", value)
        mysql.connection.commit()       
        cur.close()
        msg = 'New record created successfully'   
    return jsonify(msg)

@app.route('/updateemployee', methods=['POST'])
def updateemployee():
        print(request.form)
        pk = request.form['pk']
        name = request.form['name']
        value = request.form['value']
        print(value, name, pk)
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if name == 'category':
           cur.execute("UPDATE component_table SET category_name = %s WHERE category_id = %s ", (value, pk))
        elif name == 'component_title':
           cur.execute("UPDATE component_table SET component_name = %s WHERE category_id = %s ", (value, pk))
           print("done")
        elif name == 'description':
           cur.execute("UPDATE component_table SET descriptions = %s WHERE category_id = %s ", (value, pk))
        elif name == 'useful_life':
           cur.execute("UPDATE component_table SET useful_life = %s WHERE category_id = %s ", (value, pk))
        elif name == 'remaining_useful_life':
           cur.execute("UPDATE component_table SET remaining_useful_life = %s WHERE category_id = %s ", (value, pk))
        elif name == 'current_replacement_cost':
           cur.execute("UPDATE component_table SET current_replacement_cost = %s WHERE category_id = %s ", (value, pk))
        elif name == 'assessment':
           cur.execute("UPDATE component_table SET assessment = %s WHERE category_id = %s ", (value, pk))
        elif name == 'fund_component':
           cur.execute("UPDATE component_table SET fund_component = %s WHERE category_id = %s ", (value, pk))
        elif name == 'notes':
           cur.execute("UPDATE component_table SET notes = %s WHERE category_id = %s ", (value, pk))
        mysql.connection.commit()
        cur.close()
        return json.dumps({'status':'OK'})

@app.route("/addother", methods = ["POST", "GET"])
def other():
   cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
   if request.method == 'POST':
      data = request.form
      print(data)
      year = data["year"]
      amount_due = data["amount_due"]
      description = data["description"]
      fund_component = data["fund_component"]

      value = [year, amount_due, description, fund_component]

      cur.execute("Insert into loan_expenditues(years, amount_due, descriptions, fund_component) value(%s, %s, %s, %s)", value)
      mysql.connection.commit()       
      cur.close()
      msg = 'New record created successfully'
   
   return jsonify(msg)

@app.route("/updateloan", methods = ["POST", "GET"])
def updateloan():
   print(request.form)
   pk = request.form['pk']
   name = request.form['name']
   value = request.form['value']   
   cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
   if name == 'year':
      cur.execute("UPDATE loan_expenditues SET years = %s WHERE other_id = %s ", (value, pk))
   return json.dumps({'status':'OK'})







if __name__ == '__main__':
    app.run(debug=True)
