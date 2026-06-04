# 1. The Classic Counter

number = 1

while number <= 10:
    print(f'{number}')
    number += 1


# 2. Backwards Countdown

numb = 10

while numb >= 1:
    print(f'{numb}')
    numb -= 1


# 3. Sum of First N Numbers

user_numb = int(input(f'Enter your number :- '))
i = 1
sum = 0

while i <= user_numb:
    sum += i
    i += 1
print(f'Sum of first {user_numb} is : {sum}')



# 4. User Controlled Exit

user_word = input(f"Enter any word or Enter 'exit' for quit :- ").lower()

while user_word != "exit":
    user_word = input(f"Enter any word or Enter 'exit' for quit :- ").lower()
print(f'YOU ARE QUIT!')




# 5. Multiples of 3 Finder

i = 1

while i <= 20:
    if i % 3 == 0:
        print(f'{i}')
    i += 1


# 6. Dynamic Power Sheet


i = 1

while i <= 5:
    print(f"2 ** {i} : {2 ** i}")
    i += 1


# 7. Dynamic Power Sheet

i = 11

while i <= 20:
    if i % 2 != 0:
        print(f'{i}')
    i += 1


# 8. Digital Attendance Counter

students = 1

while students <= 40:
    print(f'Roll NO {students} is Present.')
    students += 1

# 9. The Factorial Trial

i = 1
fact = 1

while i <= 4:
    fact *= i
    i += 1
print(f'The Fact of number {i-1} is : {fact}')


# 10. Interactive Password Matcher

user_password = input(f"Set Your Password :- ")

check_password = input(f"Check Your Password :- ")

while check_password != user_password:
    print(f'Wrong Password, Try Again!')
    check_password = input(f"Check Your Password :- ")

print(f'You correctly entered your Password.')
