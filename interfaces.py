import customtkinter
import sqldatacommands
from tkinter import messagebox
from PIL import Image
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#List Functions
def reflesh_lists():
    global product 
    product = sqldatacommands.find_products()
    global employers
    employers = sqldatacommands.find_staffs()
    global category 
    category = sqldatacommands.find_category()
    global brands 
    brands = sqldatacommands.find_brands()
    global staff_table
    staff_table = sqldatacommands.staff_table()
    global product_table
    product_table = sqldatacommands.product_table()
    global pending_orders_table
    pending_orders_table = sqldatacommands.pending_orders_table()
    global tables
    tables = ["Customers","Orders","Stocks"]
    global orders_table 
    orders_table = sqldatacommands.orders_table_fill()
    global customers_table
    customers_table = sqldatacommands.customers_table_fill()
    global stocks_table
    stocks_table = sqldatacommands.stocks_table_fill()

#Main Functions
def search_data_page(page = str):

    reflesh_lists()

    search_data = customtkinter.CTk()
    search_data.iconbitmap("estulogo.ico")
    search_data.geometry("900x500")
    

    search_data_main_frame = customtkinter.CTkFrame(master=search_data)
    search_data_main_frame.pack(pady=10,padx=10, fill="both", expand=True)

    search_data_frame = customtkinter.CTkFrame(master=search_data_main_frame,width=600,height=500)
    search_data_frame.place(x=10,y=10)

    


    #Left Frame
    if page == "Orders":
        search_data_tree = ttk.Treeview(master=search_data_frame,height=25)
        search_data_tree["columns"] = ("Order ID","First Name","Last Name","Product Name","Quantity","Order Status","Staff ID")

        search_data_tree.column("#0",width=1)
        search_data_tree.column("Order ID",width=160,anchor="center")
        search_data_tree.column("First Name",width=130,anchor="center")
        search_data_tree.column("Last Name",width=130,anchor="center")
        search_data_tree.column("Product Name",width=160,anchor="center")
        search_data_tree.column("Quantity",width=160,anchor="center")
        search_data_tree.column("Order Status",width=160,anchor="center")
        search_data_tree.column("Staff ID",width=150,anchor="center")

        search_data_tree.heading("#0",text="")
        search_data_tree.heading("Order ID",text="Order ID")
        search_data_tree.heading("First Name",text="First Name")
        search_data_tree.heading("Last Name",text="Last Name")
        search_data_tree.heading("Product Name",text="Product Name")
        search_data_tree.heading("Quantity",text="Quantity")
        search_data_tree.heading("Order Status",text="Order Status")
        search_data_tree.heading("Staff ID",text="Staff ID")
        

        count = 0
        for i in orders_table:
            search_data_tree.insert(parent="",index="end",iid=count,text="",values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
            count += 1

        search_data_tree.pack(pady=10,padx=10)
    elif page == "Customers":    
        search_data_tree = ttk.Treeview(master=search_data_frame,height=25)
        search_data_tree["columns"] = ("Customer ID","ID Number","First Name","Last Name","Phone","City","Zip Code")

        search_data_tree.column("#0",width=1)
        search_data_tree.column("Customer ID",width=100,anchor="center")
        search_data_tree.column("ID Number",width=170,anchor="center")
        search_data_tree.column("First Name",width=170)
        search_data_tree.column("Last Name",width=170)
        search_data_tree.column("Phone",width=170,anchor="center")
        search_data_tree.column("City",width=160,anchor="center")
        search_data_tree.column("Zip Code",width=110,anchor="center")

        search_data_tree.heading("#0",text="")
        search_data_tree.heading("Customer ID",text="Customer ID")
        search_data_tree.heading("ID Number",text="ID Number")
        search_data_tree.heading("First Name",text="First Name")
        search_data_tree.heading("Last Name",text="Last Name")
        search_data_tree.heading("Phone",text="Phone")
        search_data_tree.heading("City",text="City")
        search_data_tree.heading("Zip Code",text="Zip Code")
        

        count = 0
        for i in customers_table:
            search_data_tree.insert(parent="",index="end",iid=count,text="",values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
            count += 1

        search_data_tree.pack(pady=10,padx=10)
    elif page == "Stocks":

        search_data_action_frame = customtkinter.CTkFrame(master=search_data_main_frame,width=200,height=435)
        search_data_action_frame.place(x=660,y=10)

        search_data_tree = ttk.Treeview(master=search_data_frame,height=25)
        search_data_tree["columns"] = ("Product ID","Product Name","Model Year","Price","Quantity")

        search_data_tree.column("#0",width=1)
        search_data_tree.column("Product ID",width=130,anchor="center")
        search_data_tree.column("Product Name",width=200,anchor="center")
        search_data_tree.column("Model Year",width=140,anchor="center")
        search_data_tree.column("Price",width=140,anchor="center")
        search_data_tree.column("Quantity",width=140,anchor="center")

        search_data_tree.heading("#0",text="")
        search_data_tree.heading("Product ID",text="Product ID")
        search_data_tree.heading("Product Name",text="Product Name")
        search_data_tree.heading("Model Year",text="Model Year")
        search_data_tree.heading("Price",text="Price")
        search_data_tree.heading("Quantity",text="Quantity")
        

        count = 0
        for i in stocks_table:
            search_data_tree.insert(parent="",index="end",iid=count,text="",values=(i[0],i[1],i[2],i[3],i[4]))
            count += 1

        search_data_tree.pack(pady=10,padx=10)

        product_name_label = customtkinter.CTkLabel(master=search_data_action_frame, text="Product Name", font=("Roboto",15))
        product_name_label.place(x=10,y=30)

        product_name_entry = customtkinter.CTkEntry(master=search_data_action_frame,placeholder_text="Product Price",state="disabled",width=170)
        product_name_entry.place(x=10,y=60)

        product_price_label = customtkinter.CTkLabel(master=search_data_action_frame, text="Product Price", font=("Roboto",15))
        product_price_label.place(x=10,y=90)

        product_price_entry = customtkinter.CTkEntry(master=search_data_action_frame,placeholder_text="Product Price",width=170)
        product_price_entry.place(x=10,y=120)

        product_quantity_label = customtkinter.CTkLabel(master=search_data_action_frame, text="Stock Quantity", font=("Roboto",15))
        product_quantity_label.place(x=10,y=150)

        product_quantity_entry = customtkinter.CTkEntry(master=search_data_action_frame,placeholder_text="Quantity",width=170)
        product_quantity_entry.place(x=10,y=180)

        def Select_Product():
            value = search_data_tree.item(search_data_tree.selection()[0])["values"]
            product_name_entry.configure(state = "normal")
            product_name_entry.delete(0,30)
            product_name_entry.insert(0,value[1])
            product_name_entry.configure(state = "disabled")
            product_price_entry.delete(0,30)
            product_price_entry.insert(0,value[3])
            product_quantity_entry.delete(0,30)
            product_quantity_entry.insert(0,value[4])

        def Edit_Product():
            values = search_data_tree.item(search_data_tree.selection()[0])["values"]
            new_values = [values[0],values[1],values[2],int(product_price_entry.get()),int(product_quantity_entry.get())]
            search_data_tree.item(search_data_tree.selection(),values=new_values)

            sqldatacommands.update_products_table(new_values[0],new_values[3],new_values[4])

            product_name_entry.configure(state = "normal")
            product_name_entry.delete(0,30)
            product_name_entry.configure(state = "disabled")
            product_price_entry.delete(0,30)
            product_quantity_entry.delete(0,30)



        select_product_button = customtkinter.CTkButton(master=search_data_action_frame,command=Select_Product , text="SELECT",width=170)
        select_product_button.place(x=10,y=220)

        select_order_button = customtkinter.CTkButton(master=search_data_action_frame,command=Edit_Product , text="EDIT",width=170)
        select_order_button.place(x=10,y=260)


        
    else:
        messagebox.showinfo("Ooops!","Something went wrong!")
        search_data.destroy()

    search_data.mainloop()

def add_data_page_product():
    add_data_product = customtkinter.CTk()
    add_data_product.iconbitmap("estulogo.ico")
    add_data_product.geometry("900x500")

    add_data_product_main_frame = customtkinter.CTkFrame(master=add_data_product)
    add_data_product_main_frame.pack(pady=10,padx=10, fill="both", expand=True)
    
    add_data_product_frame = customtkinter.CTkFrame(master=add_data_product_main_frame,width=100,height=450)
    add_data_product_frame.place(x=650,y=10)
    
    add_data_product_brand_frame = customtkinter.CTkFrame(master=add_data_product_main_frame,width=140,height=200)
    add_data_product_brand_frame.place(x=500,y=10)

    add_data_product_category_frame = customtkinter.CTkFrame(master=add_data_product_main_frame,width=140,height=205)
    add_data_product_category_frame.place(x=500,y=220)
    
    add_data_product_show_frame = customtkinter.CTkFrame(master=add_data_product_main_frame,width=480,height=450)
    add_data_product_show_frame.place(x=10,y=10)

    #Left Frame

    add_data_product_tree = ttk.Treeview(master=add_data_product_show_frame,height=25)
    add_data_product_tree["columns"] = ("ID","Product Name","Brand","Category","Model Year","Price")

    add_data_product_tree.column("#0",width=1)
    add_data_product_tree.column("ID",width=30,anchor="center")
    add_data_product_tree.column("Product Name",width=160)
    add_data_product_tree.column("Brand",width=70)
    add_data_product_tree.column("Category",width=130)
    add_data_product_tree.column("Model Year",width=90,anchor="center")
    add_data_product_tree.column("Price",width=90,anchor="center")

    add_data_product_tree.heading("#0",text="")
    add_data_product_tree.heading("ID",text="ID")
    add_data_product_tree.heading("Product Name",text="Product Name")
    add_data_product_tree.heading("Brand",text="Brand")
    add_data_product_tree.heading("Category",text="Category")
    add_data_product_tree.heading("Model Year",text="Model Year")
    add_data_product_tree.heading("Price",text="Price")

    count = 0
    for i in product_table:
        add_data_product_tree.insert(parent="",index="end",iid=count,text="",values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        count += 1
    
    add_data_product_tree.place(x=10,y=10)


    #Brand Frame
    add_data_page_brand_label = customtkinter.CTkLabel(master=add_data_product_brand_frame, text="ADD BRAND", font=("Roboto",15),width=100)
    add_data_page_brand_label.place(x=10,y=30)

    add_data_brand_name = customtkinter.CTkEntry(master=add_data_product_brand_frame, placeholder_text="Brand Name",width=120)
    add_data_brand_name.place(x=10,y=70)

    def add_brand():
        if add_data_brand_name.get() != "":
            sqldatacommands.add_brand(str(add_data_brand_name.get()))
            add_data_brand_name.delete(0,30)
            reflesh_lists()
            add_data_product.destroy()
            add_data_page_product()
        else:
            messagebox.showinfo("Ooops!","Enter a brand name!")

    add_data_brand_button = customtkinter.CTkButton(master=add_data_product_brand_frame,command=add_brand , text="ADD",width=120)
    add_data_brand_button.place(x=10,y=120)

    #Category Frame
    add_data_page_category_label = customtkinter.CTkLabel(master=add_data_product_category_frame, text="ADD CATEGORY", font=("Roboto",15),width=100)
    add_data_page_category_label.place(x=10,y=30)

    add_data_category_name = customtkinter.CTkEntry(master=add_data_product_category_frame, placeholder_text="Category Name",width=120)
    add_data_category_name.place(x=10,y=70)

    def add_category():
        if add_data_category_name.get() != "":
            sqldatacommands.add_category(add_data_category_name.get())
            add_data_category_name.delete(0,30)
            reflesh_lists()
            add_data_product.destroy()
            add_data_page_product()
        else:
            messagebox.showinfo("Ooops!","Enter a category name!")

    add_data_category_button = customtkinter.CTkButton(master=add_data_product_category_frame,command=add_category , text="ADD", width=120)
    add_data_category_button.place(x=10,y=120)

    #Right Frame
    add_data_page_label = customtkinter.CTkLabel(master=add_data_product_frame, text="ADD PRODUCT", font=("Roboto",20))
    add_data_page_label.pack(pady=12,padx=20)

    add_data_product_brandcb = customtkinter.CTkComboBox(master=add_data_product_frame,values=brands)
    add_data_product_brandcb.pack(pady=12,padx=10)
    
    add_data_product_categorycb = customtkinter.CTkComboBox(master=add_data_product_frame,values=category)
    add_data_product_categorycb.pack(pady=12,padx=10)

    add_data_product_name = customtkinter.CTkEntry(master=add_data_product_frame, placeholder_text="Product Name")
    add_data_product_name.pack(pady=12,padx=10)

    add_data_product_year = customtkinter.CTkEntry(master=add_data_product_frame, placeholder_text="Product Year")
    add_data_product_year.pack(pady=12,padx=10)

    add_data_product_price = customtkinter.CTkEntry(master=add_data_product_frame, placeholder_text="Product Price")
    add_data_product_price.pack(pady=12,padx=10)

    add_data_product_quantity = customtkinter.CTkEntry(master=add_data_product_frame, placeholder_text="Starting Quantity")
    add_data_product_quantity.pack(pady=12,padx=10)

    def button():
        brand_id = sqldatacommands.find_brand_id(add_data_product_brandcb.get()) 
        category_id = sqldatacommands.find_category_id(add_data_product_categorycb.get())
        product_name = add_data_product_name.get()
        model_year = int(add_data_product_year.get())
        price = int(add_data_product_price.get())
        quantity = int(add_data_product_quantity.get())
        sqldatacommands.add_to_product_table(product_name,brand_id,category_id,model_year,price,quantity)
        add_data_product.destroy()
        reflesh_lists()


    add_data_product_button = customtkinter.CTkButton(master=add_data_product_frame,command=button , text="ADD")
    add_data_product_button.pack(pady=12, padx=10)

    add_data_product.mainloop()

def add_data_page_employer():
    add_data_employer = customtkinter.CTk()
    add_data_employer.iconbitmap("estulogo.ico")
    add_data_employer.geometry("900x500")
    
    add_data_employer__main_frame = customtkinter.CTkFrame(master=add_data_employer)
    add_data_employer__main_frame.pack(pady=10,padx=10, fill="both", expand=True)

    add_data_employer_frame = customtkinter.CTkFrame(master=add_data_employer__main_frame,width=80,height=500)
    add_data_employer_frame.place(x=700,y=10)

    add_data_employer_search_frame = customtkinter.CTkFrame(master=add_data_employer__main_frame,width=600,height=500)
    add_data_employer_search_frame.place(x=10,y=10)

    


    #Left Frame
    add_data_employer_tree = ttk.Treeview(master=add_data_employer_search_frame,height=25)
    add_data_employer_tree["columns"] = ("Staff ID","ID Number","First Name","Last Name","Phone","Manager ID")

    add_data_employer_tree.column("#0",width=1)
    add_data_employer_tree.column("Staff ID",width=130,anchor="center")
    add_data_employer_tree.column("ID Number",width=130,anchor="center")
    add_data_employer_tree.column("First Name",width=130)
    add_data_employer_tree.column("Last Name",width=130)
    add_data_employer_tree.column("Phone",width=130,anchor="center")
    add_data_employer_tree.column("Manager ID",width=130,anchor="center")

    add_data_employer_tree.heading("#0",text="")
    add_data_employer_tree.heading("Staff ID",text="Staff ID")
    add_data_employer_tree.heading("ID Number",text="ID Number")
    add_data_employer_tree.heading("First Name",text="First Name")
    add_data_employer_tree.heading("Last Name",text="Last Name")
    add_data_employer_tree.heading("Phone",text="Phone")
    add_data_employer_tree.heading("Manager ID",text="Manager ID")

    count = 0
    for i in staff_table:
        add_data_employer_tree.insert(parent="",index="end",iid=count,text="",values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        count += 1
    
    add_data_employer_tree.pack(pady=10,padx=10)



    #Right Frame
    add_data_employer_label = customtkinter.CTkLabel(master=add_data_employer_frame, text="ADD EMPLOYER", font=("Roboto",20))
    add_data_employer_label.pack(pady=12,padx=20)

    add_data_employer_id_number = customtkinter.CTkEntry(master=add_data_employer_frame, placeholder_text="Id Number")
    add_data_employer_id_number.pack(pady=12,padx=10)

    add_data_employer_password = customtkinter.CTkEntry(master=add_data_employer_frame, placeholder_text="Password")
    add_data_employer_password.pack(pady=12,padx=10)

    add_data_employer_first_name = customtkinter.CTkEntry(master=add_data_employer_frame, placeholder_text="First Name")
    add_data_employer_first_name.pack(pady=12,padx=10)

    add_data_employer_last_tname = customtkinter.CTkEntry(master=add_data_employer_frame, placeholder_text="Last Name")
    add_data_employer_last_tname.pack(pady=12,padx=10)

    add_data_employer_phone = customtkinter.CTkEntry(master=add_data_employer_frame, placeholder_text="Phone Number")
    add_data_employer_phone.pack(pady=12,padx=10)

    add_data_employer_label = customtkinter.CTkLabel(master=add_data_employer_frame, text="Select The Manager Of Employer", font=("Roboto",10))
    add_data_employer_label.pack(pady=12,padx=10)

    add_data_employer_manager = customtkinter.CTkComboBox(master=add_data_employer_frame,values=employers)
    add_data_employer_manager.pack(pady=5,padx=2)

    def button():
        id_number = int(add_data_employer_id_number.get())
        password = add_data_employer_password.get()
        first_name = add_data_employer_first_name.get()
        last_name = add_data_employer_last_tname.get()
        phone = int(add_data_employer_phone.get())
        manager_id = sqldatacommands.find_employer_id(add_data_employer_manager.get())
        sqldatacommands.add_to_staffs_table(id_number,password,first_name,last_name,phone,manager_id)
        add_data_employer.destroy()
        reflesh_lists()

    add_data_employer_button = customtkinter.CTkButton(master=add_data_employer_frame, text="ADD EMPLOYER",command=button, font=("Roboto",15))
    add_data_employer_button.pack(pady=12, padx=10)

    add_data_employer.mainloop()

def accept_orders_page(staff_info = list):
    accept_orders = customtkinter.CTk()
    accept_orders.iconbitmap("estulogo.ico")
    accept_orders.geometry("900x500")
    
    reflesh_lists()

    accept_orders_main_frame = customtkinter.CTkFrame(master=accept_orders)
    accept_orders_main_frame.pack(pady=10,padx=10, fill="both", expand=True)

    accept_orders_action_frame = customtkinter.CTkFrame(master=accept_orders_main_frame,width=200,height=435)
    accept_orders_action_frame.place(x=660,y=10)

    accept_orders_frame = customtkinter.CTkFrame(master=accept_orders_main_frame,width=600,height=500)
    accept_orders_frame.place(x=10,y=10)

    


    #Left Frame
    accept_orders_tree = ttk.Treeview(master=accept_orders_frame,height=25)
    accept_orders_tree["columns"] = ("Order ID","Customer ID","Product ID","Quantity","Order Status","Staff ID")

    accept_orders_tree.column("#0",width=1)
    accept_orders_tree.column("Order ID",width=130,anchor="center")
    accept_orders_tree.column("Customer ID",width=130,anchor="center")
    accept_orders_tree.column("Product ID",width=130,anchor="center")
    accept_orders_tree.column("Quantity",width=130,anchor="center")
    accept_orders_tree.column("Order Status",width=130,anchor="center")
    accept_orders_tree.column("Staff ID",width=130,anchor="center")

    accept_orders_tree.heading("#0",text="")
    accept_orders_tree.heading("Order ID",text="Order ID")
    accept_orders_tree.heading("Customer ID",text="Customer ID")
    accept_orders_tree.heading("Product ID",text="Product ID")
    accept_orders_tree.heading("Quantity",text="Quantity")
    accept_orders_tree.heading("Order Status",text="Order Status")
    accept_orders_tree.heading("Staff ID",text="Staff ID")
    

    count = 0
    for i in pending_orders_table:
        accept_orders_tree.insert(parent="",index="end",iid=count,text="",values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        count += 1

    accept_orders_tree.pack(pady=10,padx=10)

    #Right Frame
    staff_name = customtkinter.CTkLabel(master=accept_orders_action_frame, text=staff_info[1], font=("Roboto",15))
    staff_name.place(x=10,y=10)

    staff_id = int(sqldatacommands.find_employer_id(staff_info[1]))

    product_order_number = customtkinter.CTkEntry(master=accept_orders_action_frame,placeholder_text="Order Number",state="disabled",width=170)
    product_order_number.place(x=10,y=40)

    product_id = customtkinter.CTkEntry(master=accept_orders_action_frame,placeholder_text="Product ID",state="disabled",width=170)
    product_id.place(x=10,y=70)

    product_quantity = customtkinter.CTkEntry(master=accept_orders_action_frame,placeholder_text="Order Quantity",state="disabled",width=170)
    product_quantity.place(x=10,y=100)

    product_stock_quantity = customtkinter.CTkEntry(master=accept_orders_action_frame,placeholder_text="Stock Quantity",state="disabled",width=170)
    product_stock_quantity.place(x=10,y=130)

    def Select_Order():
        value = accept_orders_tree.item(accept_orders_tree.selection()[0])["values"] 

        stock_quantity = sqldatacommands.find_stock_quantity(value[2])
        
        product_order_number.configure(state = "normal")
        product_order_number.delete(0,10)
        product_order_number.insert(0,value[0])
        product_order_number.configure(state = "disabled")

        product_id.configure(state = "normal")
        product_id.delete(0,10)
        product_id.insert(0,value[2])
        product_id.configure(state = "disabled")

        product_quantity.configure(state = "normal")
        product_quantity.delete(0,10)
        product_quantity.insert(0,value[3])
        product_quantity.configure(state = "disabled")

        product_stock_quantity.configure(state = "normal")
        product_stock_quantity.delete(0,10)
        product_stock_quantity.insert(0,stock_quantity)
        product_stock_quantity.configure(state = "disabled")

    def Complete_Order():
        if int(product_id.get()) > 0:
            accept_orders_tree.delete(accept_orders_tree.selection()[0])
            sqldatacommands.accept_pending_order(int(product_order_number.get()),staff_id,(int(product_stock_quantity.get())-int(product_quantity.get())),int(product_id.get()))
            reflesh_lists()
        else:
            messagebox.showinfo("Ooops!","Please select an order first!")

    select_order_button = customtkinter.CTkButton(master=accept_orders_action_frame,command=Select_Order , text="SELECT",width=170)
    select_order_button.place(x=10,y=160)

    select_order_button = customtkinter.CTkButton(master=accept_orders_action_frame,command=Complete_Order , text="COMPLETE ORDER",width=170)
    select_order_button.place(x=10,y=190)




    accept_orders.mainloop()

def previous_customer_orders(customer_info = list):
    previous_orders_table = sqldatacommands.previous_orders_fill(customer_info[0])

    search_data = customtkinter.CTk()
    search_data.iconbitmap("estulogo.ico")
    search_data.geometry("600x500")
    

    search_data_main_frame = customtkinter.CTkFrame(master=search_data)
    search_data_main_frame.pack(pady=10,padx=10, fill="both", expand=True)

    customer_name = customtkinter.CTkLabel(master=search_data_main_frame, text=(customer_info[1] + "'s Basket"), font=("Roboto",20))
    customer_name.place(x=20,y=10)

    search_data_frame = customtkinter.CTkFrame(master=search_data_main_frame,width=550,height=500)
    search_data_frame.place(x=20,y=40)

    
    search_data_tree = ttk.Treeview(master=search_data_frame,height=25)
    search_data_tree["columns"] = ("Order ID","Product Name","Quantity","Order Status")

    search_data_tree.column("#0",width=1)
    search_data_tree.column("Order ID",width=130,anchor="center")
    search_data_tree.column("Product Name",width=190,anchor="center")
    search_data_tree.column("Quantity",width=160,anchor="center")
    search_data_tree.column("Order Status",width=160,anchor="center")

    search_data_tree.heading("#0",text="")
    search_data_tree.heading("Order ID",text="Order ID")
    search_data_tree.heading("Product Name",text="Product Name")
    search_data_tree.heading("Quantity",text="Quantity")
    search_data_tree.heading("Order Status",text="Order Status")
        

    count = 0
    for i in previous_orders_table:
        search_data_tree.insert(parent="",index="end",iid=count,text="",values=(i[0],i[1],i[2],i[3]))
        count += 1

    search_data_tree.place(x=10,y=10)

    search_data.mainloop()

#Main Pages
def MainCustomerPage(customer_info = list):
    root = customtkinter.CTk()
    root.iconbitmap("estulogo.ico")
    root.geometry("900x500")


    #Main Frame
    frame = customtkinter.CTkFrame(master=root,width=880,height=480)
    frame.place(x=10,y=10)

    store_name = customtkinter.CTkLabel(master=frame, text="IKI EYLUL BIKE INTERFACE", font=("Roboto",40))
    store_name.place(x=200,y=20)
    
    def exit():
        root.destroy()
        LoginPage()

    exit_button = customtkinter.CTkButton(master=frame,width=20,height=20,text="<",command=exit)
    exit_button.place(x=10,y=10)

    def PreviousOrders():
        previous_customer_orders(customer_info)

    previous_orders_button = customtkinter.CTkButton(master=frame,width=100,height=20,text="Previous Orders",command=PreviousOrders)
    previous_orders_button.place(x=760,y=10)

    #Left Frame
    frame2 = customtkinter.CTkFrame(master=frame,height=350,width=550)
    frame2.place(x=10,y=100)

    customer_name = customtkinter.CTkLabel(master=frame2, text=customer_info[1], font=("Roboto",20))
    customer_name.place(x=10,y=10)

    frame4 = customtkinter.CTkFrame(master=frame2,height=230,width=500)
    frame4.place(x=10,y=50)

    basket_tree = ttk.Treeview(master=frame4,height=12)
    basket_tree["columns"] = ("Product Name","Quantity","Price")

    basket_tree.column("#0",width=1)
    basket_tree.column("Product Name",width=250,anchor="center")
    basket_tree.column("Quantity",width=160,anchor="center")
    basket_tree.column("Price",width=160,anchor="center")

    basket_tree.heading("#0",text="")
    basket_tree.heading("Product Name",text="Product Name")
    basket_tree.heading("Quantity",text="Quantity")
    basket_tree.heading("Price",text="Price")

    def add_to_basket():
        if int(product_quantity.get()) > 0:
            basket_tree.insert(parent="",index="end",text="",values=(str(product_name.get()),str(product_quantity.get()),sqldatacommands.find_product_price(str(product_name.get()))))
            product_quantity.delete(0,10)
        else:
            messagebox.showinfo("Error!","Please enter a quantity!")

    def remove_from_basket():
        x = basket_tree.selection()[0]
        basket_tree.delete(x)

    def checkout_basket():
        for child in basket_tree.get_children():
            sqldatacommands.add_to_orders(customer_info[0],sqldatacommands.find_product_id(basket_tree.item(child)["values"][0]),basket_tree.item(child)["values"][1])
            basket_tree.delete(child)
        messagebox.showinfo("DONE!","You placed your order!")

    basket_tree.place(x=30,y=10)

    finish_order = customtkinter.CTkButton(master=frame2, text="CHECKOUT",command=checkout_basket, font=("Roboto",15))
    finish_order.place(x= 30,y= 300)

    #Right Frame
    frame3 = customtkinter.CTkFrame(master=frame,height=350,width=300)
    frame3.place(x=570,y=100)

    select_product = customtkinter.CTkLabel(master=frame3, text="Please select your product", font=("Roboto",20))
    select_product.place(x=25,y=50)

    product_name = customtkinter.CTkComboBox(master=frame3,values=product)
    product_name.place(x=80,y=100)

    product_quantity = customtkinter.CTkEntry(master=frame3, placeholder_text="Quantity")
    product_quantity.place(x=80,y=150)

    add_order = customtkinter.CTkButton(master=frame3, text="Add to basket!",command=add_to_basket, font=("Roboto",15))
    add_order.place(x= 80,y= 200)

    remove_order = customtkinter.CTkButton(master=frame3, text="Remove from basket",command=remove_from_basket, font=("Roboto",15))
    remove_order.place(x= 80,y= 240)

    
    
    
    root.mainloop()

def MainStaffPage(staff_info = list):
    root = customtkinter.CTk()
    root.iconbitmap("estulogo.ico")
    root.geometry("900x500")


    #Main Frame
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=10,padx=10, fill = "both", expand = True)

    store_name = customtkinter.CTkLabel(master=frame, text="IKI EYLUL BIKE INTERFACE", font=("Roboto",40))
    store_name.place(x=200,y=20)

    def exit():
        root.destroy()
        LoginPage()

    def reflesh_page():
        root.destroy()
        MainStaffPage(staff_info)

    exit_button = customtkinter.CTkButton(master=frame,width=20,height=20,text="<",command=exit)
    exit_button.place(x=10,y=10)

    reflesh_button = customtkinter.CTkButton(master=frame,width=20,height=20,text="⟳",command=reflesh_page)
    reflesh_button.place(x=830,y=10)

    def SearchDataCommand():
        search_data_page(search_combobox.get())

    def AddProductCommand():
        add_data_page_product()

    def AddEmployerCommand():
        add_data_page_employer()

    def PendingOrders():
        accept_orders_page(staff_info)


    frame2 = customtkinter.CTkFrame(master=frame,height=350,width=250)
    frame2.place(x=10,y=100)

    staff_name = customtkinter.CTkLabel(master=frame2, text=staff_info[1], font=("Roboto",20))
    staff_name.place(x=10,y=10)

    search_combobox = customtkinter.CTkComboBox(master=frame2,values=tables,width=150)
    search_combobox.place(x=30,y=70)

    search_data = customtkinter.CTkButton(master=frame2, text="Seach Data",command=SearchDataCommand, font=("Roboto",15),width=150)
    search_data.place(x= 30,y= 120)

    add_product = customtkinter.CTkButton(master=frame2, text="Add Product",command=AddProductCommand, font=("Roboto",15),width=150)
    add_product.place(x= 30,y= 170)

    add_employer = customtkinter.CTkButton(master=frame2, text="Add Employer",command=AddEmployerCommand, font=("Roboto",15),width=150)
    add_employer.place(x= 30,y= 220)

    pending_orders = customtkinter.CTkButton(master=frame2, text="See Pending Orders",command=PendingOrders, font=("Roboto",15),width=150)
    pending_orders.place(x= 30,y= 270)

    


    #Employer Performance
    frame3 = customtkinter.CTkFrame(master=frame,height=160,width=275)
    frame3.place(x=300,y=100)

    new_employers_list = sqldatacommands.staff_performans()
    sizes = []
    labels = []
    explode = []
    colors = []
    for i in new_employers_list:
        labels.append(i[0])
        sizes.append(i[1])
        explode.append(0.05)
        colors.append('#20548C')


    fig = plt.figure(figsize=(1, 1), dpi=100)
    fig.set_size_inches(3.2, 1.7)
    fig.set_facecolor("#292929")
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140,textprops={'color':"w"})
    plt.axis('equal')
    

    canvasbar = FigureCanvasTkAgg(fig, master=frame3)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(x=10, y=30)

    table1_name = customtkinter.CTkLabel(master=frame3, text="Employers Performance", font=("Roboto",20))
    table1_name.place(x=30,y=0)
    
    #Pending Orders
    frame4 = customtkinter.CTkFrame(master=frame,height=160,width=275)
    frame4.place(x=585,y=100)

    pending_orders_list = sqldatacommands.pending_orders_counter()
    sizes = []
    labels = []
    explode = []
    colors = []
    for i in pending_orders_list:
        labels.append(i[0])
        sizes.append(i[1])
        explode.append(0.05)
        colors.append('#20548C')


    fig1 = plt.figure(figsize=(1, 1), dpi=100)
    fig1.set_size_inches(3, 1.7)
    fig1.set_facecolor("#292929")
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140,textprops={'color':"w"})
    plt.axis('equal')
    

    canvasbar = FigureCanvasTkAgg(fig1, master=frame4)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(x=10, y=30)

    table2_name = customtkinter.CTkLabel(master=frame4, text="Orders", font=("Roboto",20))
    table2_name.place(x=100,y=0)



    #Most Sold Products
    frame5 = customtkinter.CTkFrame(master=frame,height=170,width=275)
    frame5.place(x=300,y=280)

    sold_product_list = sqldatacommands.sold_product_counter()
    sizes = []
    labels = []
    explode = []
    colors = []
    for i in sold_product_list:
        labels.append(i[0])
        sizes.append(i[1])
        explode.append(0.05)
        colors.append('#20548C')


    fig3 = plt.figure(figsize=(1, 1), dpi=100)
    fig3.set_size_inches(3.2, 1.7)
    fig3.set_facecolor("#292929")
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140,textprops={'color':"w"})
    plt.axis('equal')
    

    canvasbar = FigureCanvasTkAgg(fig3, master=frame5)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(x=10, y=30)

    table3_name = customtkinter.CTkLabel(master=frame5, text="Sold Products", font=("Roboto",20))
    table3_name.place(x=70,y=0)

    #Customer Who Ordered Before
    frame6 = customtkinter.CTkFrame(master=frame,height=170,width=275)
    frame6.place(x=585,y=280)

    customer_placed_order_list = sqldatacommands.customer_who_order()
    sizes = []
    labels = []
    explode = []
    colors = []
    for i in customer_placed_order_list:
        labels.append(i[0])
        sizes.append(i[1])
        explode.append(0.05)
        colors.append('#20548C')


    fig3 = plt.figure(figsize=(1, 1), dpi=100)
    fig3.set_size_inches(3.2, 1.7)
    fig3.set_facecolor("#292929")
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140,textprops={'color':"w"})
    plt.axis('equal')
    

    canvasbar = FigureCanvasTkAgg(fig3, master=frame6)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(x=10, y=30)

    table4_name = customtkinter.CTkLabel(master=frame6, text="Customers", font=("Roboto",20))
    table4_name.place(x=90,y=0)

    root.mainloop()

#Login Page
def LoginPage():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.iconbitmap("estulogo.ico")
    root.geometry("900x500")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=10,padx=10, fill="both", expand=True)

    login_label = customtkinter.CTkLabel(master=frame, text="LOGIN", font=("Roboto",20))
    login_label.place(x=600,y=100)

    myimage = customtkinter.CTkImage(dark_image=Image.open("estuimage.png"),size=(500, 500))
    my_image = customtkinter.CTkLabel(master=frame,image=myimage,text="")
    my_image.place(x=50,y=50)

    id_number = customtkinter.CTkEntry(master=frame, placeholder_text="Id Number")
    id_number.place(x=600,y=150)

    password = customtkinter.CTkEntry(master=frame, placeholder_text="Password")
    password.place(x=600,y=200)

    def Login():
        new_id_number = int(id_number.get())
        new_password = password.get()
        root.destroy()
        sqldatacommands.login(new_id_number,new_password)


    def Register():
        root.destroy()
        RegisterPage()


    login_button = customtkinter.CTkButton(master=frame, text="LOGIN", command=Login, font=("Roboto",15))
    login_button.place(x=600,y=250)

    register_button = customtkinter.CTkButton(master=frame, text="REGISTER", command=Register, font=("Roboto",15))
    register_button.place(x=600,y=300)

    root.mainloop()

def RegisterPage():
    register = customtkinter.CTk()
    register.iconbitmap("estulogo.ico")
    register.geometry("900x500")

    register_frame = customtkinter.CTkFrame(master=register)
    register_frame.pack(pady=10,padx=10, fill="both", expand=True)

    myimage = customtkinter.CTkImage(dark_image=Image.open("estuimage.png"),size=(500, 500))
    my_image = customtkinter.CTkLabel(master=register_frame,image=myimage,text="")
    my_image.place(x=50,y=50)

    def exit():
        register.destroy()
        LoginPage()

    exit_button = customtkinter.CTkButton(master=register_frame,width=20,height=20,text="<",command=exit)
    exit_button.place(x=10,y=10)

    register_label = customtkinter.CTkLabel(master=register_frame, text="REGISTER", font=("Roboto",20))
    register_label.place(x=600,y=20)

    register_id_number = customtkinter.CTkEntry(master=register_frame, placeholder_text="Id Number")
    register_id_number.place(x=600,y=70)

    register_password = customtkinter.CTkEntry(master=register_frame, placeholder_text="Password")
    register_password.place(x=600,y=120)

    register_first_name = customtkinter.CTkEntry(master=register_frame, placeholder_text="First Name")
    register_first_name.place(x=600,y=170)

    register_last_tname = customtkinter.CTkEntry(master=register_frame, placeholder_text="Last Name")
    register_last_tname.place(x=600,y=220)

    register_phone = customtkinter.CTkEntry(master=register_frame, placeholder_text="Phone Number")
    register_phone.place(x=600,y=270)

    register_city = customtkinter.CTkEntry(master=register_frame, placeholder_text="City")
    register_city.place(x=600,y=320)

    register_zipcode = customtkinter.CTkEntry(master=register_frame, placeholder_text="Zip Code")
    register_zipcode.place(x=600,y=370)


    def button():
        id_number = int(register_id_number.get())
        password = register_password.get()
        first_name = register_first_name.get()
        last_name = register_last_tname.get()
        phone = int(register_phone.get())
        city = register_city.get()
        zip_code = int(register_zipcode.get())
        sqldatacommands.register(id_number,password,first_name,last_name,phone,city,zip_code)
        register.destroy()
        reflesh_lists()
        LoginPage()
        

    register_button = customtkinter.CTkButton(master=register_frame, text="REGISTER", command=button)
    register_button.place(x=600,y=420)



    

    register.mainloop()
