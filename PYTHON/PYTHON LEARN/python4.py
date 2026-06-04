# Hum user se unka daily coding time pooch rahe hain
coding_hours = int(input("For how long you did coding? "))

# Agar coding_hours 2 ya usse zyada hai (>= means greater than or equal to)

if coding_hours >= 2:
    print('Great! You are on the right track')
else:
    print("Dont worry, but you will definately fulfill your 2 hour study plan tomorrow")


# Checking if a number is positive or negative
number = int(input("Enter a number:- "))

if number >= 0:
    print("It is a positive number")
else:
    print("It is negative number")



#Grading system based on marks4
marks = 70

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C, Needs Improvement!")