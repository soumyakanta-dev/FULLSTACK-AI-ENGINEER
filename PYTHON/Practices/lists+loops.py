# 1. The Brand Displayer

brands = ["Amul", "Milky Mist", "Quaker"]

for i in brands:
    print(f"{i}")


# 2. Supplier Notification Sender

suppliers = ["Khushboo Agency", "Mahadev Company", "Sriram Enterprises"]

for i in suppliers:
    print(f"Notification sent to {i}")


# 3. The Numeric Expense Sum

expenses = [200, 500, 150, 1200]
total_expenses = 0

for i in expenses:
    if i > 0:
        total_expenses += i
    else: 
        print(f"Invalid")
print(f"Total Expenses : {total_expenses}")


# 4. Veg Product Checker

menu = ["Paneer Tikka", "Chicken Roll", "Dal Makhani", "Egg Bhurji"]

for i in menu:
    if ("chicken") in i.lower() or ("egg") in i.lower():
        continue
    else:
        print(f'Veg Items : {i}')


# 5. Expensive Price Alert

prices = [450, 1200, 800, 2300, 150]

for i in prices:
    if i > 1000:
        print(f"Premium Price: {i}")


# 6. Target Multiplier Loop

numbers = [1, 2, 3, 4, 5]

for i in numbers:
    print(f"{i * 10}")


# 7. Small Stock Detector

quantities = [50, 12, 85, 5, 120]

for stock in quantities:
    if stock < 20:
        print(f"Stock is lesser than 20")


# 8. Word Length Scanner (Micro-Logic)

words = ["Oats", "Milk", "Banana", "Chia"]

for i in words:
    print(f"Length of {i} : {len(i)}")


# 9. Dynamic Accumulator with Surcharge

bills = [300, 700, 1500]
total_bills = 0
extra_delivery_charges = 20

for i in bills:
    if i > 0:
        total_bills += extra_delivery_charges + i

print(f"Total Bill : {total_bills}")


# 10. Odd Numbers Filter from List

mixed_data = [12, 15, 22, 33, 40, 55]

for i in mixed_data:
    if i % 2 == 0:
        continue
    print(f"{i}")