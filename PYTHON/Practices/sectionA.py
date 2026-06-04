# 1. Biodata Generator

user_Name = input("Enter your name:- ")
user_Age = input("Enter your age:- ")
user_City = input("Enter your city:- ")
user_Profession = input("Enter your profession:- ")

print("\n----USER DETAILS----")
print(f"Full Name :- {user_Name}")
print(f"Age :- {user_Age}")
print(f"City:- {user_City}")
print(f"Profession:- {user_Profession}")


# 2. Simple Interest Calculator

principal_Amount = float(input("Enter the principal amount:- "))
rate_Of_Interest = float(input("Enter the rate of interest:- "))
time_Period = float(input("Enter the time period(in years):- "))
simple_Interest = (principal_Amount * rate_Of_Interest * time_Period) / 100

print(f"Simple Interest:- {simple_Interest:.2f}\n")


# 3. Temperature Converter

celsius_Temperature = float(input("Enter the temperature in Celsius:- "))
farenheit_Temperature = (celsius_Temperature * 9/5) + 32

print(f"Temperature in Farenheit:- {farenheit_Temperature:.1f}")


# 4. Year of Birth Calculator

user_Current_Age = int(input("Enter your current age:- "))
current_Year =2026
year_Of_Birth = current_Year - user_Current_Age

print(f"\nYour year of Birth is : {year_Of_Birth}")


# 5. Rectangle Area & Perimeter
length_Of_Rectangle = float(input("Enter the length of the rectangle :- "))
width_Of_Rectangle = float(input("Enter the width of the rectangle :- "))
area_Of_Rectangle = length_Of_Rectangle * width_Of_Rectangle
perimeter_Of_Rectangle = 2 * (length_Of_Rectangle + width_Of_Rectangle)

print(f"\nArea of the Rectangle is : {area_Of_Rectangle:.2f}")
print(f"\nPerimeter of the Rectangle is : {perimeter_Of_Rectangle:.2f}")


# 6. BMI Calculator

user_weight = float(input("Enter your weight(K.G):- "))
user_height = float(input("Enter your height(M):- "))

bmi = user_weight / (user_height ** 2)
print(f"\nYour BMI is : {bmi:.2f}")


# 7. Salary Increment Calculator
user_Current_Salary = float(input("Enter your current salary:- "))
increment_Perecentage = 10
increment_Amount = (user_Current_Salary * increment_Perecentage) / 100

new_Salary = user_Current_Salary + increment_Amount

print(f"\nNew Salary Amount is: {new_Salary:.2f}")


# 8. Seconds to Minutes

user_Seconds = int(input("Enter seconds :- "))
minutes = user_Seconds / 60

print(f"\n{user_Seconds}seconds in minutes is : {minutes:.2f}")


# 9. Trip Cost Calculator
total_distance = float(input("Enter total distance :- "))
fuel_Price = float(input("Enter the price of fuel :- "))
mileage = float(input("Enter your mileage :- "))

expense = (total_distance / mileage ) * fuel_Price

print(f"\nTrip expense is : {expense:.2f}")


# 10. Word Joiner Story
user_noun1st = input("Enter your 1st Noun :- ")
user_noun2nd = input("Enter your 2nd Noun :- ")
user_noun3rd = input("Enter your 3rd Noun :- ")
user_verb = input("Enter your Verb :- ")

print(f"\nFunny Line : {user_noun1st} {user_noun2nd} {user_verb} {user_noun3rd}")
