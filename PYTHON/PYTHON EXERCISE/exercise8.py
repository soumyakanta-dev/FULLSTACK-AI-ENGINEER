secret_pin = 2580
attempts = 3

while attempts > 0:
    entered_pin = int(input("Enter PIN :- "))
    if entered_pin == secret_pin:
        print(f"\nAccess Granted!")
        break
    attempts -= 1

    if attempts > 0:
        print(f"\nWrong Pin, Try Again!")
    else:
        print(f"\nCard Blocked! Too many Wrong attempts.")


total_amount = 0

for item in range(1, 6):
    price = int(input(f"Enter price of the item {item} :- "))
    if price <= 0:
        print(f"Invalid Price! Skipping this item...")
        continue

total_amount += price

print(f"\nTotal bill is : {total_amount}")

    

