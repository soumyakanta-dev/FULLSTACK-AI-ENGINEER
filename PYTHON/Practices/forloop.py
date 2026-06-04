# 1. The Counter Multiply

user_num = int(input(f'Enter a number :- '))

for i in range(1, 6):
    print(f'{i * user_num}')


# 2. Average Calculator

total_marks = 0
valid_subjects = 0

for i in range(1, 5):
    user_marks = int(input(f'Enter your marks :- '))
    if 0 < user_marks < 100:
        total_marks += user_marks
        valid_subjects += 1
    else:
        print(f'Enter only Positive marks and in between 0 to 100 and Try Again.')
        break

if valid_subjects > 0:
    print(f'\nTotal Marks : {total_marks}')
    print(f'\nAverage : {total_marks/valid_subjects:.2f}')


# 3. Square Sheet Generator

for i in range(1, 8):
    print(f'{i} * {i} = {i * i}')


# 4. Reverse Step Counting

for i in range(20, 0, -5):
    if i % 5 == 0:
        print(f'{i}')


# 5. Character Speller

username = input(f'Enter your name :- ')

for i in username:
    print(f'{i}')


# 6. Dynamic Star Pattern

user_number = int(input(f'Enter a number :- '))

for i in range(1, user_number + 1):
    print(f'{i * '*'}')


# 7. Cubes Finder

for i in range(10, 16):
    print(f'cube of {i} : {i * i * i}')


# 8. Product of Range

product = 1

for i in range(1, 6):
    product *= i
print(f'\nProduct till {i} is {product}\n')


# 9. Gym Schedule Tracker

for day in range(1, 8):
    if day == 7:
        print(f'Day 7: Rest Day')
    else:
        print(f'Day {day}: Workout Day')

# 10. Salary Multiplier

salary = 10000

for years in range(1, 5):
    salary = salary + ((salary * 10)/ 100)
    print(f'{years} increment salary is {int(salary)}')