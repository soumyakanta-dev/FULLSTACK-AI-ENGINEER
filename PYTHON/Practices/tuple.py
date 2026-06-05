# 1. The Fixed Brand Vault

favorite_brands = ("Amul", "Milky Mist", "Danone")
print(f"{favorite_brands}")


# 2. Target Index Puller

macro_targets = (2000, 160, 50, 40)

print(f"{macro_targets[-1]}")
print(f"{macro_targets[1]}")


# 3. Complete Registry Scan

operating_days = ("Monday", "Wednesday", "Friday")

for day_name in operating_days:
    print(f"Business open on: {day_name}")



# 4. Safe Conditional Search

allowed_modes = ("UPI", "Cash", "NetBanking")

for modes in allowed_modes:
    if modes == "Cash":
        print(f"Cash system detected!")



# 5. Unpacking Pipeline

location_point = ("Puri", 752001)

city , pincode = location_point

print(f"City Name is {city} and code is {pincode}")

