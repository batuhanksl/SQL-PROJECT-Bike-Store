import sqlite3
from tkinter import messagebox
import interfaces

#Main Tables
def add_to_staffs_table(id_number = int,password = str,first_name = str,last_name = str,phone = int,manager_id = int):

    conn = sqlite3.connect("data.db")

    data_insert_query = '''INSERT INTO staffs
                        (id_number,first_name,last_name,phone,manager_id) VALUES (?,?,?,?,?)
                        '''
    data_insert_tuple = (id_number,first_name,last_name,phone,manager_id)

    cursor = conn.cursor()
    cursor.execute(data_insert_query,data_insert_tuple)
    conn.commit()

    data_insert_query2 = '''INSERT INTO login_info
    (type,id_number,password) VALUES (?,?,?)
    '''
    data_insert_tuple2 = ("staffs",id_number,password)
    cursor.execute(data_insert_query2,data_insert_tuple2)
    
    
    conn.commit()

    conn.close()

def add_to_product_table(product_name = str,brand_id = int,category_id = int,model_year = int,price = int,quantity = int):

    conn = sqlite3.connect("data.db")

    data_insert_query = '''INSERT INTO products
                        (product_name,brand_id,category_id,model_year,price) VALUES (?,?,?,?,?)
                        '''
    data_insert_tuple = (product_name,brand_id,category_id,model_year,price)

    data_insert_query2 = '''INSERT INTO stocks (quantity) VALUES (?)'''
    cursor = conn.cursor()
    cursor.execute(data_insert_query,data_insert_tuple)
    cursor.execute(data_insert_query2,(quantity,))
    conn.commit()

    conn.close()

def add_to_orders(id_number = int,product_id = int,quantity = int):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT customer_id FROM customer WHERE id_number = "+str(id_number))
    selection = cursor.fetchall()
    customer_id = int(selection[0][0])

    data_insert_query2 = '''INSERT INTO orders
    (customer_id,product_id,quantity,order_status,staff_id) VALUES (?,?,?,?,?)
    '''
    data_insert_tuple2 = (customer_id,product_id,quantity,"Pending",None)
    cursor.execute(data_insert_query2,data_insert_tuple2)
    
    
    conn.commit()

    conn.close()

def accept_pending_order(order_number = int,staff_id = int,new_stock = int,product_id = int):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute('''UPDATE orders SET order_status = (?), staff_id = (?) WHERE order_id = (?)''',("Completed",staff_id,order_number))
    cursor.execute('''UPDATE stocks SET quantity = (?) WHERE product_id = (?)''',(new_stock,product_id))
    conn.commit()
    conn.close()

def add_brand(brand_name = str):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO brands (brand_name) VALUES (?)''',(brand_name,))
    conn.commit()
    conn.close()

def add_category(category_name = str):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO categories (category_name) VALUES (?)''',(category_name,))
    conn.commit()
    conn.close()

def update_products_table(product_id = int,price = int,quantity = int):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute('''UPDATE products SET price = (?) WHERE product_id = (?)''',(price,product_id))
    cursor.execute('''UPDATE stocks SET quantity = (?) WHERE product_id = (?)''',(quantity,product_id))
    conn.commit()
    conn.close()


#Login And Register
def login(id_number = int, password = str):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM login_info WHERE id_number = '"+str(id_number)+"'")
    selection = cursor.fetchall()
    conn.close()

    if len(selection) == 0:
        messagebox.showinfo("Info","User not found!")
        interfaces.LoginPage()
    elif len(selection) > 0 and selection[0][2]==password:
        if selection[0][0] == "staffs":
            staff_info = find_staff_name(selection[0][1])
            interfaces.MainStaffPage(staff_info)
        else:
            customer_info = find_customer_name(selection[0][1])
            interfaces.MainCustomerPage(customer_info)   
    elif len(selection) > 0 and selection[0][2]!=password:
        messagebox .showinfo("Info","Wrong password!")
        interfaces.LoginPage()
    else:
        messagebox.showinfo("Info","Something went wrong!")
        interfaces.LoginPage()

def register(id_number = int,password = str,first_name = str,last_name = str,phone = int,city = str,zip_code = int):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM login_info WHERE id_number = '"+str(id_number)+"'")
    selection = cursor.fetchall()

    if len(selection) == 0:
        data_insert_query = '''INSERT INTO customer
        (id_number,first_name,last_name,phone,city,zip_code) VALUES (?,?,?,?,?,?)
        '''
        data_insert_tuple = (id_number,first_name,last_name,phone,city,zip_code)

        cursor = conn.cursor()
        cursor.execute(data_insert_query,data_insert_tuple)
        conn.commit()

        data_insert_query2 = '''INSERT INTO login_info
        (type,id_number,password) VALUES (?,?,?)
        '''
        data_insert_tuple2 = ("customer",id_number,password)
        cursor.execute(data_insert_query2,data_insert_tuple2)
        conn.commit()
    else:
        messagebox.showinfo("Info","Already registered!")
    
    
    

    conn.close()


#Mini Call Commands
def find_product_id(product_name):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT product_id FROM products WHERE product_name = '"+str(product_name)+"'")
    selection = cursor.fetchall()
    product_id = int(selection[0][0])
    conn.close()
    return product_id

def find_employer_id(employer_name):
    employer_search_name = employer_name.split(" ")
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT staff_id FROM staffs WHERE first_name = '"+str(employer_search_name[0])+"'")
    selection = cursor.fetchall()
    staff_id = int(selection[0][0])
    conn.close()
    return staff_id

def find_brand_id(brand_name):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT brand_id FROM brands WHERE brand_name = '"+str(brand_name)+"'")
    selection = cursor.fetchall()
    staff_id = int(selection[0][0])
    conn.close()
    return staff_id

def find_category_id(category_name):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category_id FROM categories WHERE category_name = '"+str(category_name)+"'")
    selection = cursor.fetchall()
    staff_id = int(selection[0][0])
    conn.close()
    return staff_id


#Combobox Filler Commands
def find_brands():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT brand_name FROM brands")
    selection = cursor.fetchall()
    new_list = []
    conn.close()
    for i in selection:
        new_list.append(i[0])

    return new_list

def find_category():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category_name FROM categories")
    selection = cursor.fetchall()
    new_list = []
    conn.close()
    for i in selection:
        new_list.append(i[0])

    return new_list

def find_staffs():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name FROM staffs")
    selection = cursor.fetchall()
    new_list = []
    conn.close()
    for i in selection:
        new_list.append(i[0]+" "+i[1])

    return new_list

def find_products():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT product_name FROM products")
    selection = cursor.fetchall()
    new_list = []
    conn.close()
    for i in selection:
        new_list.append(i[0])

    return new_list

def find_customer_name(customer_id = int):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT first_name,last_name FROM customer WHERE id_number = '"+str(customer_id)+"'")
    selection = cursor.fetchall()
    name = str(selection[0][0]+" "+selection[0][1])
    conn.close()
    return [customer_id, name]

def find_staff_name(staff_id = int):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT first_name,last_name FROM staffs WHERE id_number = '"+str(staff_id)+"'")
    selection = cursor.fetchall()
    name = str(selection[0][0]+" "+selection[0][1])
    conn.close()
    return [staff_id, name]

def find_product_price(product_name = str):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM products WHERE product_name = '"+ str(product_name) +"'")
    selection = cursor.fetchall()
    price = selection[0][0]
    conn.close()

    return price

def find_product_id(product_name = str):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT product_id FROM products WHERE product_name = '"+ str(product_name) +"'")
    selection = cursor.fetchall()
    name = selection[0][0]
    conn.close()

    return name

def staff_table():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staffs")
    selection = cursor.fetchall()
    conn.close()
    return selection

def product_table():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT products.product_id, products.product_name, brands.brand_name, categories.category_name, products.model_year, products.price FROM products INNER JOIN brands ON products.brand_id = brands.brand_id INNER JOIN categories ON products.category_id = categories.category_id ORDER BY products.product_id DESC")
    selection = cursor.fetchall()
    conn.close()
    return selection

def pending_orders_table():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE order_status = 'Pending'")
    selection = cursor.fetchall()
    conn.close()
    return selection

def find_stock_quantity(product_id = int):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT quantity FROM stocks WHERE product_id = "+str(product_id))
    selection = cursor.fetchall()[0][0]
    conn.close()
    return selection

def staff_performans():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT staff_id, count(staff_id) FROM orders GROUP BY staff_id")
    selection = cursor.fetchall()
    
    new_list = []
    for i in selection:
        if i[0] != None:
            cursor.execute("SELECT first_name,last_name FROM staffs WHERE staff_id = (?)",(i[0],))
            name_search = cursor.fetchall()
            name = str(name_search[0][0])+" "+str(name_search[0][1])
            new_list.append([name,i[1]])
        
    conn.close()
    return new_list

def pending_orders_counter():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT order_status, count(order_status) FROM orders GROUP BY order_status")
    selection = cursor.fetchall()
    return selection

def sold_product_counter():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT products.product_name, sum(orders.quantity) FROM orders 
                   INNER JOIN products ON orders.product_id = products.product_id
                   GROUP BY orders.product_id''')
    selection = cursor.fetchall()
    return selection

def customer_who_order():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT customer_id FROM orders GROUP BY customer_id")
    ordered = cursor.fetchall()
    cursor.execute('''SELECT customer_id FROM customer 
                    EXCEPT 
                    SELECT DISTINCT customer_id FROM orders''')
    not_ordered = cursor.fetchall()
    return [["Ordered Before",ordered.__len__()],["Not Ordered Before",not_ordered.__len__()]]

def orders_table_fill():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT orders.order_id, customer.first_name, customer.last_name ,products.product_name, 
                   orders.quantity, orders.order_status, orders.staff_id FROM orders 
                   INNER JOIN products ON orders.product_id = products.product_id 
                   INNER JOIN customer ON orders.customer_id = customer.customer_id 
                   ORDER BY orders.order_id DESC''')
    selection = cursor.fetchall()
    conn.close()
    return selection

def customers_table_fill():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer ORDER BY customer_id DESC")
    selection = cursor.fetchall()
    conn.close()
    return selection

def stocks_table_fill():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT products.product_id ,products.product_name, products.model_year, 
                   products.price, stocks.quantity FROM products 
                   INNER JOIN stocks ON products.product_id = stocks.product_id''')
    selection = cursor.fetchall()
    conn.close()
    return selection

def previous_orders_fill(customer_id = int):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT customer_id FROM customer WHERE id_number = (?)",(str(customer_id),))
    customer = cursor.fetchall()[0][0]

    cursor.execute('''SELECT orders.order_id, products.product_name, orders.quantity, orders.order_status FROM orders 
                   INNER JOIN products ON orders.product_id = products.product_id 
                   WHERE customer_id = (?) 
                   ORDER BY orders.order_id DESC''',(str(customer),))
    selection = cursor.fetchall()
    conn.close()
    return selection
