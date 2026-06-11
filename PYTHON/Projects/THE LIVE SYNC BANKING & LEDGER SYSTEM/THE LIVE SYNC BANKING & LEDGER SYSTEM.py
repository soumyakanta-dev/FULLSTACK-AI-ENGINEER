import os

current_directory = os.getcwd()
path = os.path.join(current_directory, 'bank_ledger.txt')

if os.path.exists(path):
    with open(path, 'r') as file:
        current_balance = int(file.read())
        print(current_balance)
else:
    current_balance = 0


def system_menu():
     print(f''' 
1. Deposit Money
2. Withdraw Money
3. View Current Live Balance
4. Exit & Commit to Ledger''')
     
def deposit_logic():
    deposit_money = input(f'Enter your deposit amount :- ')

    global current_balance

    if deposit_money.strip().isdigit():
        if int(deposit_money) > 0: 
            current_balance += int(deposit_money)
        else:
            print(f'Deposit Money Should be higher than 0.')
    else:
        print(f'please enter valid deposit amount.')

def withdrawl_logic():
    withdrawl_money = input(f'Enter your withdrawl amount :- ')

    global current_balance

    if withdrawl_money.strip().isdigit():
        if int(withdrawl_money) > 0:
            if int(withdrawl_money) <= current_balance:
                current_balance -= int(withdrawl_money)
            else:
                print(f'Withdrawl failed due to it is higher than current balance.')
        else:
            print(f'withdrawl amount should be higher than 0.')
    else:
        print(f'Please enter valid withdrawl amount')

def real_time_balance():
    global current_balance
    print(f'Your Current Live Balance is: ₹{current_balance}')

def persistent_commitment():
    with open(path, "w") as log:
        global current_balance
        log.write(f'{current_balance}')
        print(f'Final Synced Balance: {current_balance}')
        print(f'⫘⫘⫘⫘⫘⫘')
        print(f'Data securely flushed to disk. Goodbye!')


while True:
    system_menu()
    user_entry = input("Enter 1 or 2 or 3 or 4 :- ")

    if user_entry == "1":
        deposit_logic()
    
    elif user_entry == "2":
        withdrawl_logic()
    
    elif user_entry == "3":
        real_time_balance()
    
    elif user_entry == "4":
        persistent_commitment()
        break

    else:
        print(f'Enter valid menu option.')
        continue