ledger_database = []

def expense_options():
    print(f''' 
1. Log Expense (Supplier Bill / Asset Purchase)
2. View Total Ledger Balance
3. Commit & Backup Data to File''')
    
def dynamic_logs():
    expense_name = input(f'Enter Expense Name :- ')
    category_name = input(f'Enter Category Name (Supplier / General):- ').lower()
    amount_paid = input(f'Enter Amount Paid For :- ')

    if expense_name == "":
        print(f'Expense Name can not be Empty.')
        return
    
    if category_name != "supplier":
        category_name = "general"
    
    if amount_paid.isdigit() == True:
        if int(amount_paid) > 0:
            ledger_database.append({'Expense' : expense_name, 'Category' : category_name, 'Amount' : int(amount_paid)})
        else:
            print(f'Amount never be a negative value.')
    else:
        print(f'Paid Amount always be in Numeric.')


       

def display_ledger():
   total_supplier_outflow = 0
   total_general_outflow = 0
   

   target_supplier_category = "supplier"
   target_general_category = "general"

   if not ledger_database:
      print(f'Database is empty now.')
      return
   
   for item in ledger_database:
      
        if item.get('Category') == target_supplier_category:
            target_supplier_amount = item.get('Amount')
            total_supplier_outflow += target_supplier_amount

        elif item.get('Category') == target_general_category:
            target_general_amount = item.get('Amount')
            total_general_outflow += target_general_amount

   grand_total = total_supplier_outflow + total_general_outflow
   print(f'Total Supplier Amount : {total_supplier_outflow}')
   print(f'Total General Amount : {total_general_outflow}')
   print(f'Grand Total : {grand_total}')
         

def saving_ledger():
   with open('expense_ledger.txt' , 'a') as file:

    for item in ledger_database:
       file.write(f"Expense: {item['Expense']}, Category: {item['Category']}, Amount: {item['Amount']}\n")

    print(f'Data Saved Succesfully, Exiting Goodbye.....')


while True:
   expense_options()
   user_options = input("Enter your Choice :- ")

   if user_options == "1":
      dynamic_logs()

   elif user_options == "2":
      display_ledger()

   elif user_options == "3":
      saving_ledger()
      break
   
   else:
      print(f'no strings are allowed only 1,2,3')


   

    
      
