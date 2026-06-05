# 1. The Personal Diet Profile

my_diet = {
    "target_kcal" : 2000,
    "diet_type" : "Vegetarian",
    "protein_target_g" : 200
}

print(f'\n{my_diet}')


# 2. Specific Metric Fetcher

user_stats = {
    "name": "Soumya", 
    "age": 23,
    "city": "Puri"
    }

print(f'Name : {user_stats["name"]}')
print(f'City : {user_stats["city"]}')


# 3. Real-Time Price Hiker

item_data = {"name": "Amul Paneer", "price": 120}

item_data["price"] = 140
print(f'{item_data}')


# 4. New Feature Roll-out

app_settings = {"theme": "Dark", "version": 2.1}

app_settings["notifications"] = True
print(f'{app_settings}')


# 5. The Warehouse Stock Clearer

stock = {"item_id": 101, "quantity": 45, "expiry_date": "12-2026"}

if "expiry_date" in stock:
    print(f"Loading for delete this")
    del stock["expiry_date"]
print(f'{stock}')


# 6. Crash-Proof Security Guard

invoice = {"bill_no": 4502, "amount": 1800}

if  "status" in invoice:
    print(f"Status is tracked")
else:
    print(f"Status is Missing!")


# 7. Combined Ledger Overhaul

ledger = {"supplier": "Khushboo Agency", "balance": 5000}

ledger["balance"] = 3500

ledger["payment_mode"] = "UPI"

print(f'{ledger}')


# 8. Safety Delete Routine

employee = {"emp_id": 905, "role": "Manager", "bonus": 500}

if "bonus" in employee:
    del employee["bonus"]

print(f'{employee}')


# 9. Mixed Profile Reader

business = {"brand": "Vyapar", "users": 10000, "is_free": False}

print(f'\nBrand {business["brand"]} has {business["users"]} active users')



# 10. Key Overwrite Challenge

record = {"code": 110, "status": "Pending"}

record["status"] = "Completed"

if record["status"] == "Completed":
    print(f"Task Finished Successfully!")