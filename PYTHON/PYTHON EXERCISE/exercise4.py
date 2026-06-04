user_age = int(input("What is your age? "))

if user_age >= 18:
    print("You are eligible for voting.")
else:
    print("Now You are not eligible for voting.")


score = int(input("Enter your score? "))

if score >= 100:
    print("Superb! you are a pro coder.")
elif score >= 50:
    print("Good Job! Keep practicing.")
else:
    print("Don't Give Up! Code again tomorrow")