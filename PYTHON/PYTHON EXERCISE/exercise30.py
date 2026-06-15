user_num = input("enter a number :- ")

try:
    clean_num = int(user_num)

except ValueError:
    print(f'Invalid Number')

else:
    print(f'Conversion Successfully')

finally:
    print(f'Execution Finished')