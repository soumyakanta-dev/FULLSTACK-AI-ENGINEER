# secret_number = 7
# user_guess = int(input("Guess the secret number :- "))
# while user_guess != secret_number:
#     print(f"Wrong Guess! Try Again.")
#     user_guess = int(input("Guess the secret number :- "))
# print(f"\nCongratulations! You Guessed the right number.")



# countdown = 5
# while countdown > 0:
#     print(f"\nT-Minus {countdown} seconds")
#     countdown = countdown - 1
# print(f"\nBLAST OFF! Rocket Launched.")


# current_pin = 1234
# entered_pin = int(input("Enter your 4-digit pin :- "))
# while entered_pin != current_pin:
#     print(f"\n Wrong Pin Entered! Acces Denied, Try Again....")
#     entered_pin = int(input("Enter your 4-digit pin :- "))
# print(f"\n You entered the right PIn, Welcome....")


seats = 5

while seats > 0:
    user_name = input("Enter your Name :- ")
    print(f"{user_name} entered! {seats -1} remaining.\n")
    seats = seats - 1
print(f"\nAll seats are full, SORRY!")