# 1. Clean Diet Vault

unique_diet_items = {"Oats", "Milk", "Oats", "Tempeh", "Milk"}

print(f"\n{unique_diet_items}")


# 2. Dynamic Component Injection

active_vendors = {"Khushboo Agency", "Mahadev Company"}

active_vendors.add("Narayan Enterprises")
active_vendors.remove("Mahadev Company")

print(f"\n{active_vendors}")



# 3. The Bulk Filter Pipeline

raw_orders = [1500, 4200, 1500, 850, 4200]

new_orders = set(raw_orders)

print(f"\n{new_orders}")


# 4. Registry Scanner Execution

secured_zones = {"Warehouse A", "Office", "Gate 1"}

for i in secured_zones:
    print(f"\nSecurity Checkpoint: {i}")


# 5. Search Guard verification

verified_pincodes = {752001, 751001, 753001}

for i in verified_pincodes:
    if i == 752001:
        print(f"\nPrimary Business Location Pincode Detected!")