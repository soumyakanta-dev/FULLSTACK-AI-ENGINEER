# 1. The Number Stopper

for i in range(1, 10):
    if i == 7:
        print(f'\nNumber 7 detected! Stopping loop.\n')
        break
    print(f'{i}')


# 2. Skip Multiples of 5

for i in range(1, 20):
    if i % 5 == 0:
        continue
    print(f'{i}')


# 3. Infinite Budget Shopping

budget = 500

while True:
    item_price = int(input(f'Enter the price of the item :- '))
    budget -= item_price
    if budget <= 0:
        print(f'Budget Exceeded!')
        break


# 4. Vowel Skip Tool

user_name = input(f'Enter your Name :- ').lower()

for i in user_name:
    if i in ["a", "e", "i", "o", "u"]:
        continue
    print(f'{i}')


# 5. Dynamic Number Search

for i in range(10, 21):
    if i % 13 == 0:
        print(f'Found the match!')
        break


# 6. Positive Numbers Sum

total_sum = 0

for i in range(1, 6):
    user_number_input = int(input(f'Enter a Positive number :- '))
    if user_number_input<= 0:
        print(f'Warning! Enter a positive number (no 0)')
        continue
    total_sum += user_number_input
print(f"Total Sum of Positive number : {total_sum}")


# 7. OTP Verification Max Attempts

correct_otp = 4455

for attempts in range(1, 4):
    check_otp = int(input(f'Enter your otp :- '))

    if check_otp == correct_otp:
        print(f"Verification Successful")
        break

    if attempts == 3:
        print(f"Wrong Otp! Verification failed.")
        break

    print(f'Wrong Otp! {3 - attempts}attempts left.')


# 8. Odd Index Skip

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(f"{i}")


# 9. Stock Alert System

inventory = 3 

while True:
    user_quant = int(input(f'How many items do u need ? - '))

    if user_quant > inventory:
        print(f"Sorry we have only {inventory} left, you can't buy {user_quant}items.")
    inventory -= user_quant
    if inventory == 0:
        print(f"Out of Stock!")
        break
    print(f"You can buy {inventory}items more")


# 10. Skipping Specific Floor

for lift in range(1, 8):
    if lift == 4:
        print(f"4th Floor is under Maintainance.....")
        continue
    print(f"Landed on Floor {lift}")
