# 1. ATM Withdrawal Simulator

enter_balance = int(input("Enter your funds :- "))
withdrawl_amount = int(input("Enter withdrawl amount :- "))

if withdrawl_amount <= enter_balance:
    remaining_balance = enter_balance - withdrawl_amount
    print(f"\nRemaining Balance : {remaining_balance}")
else:
    print(f"\nInsufficient Funds!")


# 2. Advanced Login with Max Attempts

set_username = input("Set a username :- ")
set_password = input("Set a password :- ")

check_username = input("Enter your username :- ")
check_password = input("Enter your password :- ")

if (check_username == set_username and check_password == set_password):
    print(f"\nWelcome Admin!")
else:
    print(f"\n1 Attempt used, 2 Remaining!")


# 3. Income Tax Calculator 

user_annual_income = int(input("Enter your Annual Income :- "))


if  user_annual_income <= 0:
    print(f"\nInvalid Credentials!")
elif user_annual_income <= 500000:
    tax = 0
elif user_annual_income < 1000000:
    tax = 10
else:
    tax = 20

if user_annual_income > 0:
    tax_amount = (user_annual_income * tax ) / 100
    net_income = user_annual_income - tax_amount
    print(f"\nApplied Tax Slab : {tax}%")
    print(f"\nFinal Net Amount : {net_income:.2f}\n")



# 4. Zodiac Sign Finder

user_birth_month = input("Enter your birth month :- ").lower()
user_birth_date = int(input("Enter your birth date :- "))

if (user_birth_month == "march" and 21 <= user_birth_date <= 31) or (user_birth_month == "april" and 0 < user_birth_date <= 19):
    print(f"\nYour Zodiac Sign is : ARIES \n")
elif (user_birth_month == "april" and 20 <= user_birth_date <= 30) or (user_birth_month == "may" and 0 < user_birth_date <= 20):
    print(f"\nYour Zodiac Sign is : TAURUS \n")
elif (user_birth_month == "may" and 21 <= user_birth_date <= 31) or (user_birth_month == "june" and 0 < user_birth_date <= 20):
    print(f"\nYour Zodiac Sign is : GEMINI \n")
elif (user_birth_month == "june" and 21 <= user_birth_date <= 30) or (user_birth_month == "july" and 0 < user_birth_date <= 22):
    print(f"\nYour Zodiac Sign is : CANCER \n")
elif (user_birth_month == "july" and 23 <= user_birth_date <= 31) or (user_birth_month == "august" and 0 < user_birth_date <= 22):
    print(f"\nYour Zodiac Sign is : LEO \n")
elif (user_birth_month == "august" and 23 <= user_birth_date <= 31) or (user_birth_month == "september" and 0 < user_birth_date <= 22):
    print(f"\nYour Zodiac Sign is : VIRGO \n")
elif (user_birth_month == "september" and 23 <= user_birth_date <= 30) or (user_birth_month == "october" and 0 < user_birth_date <= 22):
    print(f"\nYour Zodiac Sign is : LIBRA \n")
elif (user_birth_month == "october" and 23 <= user_birth_date <= 31) or (user_birth_month == "november" and 0 < user_birth_date <= 21):
    print(f"\nYour Zodiac Sign is : SCORPIO \n")
elif (user_birth_month == "november" and 22 <= user_birth_date <= 30) or (user_birth_month == "december" and 0 < user_birth_date <= 21):
    print(f"\nYour Zodiac Sign is : SAGITTARIUS \n")
elif (user_birth_month == "december" and 22 <= user_birth_date <= 31) or (user_birth_month == "january" and 0 < user_birth_date <= 19):
    print(f"\nYour Zodiac Sign is : CAPRICORN \n")
elif (user_birth_month == "january" and 20 <= user_birth_date <= 31) or (user_birth_month == "february" and 0 < user_birth_date <= 18):
    print(f"\nYour Zodiac Sign is : AQUARIUS \n")
elif (user_birth_month == "february" and 19 <= user_birth_date <= 29) or (user_birth_month == "march" and 0 < user_birth_date <= 20):
    print(f"\nYour Zodiac Sign is : PISCES \n")
else:
    print(f"\n Invalid Credentials, Enter Correctly!")



# 5. Uber Fare Estimator

total_distance = int(input(f"Enter Total Distance (K.M) :- "))
ride_type = input(f"Enter your ride type (mini/sedan/suv) :- ").lower()
total_fare = 0
if total_distance > 0:
    if ride_type == "mini":
        total_fare = 10 * total_distance   
    elif ride_type == "sedan":
        total_fare = 15 * total_distance   
    elif ride_type == "suv":
        total_fare = 25 * total_distance    
    else:
        print(f"Invalid Ride")
    if total_fare > 0:    
        print(f"Total Fare : {total_fare}")
else:
    print(f"Invalid Distance")


# 6. Student Grading System (GPA)

mark_subject1 = int(input(f'Enter your marks :- '))
mark_subject2 = int(input(f'Enter your marks :- '))
mark_subject3 = int(input(f'Enter your marks :- '))
mark_subject4 = int(input(f'Enter your marks :- '))
mark_subject5 = int(input(f'Enter your marks :- '))

average = (mark_subject1 + mark_subject2 + mark_subject3 + mark_subject4 + mark_subject5)/5

if average >= 90:
    print(f'Grade : A')
elif average >= 80:
    print(f'Grade : B')
elif average >= 70:
    print(f'Grade : C')
else:
    print(f'Grade : F')


# 7. Simple Chatbot Router 

user_inpt = input(f"Enter the SOS message (hello/ help/ price) :- ").lower()

if user_inpt == "hello":
    print(f'\nWelcome Boss! How r u?')
elif user_inpt == "help":
    print(f'\nTell me Boss! how can i help u ?')
elif user_inpt == "price":
    print(f'\nTell me Boss! What price about u want to know ?')
else:
    print(f'\nSorry! Out of Suggestions.... Try From the options.')


# 8. Game High-Score Tracker

high_score = 500
user_new_score = int(input(f'Enter your score :- '))

if user_new_score > high_score:
    print(f'\nNew High Score is Set!')
else:
    print(f'\nTry Again to beat the Record....')


# 9. Currency Converter Engine

user_inr_amount = int(input(f'Enter INR amount to Convert in other Currencies :- ')) 
option_menu = int(input(f'Enter 1 for USD or Enter 2 for EUR :- '))

if user_inr_amount > 0:
    if option_menu == 1:
        print(f'\n{user_inr_amount} in USD is {user_inr_amount * 95.81:.2f}')
    elif option_menu == 2:
        print(f'\n{user_inr_amount} in EUR is {user_inr_amount * 110.99:.2f}')
    else:
        print(f'\nEnter 1 or 2, NOthing ElSE')
else:
    print(f'\nEnter Positive INR amount...')


# 10. Restaurant Billing System with GST

item_price = int(input(f'Enter the amount of the item :- '))
item_quantity = int(input(f'Enter the quantity of the item :- '))

item_bill = item_price * item_quantity
tax_bill =  (item_bill * 18 ) / 100
final_bill = item_bill + tax_bill

if final_bill > 1000:
    net_payable_amount = final_bill - 100
    print(f'\n{net_payable_amount}')
else:
    net_payable_amount = final_bill
    print(f'\n{net_payable_amount}')
