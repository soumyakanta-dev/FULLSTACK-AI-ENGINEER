# LOOPS IN DICTIONARY
supplier_profile = {
    "agency_name" : "Khushboo Agency",
    "pending_bill" : 6000,
    "location" : "Puri"
}

# .keys() lagane se loop sirf left side wale naamo par chalega
for k in supplier_profile.keys():
    print(f"Bani hui Key ka naam hai: {k}")


# .values() lagane se loop sirf right side wale data par chalega
for v in supplier_profile.values():
    print(f"Data value: {v}")


# k me aayegi Key, aur v me aayegi uski Value
for k, v in supplier_profile.items():
    print(f"{k} ➡️ {v}")




# MATHEMATICS IN DICTIONARY + LOOPS

# Real-World Business Example
monthly_expenses = {
    "milk_bill": 1200,
    "oats_stock": 800,
    "paneer_supply": 2500
}

total_expense = 0 # Accumulator bahar khada hai

for amount in monthly_expenses.values():
    total_expense += amount # Sirf numbers par loop chal kar plus ho raha hai

print(f"Total Monthly Dietary Expense: {total_expense}rs")



# FILTERING .items()

# Real-World Business Filter Example
vendor_credit = {
    "Khushboo Agency": 4500,
    "Mahadev Company": 6200,
    "Sriram Enterprises": 1200
}

# Hame sirf unhe dhoodhna hai jinka bill 4000 se zyada hai
for supplier, bill in vendor_credit.items():
    if bill > 4000:
        print(f"Priority Payment Alert 🚨: Call {supplier} (Due: {bill}rs)")