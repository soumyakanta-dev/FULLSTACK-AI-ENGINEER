# TUPLE 

# Fixed data architecture setup
fixed_coordinates = (19.8048, 85.8178) # Puri's Lat-Long
days_of_week = ("Monday", "Tuesday", "Wednesday")

# Tuple Loops & Immutability Test

# for item in tuple_name:

dimensions = (1920, 1080)

# 1. Loop chalana (Read-Only Mode)
for d in dimensions:
    print(d)

# 2. Galti se update karne ki koshish (Crash Test)
# dimensions[0] = 2560  #-> Yeh line chalte hi Python 'TypeError' dega aur code rook jayega.


# Packed Tuple
supplier_info = ("Khushboo Agency", 4500, "Puri")

# Unpacking Process (Bina kisi loop ke, direct assignment)
agency_name, pending_bill, location = supplier_info

# Variables checking
print(agency_name)   # Output: Khushboo Agency
print(pending_bill)  # Output: 4500
print(location)      # Output: Puri

location = ("Puri", 752001)
city, pincode, state = location  # ❌ Triggers ValueError: not enough values to unpack

supplier = ("Khushboo Agency", 4500, "Puri")
name, bill = supplier  # ❌ Triggers ValueError: too many values to unpack

