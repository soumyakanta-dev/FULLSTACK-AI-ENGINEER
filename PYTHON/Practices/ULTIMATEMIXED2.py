# 1. The Safe Calculator Loop

while True:
    user_numb1 = int(input(f'Enter 1st number :- '))
    user_numb2 = int(input(f'Enter 2nd number :- '))
    choose_operator = input(f'Enter + , - , * , / , exit :- ')

    if choose_operator == "+":
        print(f'{user_numb1} {choose_operator} {user_numb2} = {user_numb1  + user_numb2}')

    elif choose_operator == "-":
        print(f'{user_numb1} {choose_operator} {user_numb2} = {user_numb1 - user_numb2}')

    elif choose_operator == "*":
        print(f'{user_numb1} {choose_operator} {user_numb2} = {user_numb1 * user_numb2}')

    elif choose_operator == "/":
        print(f'{user_numb1} {choose_operator} {user_numb2} = {user_numb1 / user_numb2}')


    elif choose_operator.lower() == "exit":
        print(f'You choose for exit!')
        break

    else:
        print(f"Invalid Synatax")
        break
    


# 2. Password Set and Match Limits

set_password = input(f'\nSet a Password :- ')

for attempts in range(1, 4):
    check_password = input(f"\nEnter your Password :- ")

    if check_password == set_password:
        print(f"Welcome!")
        break

    if attempts == 3:
        print(f"\nAccount Locked")
        break

    print(f"Wrong Password! {3- attempts} remaining...")


# 3. Skipping Even Multiples

for i in range(1, 16):
    if i % 3 == 0 and i % 2 == 0:
        continue
    print(f'{i}')


# 4. Hotel Room Rent Calculator

room_type = input(f'Enter Room Type (std / dlx) (std : 1000/nights) and (dlx : 2000/nights)  :-   ').lower()

std_room_night = 1000
dlx_room_night = 2000

total_bill = 0

nights = int(input(f'How Many nights do u want to stay :-   '))

if room_type == "std":
    if nights > 5:
        total_bill = (nights * std_room_night) * 0.9
    else:
        total_bill = (nights * std_room_night)

elif room_type == "dlx":
    if nights > 5:
        total_bill = (nights * dlx_room_night) * 0.9
    else:
        total_bill = (nights * dlx_room_night)

else:
    print(f'Invalid Credentials !')

if total_bill > 0:
    print(f"""\n-----Total Bill------\n
Total Nights : {nights}
Room Type :  {room_type}
Bill : {total_bill}
          """)



# 5. Dynamic Grade Collector


while True:
    student_marks = int(input(f"\nEnter your marks :- "))
    if student_marks > 100:
        print(f"Are u Dumb please enter your marks between 0 to 100.\n")
    elif 50 <= student_marks <= 100:
        print(f"Passed!")
    elif student_marks < 0:
        break
    elif student_marks <= 50:
        print(f'Failed!')


# 6. FizzBuzz Micro-Logic

for number in range(1, 11):
    if number % 3 == 0:
        print(f"Fizz")
    elif number % 5 == 0:
        print(f'Buzz')
    else:
        print(f'{number}')


# 7. Limited ATM Cash Dispenser

vault_cash = 2000


while True:
    withdrawl_amount = int(input(f"Enter Withdrawl amount :- "))

    if withdrawl_amount > vault_cash:
        print(f"Sorry we can't do it. We have only {vault_cash}rs, {withdrawl_amount}rs is bigger than this.")
        continue
    
    vault_cash -= withdrawl_amount
    print(f"Continue Withdraw, {vault_cash}rs Remaining....")

    if vault_cash == 0:
            print(f"Vault is empty!")
            break
    


# 8 . Skipping Odd Character Positions

user_name = input(f"Enter your name :-  ")
count = 1

for i in user_name:
    if count % 2 == 0:
        count += 1
        continue
    else:
        print(f'{i}')
    count += 1


# 9. Multi-Item Tax Invoicer

total_price = 0 

for price in range(1, 4):
    enter_price = int(input(f"Enter Price of the Product :-  "))

    if enter_price > 500:
        price = enter_price + (enter_price * 18 / 100)
    elif enter_price <= 500:
        price = enter_price + (enter_price * 5 / 100)

    total_price += price   
    

print(f'{total_price}')


# 10. Age Bracket Counter

children = 0
adult = 0

for member in range(1, 5):
    member_age = int(input("Enter your family member's age :-   "))

    if member_age >= 18:
        adult += 1
    elif 0 < member_age < 18:
        children += 1
    else:
        print(f"Invalid age!")
        break

print(f"\nTotal Children in your Family : {children}")
print(f"Total Adult in your Family : {adult}\n")



# 11. The Smart Petrol Pump Dispenser

total_petrol = 50

while True:
    user_petrol = int(input(f"Enter your Petrol Quantity(lts) :-  "))

    if user_petrol > total_petrol:
        print(f"Sorry We don't have That much petrol, we have {total_petrol}ltrs Only")
        continue

    total_petrol -= user_petrol
    print(f"\n{user_petrol}ltrs Gone, {total_petrol}ltrs Remaining....")

    if total_petrol == 0:
        print(f"Pump Out of Stock! Closing for the day.")
        break


# 12. The Duplicate Word Letter Finder

users_word = input(f"Enter repeated letter word :-   ")
position = 1

for i in users_word:
    if position % 2 == 0:
        position += 1
        continue
    
    print(f'{i}')
    position += 1




# 13. Daily Expense Budget Manager'

total_expense = 0

for day in range(1, 5):
    user_expense = int(input(f"Enter your daily Expense :-  "))

    if user_expense >= 1000:
        total_expense += user_expense + 50
    else:
        total_expense += user_expense

print(f"Your Total Expense is : {total_expense}")




# 14. Uber Shared Ride Cap Limit


seating_capacity = 4

while True:
    passengers_number = int(input(f"How many passengers in your group? :-  "))

    if passengers_number > seating_capacity:
        print(f"Sorry, not enough seats for your group!")
        continue

    seating_capacity -= passengers_number
    print(f"{passengers_number}seats are fulled, {seating_capacity}seats are remaining.....")

    if seating_capacity == 0:
        print(f"Car is Full! Starting the ride now.")
        break


# 15. Google Form Username Filter


user_fullname = input(f"Enter your full name :-    ")
char_count = 0

for i in user_fullname:
    if i == " ":
        char_count += 1
        continue

    if char_count == 8:
        print(f"Limit Reached at 8th character!")
        break

    print(f"{i}")
    char_count += 1

