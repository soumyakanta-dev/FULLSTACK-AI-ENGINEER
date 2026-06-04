# Ek high-protein plant-based product aur dairy brands ki list banate hain
my_favorites = ["Tempeh", "Amul Buttermilk", "Milky Mist Paneer"]

# List me alag-alag data types bhi ek sath aa sakte hain (Mixed List)
my_business_data = ["Mahadev Agency", 101, 4500.50, True] 
# (Supplier Name, Order ID, Bill Amount, Payment Done Status)

#INDEXING IN LISTS

print(my_favorites[0])

# NEGATIVE INDEXING
print(my_favorites[-1])


# list_name . method_name ( jo kaam karna hai )

# Ek khali jhola (list) banaya
my_cart = [] 

# 1. Append se item joda
my_cart.append("Amul Buttermilk") # Cart ho gayi: ["Amul Buttermilk"]

# 2. Insert se index 0 par naya item baithaya
my_cart.insert(0, "Tempeh") # Cart ho gayi: ["Tempeh", "Amul Buttermilk"]

# 3. Pop se index 1 wala item uda diya
my_cart.pop(1) # Cart ho gayi: ["Tempeh"]


# SLICING IN LISTS

brands = ["Amul", "Milky Mist", "Quaker", "Nestle", "Britannia"]
# Index:    0          1           2         3          4

# Mujhe index 1 se lekar index 3 tak ke items chahiye
my_slice = brands[1:4] # Yeh chalega index 1, 2, aur 3 tak (4 include nahi hoga)
print(my_slice)



