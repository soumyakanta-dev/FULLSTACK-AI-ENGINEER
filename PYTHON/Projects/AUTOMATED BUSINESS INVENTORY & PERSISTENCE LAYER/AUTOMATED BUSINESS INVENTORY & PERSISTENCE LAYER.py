database_manager = []


def show_menu():
    print(f'''\n
          1, Add Suppliers and Products 
          2, Display the Stocks
          3, Exit from the loops \n''')
    



def add_name():
    suppplier_name = input(f'Enter Supplier Name:- ')
    product_name = input(f'Enter Product Name:- ')
    current_stock = input(f'Enter Stock Quantity:- ')

    if int(current_stock) >= 0:
        database_manager.append({'Supplier Name' : suppplier_name, 'Product Name' : product_name, 'Current Stock' : current_stock})
    else:
        show_menu()



def display_stock():
    for item in database_manager:
        print(f"'Supplier Name' - {item['Supplier Name']} | 'Product Name' - {item['Product Name']} | 'Current Stock' - {item['Current Stock']}\n")


def break_handle():
    with open("inventory_ledger.txt", "a") as files:
        for item in database_manager:
            files.write(f"'Supplier Name' - {item['Supplier Name']} | 'Product Name' - {item['Product Name']} | 'Current Stock' - {item['Current Stock']}\n")

        print(f'Successfully Saved the Data, Now Exiting........')



while True:
    show_menu()
    user_choices = input("Enter your Choices in 1 or 2 or 3 :- ")

    if user_choices == "1":
        add_name()

    elif user_choices == "2":
        display_stock()
    
    elif user_choices == "3":
        break_handle()
        break

    else:
     print(f'Please Enter 1 or 2 or 3.')
     continue







