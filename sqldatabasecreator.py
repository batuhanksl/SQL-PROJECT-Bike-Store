import sqlite3
import sqldatacommands

def create_editable_sql_tables():
    conn = sqlite3.connect("data.db")

    table_crate_query = '''CREATE TABLE IF NOT EXISTS customer
    (customer_id INTEGER PRIMARY KEY AUTOINCREMENT,id_number INTEGER,first_name TEXT,last_name TEXT,phone INTEGER,city TEXT,zip_code INTEGER)'''

    table_crate_query2 = '''CREATE TABLE IF NOT EXISTS staffs
    (staff_id INTEGER PRIMARY KEY AUTOINCREMENT,id_number INTEGER,first_name TEXT,last_name TEXT,phone INTEGER,manager_id INTEGER)'''

    table_crate_query3 = '''CREATE TABLE IF NOT EXISTS products
    (product_id INTEGER PRIMARY KEY AUTOINCREMENT,product_name TEXT,brand_id INTEGER,category_id INTEGER,model_year INTEGER,price INTEGER)'''

    table_crate_query4 = '''CREATE TABLE IF NOT EXISTS stocks
    (product_id INTEGER PRIMARY KEY AUTOINCREMENT,quantity INTEGER)'''

    table_crate_query5 = '''CREATE TABLE IF NOT EXISTS orders
    (order_id INTEGER PRIMARY KEY AUTOINCREMENT,customer_id INTEGER,product_id INTEGER,quantity INTEGER,order_status TEXT,staff_id INTEGER)'''

    table_crate_query6 = '''CREATE TABLE IF NOT EXISTS login_info
    (type TEXT,id_number INTEGER,password TEXT)'''

    table_crate_query7 = '''CREATE TABLE IF NOT EXISTS brands
    (brand_id INTEGER PRIMARY KEY AUTOINCREMENT,brand_name TEXT)'''

    table_crate_query8 = '''CREATE TABLE IF NOT EXISTS categories
    (category_id INTEGER PRIMARY KEY AUTOINCREMENT,category_name TEXT)'''

    conn.execute(table_crate_query)
    conn.execute(table_crate_query2)
    conn.execute(table_crate_query3)
    conn.execute(table_crate_query4)
    conn.execute(table_crate_query5)
    conn.execute(table_crate_query6)
    conn.execute(table_crate_query7)
    conn.execute(table_crate_query8)
    conn.close()

create_editable_sql_tables()

#If you deleted data.db run this
def first_time():
    #Employers
    sqldatacommands.add_to_staffs_table(33333333333,123,"Batuhan","Kislaci",5555555555,None)
    sqldatacommands.add_to_staffs_table(38723264821,68123,"Cansel","Ozyurt",5386259471,1)
    sqldatacommands.add_to_staffs_table(38723424821,71823,"Hanife","Yildizhan",5312259471,2)
    sqldatacommands.add_to_staffs_table(38723261221,17232,"Arda","Altintas",5386242471,2)

    #Brands
    sqldatacommands.add_brand("Salcano")
    sqldatacommands.add_brand("Kron")
    sqldatacommands.add_brand("Sedona")
    sqldatacommands.add_brand("Mosso")
    sqldatacommands.add_brand("Bianchi")
    sqldatacommands.add_brand("Kuba")

    #Categories
    sqldatacommands.add_category("Children Bike")
    sqldatacommands.add_category("Electric Bike")
    sqldatacommands.add_category("Mountain Bike")
    sqldatacommands.add_category("Road Bike")

    #Customers
    sqldatacommands.register(11111111111,123,"Arda","Guler",5425721236,"Istanbul",34120)
    sqldatacommands.register(38261274682,21412,"Kenan","Yildiz",5425221236,"Ankara",60200)
    sqldatacommands.register(38261245682,22535,"Ferdi","Kadioglu",5215221236,"İzmir",35200)
    sqldatacommands.register(38212274682,62624,"Ridvan","Yilmaz",5435221236,"Edirne",22140)
    sqldatacommands.register(38267274682,75472,"Hakan","Calhanoglu",5655221236,"Eskisehir",26200)
    sqldatacommands.register(38261287682,12311,"Mesut","Ozil",5755221236,"Eskisehir",26120)
    sqldatacommands.register(35361274682,12477,"Toprak","Razgatlioglu",5865221236,"Eskisehir",26320)
    sqldatacommands.register(35461274682,57343,"Alperen","Sengun",5985221236,"Eskisehir",26120)
    sqldatacommands.register(36461274682,73453,"Furkan","Korkmaz",5135221236,"Eskisehir",26120)

    #Products 
    sqldatacommands.add_to_product_table("Salcano Hector",1,3,2022,7000,32)
    sqldatacommands.add_to_product_table("Salcano City",1,4,2020,17100,45)
    sqldatacommands.add_to_product_table("Kron XC100",2,4,2018,9750,24)
    sqldatacommands.add_to_product_table("Mosso Wildfire",4,1,2024,11000,48)
    sqldatacommands.add_to_product_table("Bianchi Snap",5,3,2021,8300,26)
    sqldatacommands.add_to_product_table("Kuba S15",6,2,2024,13200,67)
    sqldatacommands.add_to_product_table("Sedona 640",3,4,2022,17000,21)

    #Pending Orders
    sqldatacommands.add_to_orders(11111111111,1,2)
    sqldatacommands.add_to_orders(38261274682,2,1)
    sqldatacommands.add_to_orders(38261245682,5,2)
    sqldatacommands.add_to_orders(38261245682,1,1)

    #Completed Orders
    sqldatacommands.accept_pending_order(1,2,30,1)
