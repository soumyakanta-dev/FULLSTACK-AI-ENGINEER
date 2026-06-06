total_cash = 0
while True:
    cash_input = input(f"User Please Enter your cash amount or exit :-  ")

    if cash_input.lower() == "exit":
        print(f"Counter Closed Here!")
        break

    if cash_input == "":
        print(f"Invalid Input")
        continue

    with open("cash_ledger.txt", "a") as file:
        file.write(f"{cash_input}\n")

    print(f"💾 Storage Status: {cash_input}rs safely locked into 'cash_ledger.txt'.\n")



with open("cash_ledger.txt", "r") as file:
    cash_collect = file.readlines()

for i in cash_collect:
    total_cash += int(i)

print(f"Total Cash Collection : {total_cash}")



with open("system_log_details.txt", "a") as log_file:
    log_file.write(f"Project Run Successfully.")

print(f"System is Shutting Down Now, GOODBYE!")



