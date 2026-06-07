# # 1. The Dynamic Price Ingestion Ledger

# with open("args.txt", "w") as file:
#     file.write(f"----------ARGS1 STARTS FROM HERE----------\n")
    
# def backup_item_prices(category_name, *args):
#     print(f"Category: {category_name}\n")

#     with open("args.txt", "a") as file:
#         file.write(f"Category: {category_name}\n")

#         for i in args:
#             print(f"Price : {i}")
#             file.write(f"Price : {i}\n")
    
# backup_item_prices("Dairy Stock", 60.50, 160.00, 320.00)




# # 2. The Bulk Employee Whitelist Engine

# with open("args.txt", "a") as file:
#     file.write(f"\n\n----------ARGS2 STARTS FROM HERE----------\n")

# def register_staff_bulk(department, *args):

#     with open("args.txt", "a") as file:

#      for i in args:
#         print(f"\n Staff : {i} | Dept : {department}")
#         file.write(f'\nStaff : {i} | Dept : {department}')

# register_staff_bulk("Operations", "Soumya")





# # 3. Multi-Layer Attendance Audit Tracker

# with open("args.txt", "a") as file:
#     file.write(f"\n\n----------ARGS3 STARTS FROM HERE----------\n")

#     file.write(f"\nName of Employee Present Today :- ")

# def audit_daily_attendance(date_string, *args):

#     with open("args.txt", "a") as file:

#         for i in args:
#          print(f'\n{i} is present Today.')
#          file.write(f'\n{i}')  


#     print(f'\nDate: {date_string} | Total Headcount: {len(args)}\n')        

#     with open("args.txt", "a") as file:
#         file.write(f'\n\nDate: {date_string} | Total Headcount: {len(args)}\n')

# audit_daily_attendance("07-06-2026", "Soumya", "Tarun", "Hrushikesh")





# # 4. The Strict Integer Stream Filter

# with open("args.txt" , "a") as file:
#     file.write(f"\n\n----------ARGS4 STARTS FROM HERE----------\n")

#     file.write(f"\nTotal Filtered Numbers are : ")

# def filter_and_save_scores(*args):

#     print(f"Total Filtered Numbers are : ")

#     with open("args.txt", "a") as file:
        
#         for i in args:
#          if i >= 100:
#             print(f"{i}")
#             file.write(f"\n{i}")

# filter_and_save_scores(45, 120, -50, 300, 99, 150)





# # 5. Full Cycle String Concatenation Dump


# with open("args.txt", "a") as file:
#     file.write("\n\n----------ARGS5 STARTS FROM HERE----------\n")

# def merge_text_stream(filename, *args):

#     word = " ".join(args)

#     print(f"\nFile Name: {filename} | Merge_word = {word}\n")

#     with open("args.txt", "a") as file:
#         file.write(f"\nFile Name: {filename} | Merge_word = {word}\n")

# merge_text_stream("sentence.txt", "Puri", "Business", "Management", "System")


# with open("args.txt", "r") as file:
#     read = file.read()
#     #print(read)






########################################################################################################################################





# 6. Dynamic Supplier Matrix Locker


with open("kwargs.txt", "w") as files:
    files.write(f"\n**************** KWARGS 1 STARTS HERE ***************\n")


def lock_supplier_meta(supplier_name, **kwargs):

    with open("kwargs.txt", "a") as files:
        files.write(f"\nSupplier Name : {supplier_name}")

        print(f"\nSupplier Name : {supplier_name}")

        for k, v in kwargs.items():
            print(f'{k} : {v}')
            files.write(f'{k} : {v}\n')


lock_supplier_meta("Khushboo Agency", city="Puri", rating=5, items_supplied=22)



# 7. Automated Product Specification Index

with open("kwargs.txt", "a") as files:
    files.write(f"\n**************** KWARGS 2 STARTS HERE ***************\n")

def index_product_spec(product_id, **kwargs):

    with open("kwargs.txt", "a") as files:
        files.write(f"\nProduct_id : {product_id}")

        print(f"\nProduct_id : {product_id}")
    
        for k, v in kwargs.items():
            print(f"{k} : {v}")
            files.write(f"{k} : {v}\n")

index_product_spec("PROD_991", brand="Amul", protein="15g", type="Buttermilk")



# 8. Smart Application Settings Configurator

with open("kwargs.txt", "a") as files:
    files.write(f"\n**************** KWARGS 3 STARTS HERE ***************\n")

def update_app_config(**kwargs):

    print(f"\nSettings of Application :- ")

    with open("kwargs.txt", "a") as files:
        files.write(f"\nSettings of Application :- ")
        
        for k, v in kwargs.items():
            print(f'{k} : {v}')

            files.write(f'{k} : {v}\n')

update_app_config(theme="Dark Mode", font_size=14, automatic_backup="ENABLED")



# 9. Financial Due Alert Flag Checking (The Conditional Challenge)

with open("kwargs.txt", "a") as files:
    files.write(f"\n**************** KWARGS 4 STARTS HERE ***************\n")


def flag_high_dues(**kwargs):

    with open("kwargs.txt", "a") as files:
        files.write(f"CRITICAL DUE ALERT :- ")

        for k, v in kwargs.items():

            if v >= 5000:
                print(f"""\n
⚠️ CRITICAL DUE ALERT -\n 
Supplier: {k}  
Balance: {v}\n""")
                files.write(f"Supplier: {k} | Balance: {v}\n")

flag_high_dues(Khushboo_Agency=4500, Milky_Mist=12000, Amul_Distributor=3200)



# 10. Complete Inventory Voucher (Triple Quote Challenge)

with open("kwargs.txt", "a") as files:
    files.write(f"\n**************** KWARGS 5 STARTS HERE ***************\n")


def generate_dynamic_voucher(voucher_id, **kwargs):

    with open("kwargs.txt", "a") as files:
        files.write(f"\nVoucher_id : {voucher_id}")

        print(f"\nVoucher_id : {voucher_id}")

        for k, v in kwargs.items():
            print(f'''{k} : {v}''')
            files.write(f'''{k} : {v}\n''')
            
generate_dynamic_voucher("VOUCH_JUNE_07", Total_Items=15, Cashier="Soumya", Mode="Cash Counter")


with open("kwargs.txt", "r") as files:
    content = files.read()
    # print(content)