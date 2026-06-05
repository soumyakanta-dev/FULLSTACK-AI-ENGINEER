# Unique stock categories array setup
# Duplicate values will be dropped automatically
diet_set = {"Oats", "Milk", "Oats", "Banana"}

print(diet_set) 
# Output can be in any order, e.g.: {'Banana', 'Milk', 'Oats'}


# Raw List with duplicates
raw_orders = ["Oats", "Milk", "Oats", "Banana", "Milk"]

# 1. List ko Set me badal kar duplicates udana
clean_catalog = set(raw_orders)

# 2. Set par loop chalana (Read-Only sequence)
for item in clean_catalog:
    print(f"Unique Item: {item}")