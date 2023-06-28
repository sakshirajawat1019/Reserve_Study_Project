import mysql.connector as connection

mydb = connection.connect(host = "localhost", database = "reserve_study_db", user = "root", password= "Tushar0420&", use_pure = True)
print(mydb.is_connected())

cursor = mydb.cursor()

# cursor.execute("create database Reserve_Study_db")
# cursor.execute("show databases")
# print(cursor.fetchall())

# cursor.execute("use Reserve_Study_db")

# cursor.execute("create table")

# values = [('Common Exteriors',), ('Common Interiors',), ('Facilities',), ('Furnishings',), ('Irrigation',), ('Landcaps',), ('Lighting',), ('Other',),( 'Access Control',), ('Concrete',)]
# cursor.executemany(f'insert into category_table (category_name) values(%s)', values)
# mydb.commit()


# values = [ ("Decks",), ("Exterior",), ("HVAC",), ("Landscaping",), ("Lighting/Electrical",), ("Pool/Spa",)]
# cursor.executemany(f'insert into category_table (category_name) values(%s)', values)
# mydb.commit()

# values = [("Access Control",), ("Asphalt",), ("Concrete",), ("Decks",), ("Exterior",), ("Fencing",), ("HVAC",), ("Landscaping",), ("Lighting/Electrical",), ("Loans or Other Expenditures",), ("Pool/ Spa",)]
# cursor.executemany(f"insert into category_table (category_name) values (%s)", values)
# mydb.commit()


# import csv

def trim(data):
    if data.isnumeric() == True:
        return int(data)
    elif len(data)>1:
        return data[1:-1]
    else:
        return data

# with open("Component_list.csv", 'r') as f:
#     next(f)
#     for line in f:
#         try:
#             values = tuple(list(map(trim, line.split(",")))[:-1])
#             print(values)\
#             cursor.execute("insert into component_table (category_name, component_name, descriptions, useful_life, remaining_useful_life, current_replacement_cost, assessment, fund_component) values (%s, %s, %s, %s, %s, %s, %s, %s)", values)
#         except:
#             continue
#     mydb.commit()


with open("Component_Detail.csv", "r") as f:
    next(f)
    for line in f:
        
        values  = line.split(",")
        print(values)
            