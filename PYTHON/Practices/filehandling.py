# 1. The Live Inventory Appending Engine (Continuous Input)

while True:
    item_name = input(f'Enter name of the item or enter "exit" :-   ')

    if item_name == "exit":
        break

    with open("inventory_log.txt", "a") as file:
        file.write(f'\n{item_name}')

with open("inventory_log.txt", "r") as file:
    content = file.read()
    print(content)



# 2. Business Supplier Authentication Guard (Read & Verify)


with open("approved_suppliers.txt", "a") as file:
    file.write("Khushboo Agency\n")
    file.write( "Milky Mist\n")

user_supplier_name = input(f"Enter Supplier Name : ")

with open("approved_suppliers.txt", "r") as file:
    file_content = file.read()

    if user_supplier_name in file_content:
        print(f"Access Granted ✅")
    else:
        print("Access Denied ❌")    



# # 3. Dynamic Expense Calculator Ledger (Mathematical Extraction)


with open("daily_expenses.txt", "a") as file:
    file.write("450\n")
    file.write("1200\n")
    file.write("300\n")
with open("daily_expenses.txt", "r") as file:
    content = file.read().splitlines() 


total_sum = 0

for i in content:
    if i != "":
        total_sum += int(i)
print(total_sum)




# 4. The Overwrite Safety Switch (Write vs Append Experiment)


with open("security_key.txt", "w") as file:
    file.write("OLD_SECRET_KEY_123\n")

with open("security_key.txt", "w") as file:
    file.write("NEW_SECRET_KEY_999\n")

with open("security_key.txt", "r") as file:
    content = file.read()

print(content)



# 5. Automated System Logger (Timestamp Matrix)


task_name = input("Enter your task name :-   ")
status = input("Enter your status of task :- ")

clean_format = f"[Task Name : {task_name} | Status: {status}\n"

with open("system_logs.txt", "a") as file:
    file.write(clean_format)
    position = file.tell()
    print(position)