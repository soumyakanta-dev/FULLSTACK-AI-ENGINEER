# 1. Traffic Light Simulator

user_color_input = input("Enter your color(R/Y/G) :- ").lower()

if user_color_input == "r":
    print(f"\nSTOP.")
elif user_color_input == "y":
    print(f"\nWAIT.")
elif user_color_input == "g":
    print(f"\nGO.")
else:
    print(f"\nINVALID COLOR ENTERED.")


# 2. Pass/Fail Checker

user_subject1 = int(input("Enter your mark of 1st subject:- "))
user_subject2 = int(input("Enter your mark of 2nd subject:- "))
user_subject3 = int(input("Enter your mark of 3rd subject:- "))

average_mark = (user_subject1 + user_subject2 + user_subject3) / 3

if average_mark > 40:
    print(f"\nPASSED.")
else:
    print(f"\nFAILED")



# 3. Odd or Even Number

user_number = int(input("Enter your number :- "))

if user_number % 2 == 0:
    print(f"\nYour entered numnber is a even number.")
else:
    print(f"\nYour entered number is a odd number.")



# 4. Electricity Bill Calculator


user_consumed_unit = int(input("Enter How many Units you consumed :- "))

if user_consumed_unit <= 100 and user_consumed_unit > 0:
    print(f"\nYour electricity bill is {user_consumed_unit * 5}rs")
elif user_consumed_unit > 100:
    print(f"\nYour electricity bill is {user_consumed_unit * 10}rs")
else:
    print(f"\nYou entered something wrong!")



# 5. Leap Year Checker

user_year = int(input("Enter year for checking it leap year or not :- "))

if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
    print(f"\nYour entered year is a leap year.")
else:
    print(f"\nYour entered year is not a leap year.")



# 6. Movie Ticket Pricing

user_age = int(input("Enter your age :- "))

if user_age < 12:
    print(f"\nYour ticket price is 150rs.")
elif user_age >= 12 and user_age< 60:
    print(f"\nYour ticket price is 300rs.")
elif user_age >= 60:
    print(f"\nYour ticket price is 200rs.")
else:
    print(f"\nPlease enter a valid age.")
    


# 7. E-Commerce Discount Finder

total_shopping_amount = int(input("Enter your total shopping amount :- "))

if total_shopping_amount > 5000:
    print(f"\nYeah! you got 20% discount.")
elif total_shopping_amount >= 2000:
    print(f"\nYou got 10% discount.")
else:
    print(f"\nOOPS! you don't get any kind of discount.")



# 8. Triangle Validity

user_angleA = int(input("Enter the value of angle A :- "))
user_angleB = int(input("Enter the value of angle B :- "))
user_angleC = int(input("Enter the value of angle C :- "))

angle_sum = user_angleA + user_angleB + user_angleC

if angle_sum == 180:
    print(f"\nThis is a valid triangle.")
else:
    print(f"\nINVALID.")



# 9. Rock-Paper-Scissors

input_user1 = input("Enter your input (R/ P/ S) :- ").upper()
input_user2 = input("Enter your input (R/ P/ S) :- ").upper()

if input_user1 == "R" and input_user2 == "P":
    print(f"\nUser2 Won!")
elif input_user1 == "R" and input_user2 == "S":
    print(f"\nUser1 Won!")
elif input_user1 == "P" and input_user2 == "S":
    print(f"\nUser2 Won!")
elif input_user1 == "P" and input_user2 == "R":
    print(f"\nUser1 Won!")
elif input_user1 == "S" and input_user2 == "P":
    print(f"\nUser1 Won!")
elif input_user1 == "S" and input_user2 == "R":
    print(f"\nUser2 Won!")
elif input_user1 == input_user2:
    print(f"\nTIED! TRY AGAIN.")
else:
    print(f"\nInvalid.")


# 10. Blood Donation Eligibility

user_age_now = int(input("Enter your age :- "))
user_weight_now = int(input("Enter your weight (K.G) :- "))

if user_age_now >= 18 and user_weight_now >= 50:
    print(f"\nYou are eligible for blood donation.")
else:
    print(f"\nYou are not eligible for this, SORRY!")

