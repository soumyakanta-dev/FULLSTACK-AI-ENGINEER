while True:
    try:
        user_birth_year = input(f'Enter your birth year :- ')
        birth_year = int(user_birth_year)
        user_age = 2026 - birth_year
        print(f'your age is {user_age}')
        break
    except Exception:
        print(f'Enter the correct number')
