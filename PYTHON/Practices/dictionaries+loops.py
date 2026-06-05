# 1. The Stock Label Scanner

inventory_stock ={
    "Oats" : 100,
    "Milk": 250, 
    "Banana": 1
}

for i in inventory_stock.keys():
    print(f"Item Name : {i}")


# 2. The Bill Tracker Loop

purchase_ledger = {
    "Khushboo Agency": 1500, 
    "Mahadev Company": 4200, 
    "Sriram Enterprises": 850
    }

for k, v in purchase_ledger.items():
    print(f"Supplier Name: {k} | Pending Amount: {v}rs")


# 3. Pure Math Value Aggregator

product_rates = {
    "Tempeh": 160, 
    "Buttermilk": 15, 
    "Paneer": 110
    }

total_rates = 0

for v in product_rates.values():
    if v > 0:
        total_rates += v
    else:
        continue
print(f"Final Total : {total_rates}")


# 4. VIP Supplier Locator

suppliers = {
    "Khushboo Agency": 4500, 
    "Mahadev Company": 8200, 
    "Narayan Enterprises": 3100
    }

for k, v in suppliers.items():
    if v > 5000:
        print(f"VIP Supplier : {k}")


# 5. Out of Stock Alert

warehouse_stock = {
    "Keyboard": 45, 
    "Mouse": 0, 
    "Monitor": 12, 
    "CPU": 0
    }

for k, v in warehouse_stock.items():
    if v == 0:
        print(f"Alert! {k} is totally out of stock!")


# 6. Dynamic Value Hiker (Inflation Run)

menu_rates = {
    "Oats": 50, 
    "Milk": 30, 
    "Banana": 40
    }

for k, v in menu_rates.items():
    v += 10
    print(f"Updated price of {k}: {v}rs")


# 7. Character Key Counter (Micro-Logic)

user_cities = {
    "Soumya": "Puri", 
    "Amit": "Bhubaneswar", 
    "Raj": "Cuttack"
    }

for k in user_cities.keys():
    print(f"The name {k} has {len(k)} characters.")


# 8. Cheap Item Filter

items_price = {
    "Chia Seeds": 120, 
    "Dates": 350, 
    "Figs": 450, 
    "Oats": 60
    }

for k, v in items_price.items():
    if v < 150:
        print(f"Product {k} ----> {v}rs")


# 9. Double Accumulator Challenge (Business Logic)

order_sheet = {
    "Order 1": 1200, 
    "Order 2": 450, 
    "Order 3": 2500, 
    "Order 4": 800
    }

high_volume_total = 0
low_volume_total = 0

for v in order_sheet.values():
    if v >= 1000:
        high_volume_total += v
    else:
        low_volume_total += v

print(f"high_volume_total : {high_volume_total}")
print(f"low_volume_total : {low_volume_total}")


# 10. Key Verification Pipeline

required_keys = ["agency_name", "pending_bill", "rating"]

current_supplier = {
    "agency_name": "Khushboo Agency", 
    "pending_bill": 4500
    }

for i in required_keys:
    if i in current_supplier:
        print(f"{i} is verified.")
    else:
        print(f"{i} is missing from database!")