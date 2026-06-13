numbers = [10, 20, 30]

# Lambda ek chota 1-line ka function hota hai (lambda x: x * 2 yani har item ko 2 se multiply karo)
doubled_numbers = list(map(lambda x: x * 2, numbers))

print(doubled_numbers) # Output: [20, 40, 60]





stock_list = [2, 8, 1, 15, 4]

# Filter sirf unhi ko unka pass karega jahan x > 5 sach hoga
premium_stock = list(filter(lambda x: x > 5, stock_list))

print(premium_stock) # Output: [8, 15] (Baki sab filter out ho gaye!)




prices = [100, 200, 300]

# 1. Pehle alag se 2 lines ka function define karo
def add_fifty(x):
    return x + 50

# 2. Phir us function ko map ke andar pass karo
updated_prices = list(map(add_fifty, prices))
print(updated_prices) # Output: [150, 250, 350]




prices = [100, 200, 300]

# Sab kuch sirf 1 single line me bina alag se function banaye khatam!
updated_prices = list(map(lambda x: x + 50, prices))
print(updated_prices) # Output: [150, 250, 350]


# lambda arguments : expression


# Ek lambda function banaya jo do numbers ko plus karta hai
sum_two_numbers = lambda a, b : a + b

# Isko call kiya normal function ki tarah
result = sum_two_numbers(10, 20)
print(result) # Output: 30


raw_prices = [40, 150, 80, 200, 300]

# Step 1: Filter chalaya (Sirf 100 se bade numbers bachenge -> [150, 200, 300])
premium_items = list(filter(lambda x: x > 100, raw_prices))

# Step 2: Bache hue numbers par Map chalaya (Sabme +50 ho gaya -> [200, 250, 350])
final_invoice = list(map(lambda x: x + 50, premium_items))

print(final_invoice) # Output: [200, 250, 350]



from functools import reduce

numbers = [1, 2, 3, 4]

# Lambda yahan do parameters lega (x, y) - x hai accumulation dabba aur y hai agla number
total_sum = reduce(lambda x, y : x + y, numbers)

print(total_sum) # Output: 10 (1+2=3, 3+3=6, 6+4=10)


from functools import reduce

raw_inventory = [5, 20, 50, 8]

# 1. Filter: Sirf [20, 50] bachenge
filtered_items = list(filter(lambda x: x > 10, raw_inventory))

# 2. Map: Dono me 18% tax judega -> [23.6, 59.0]
taxed_items = list(map(lambda x: x * 1.18, filtered_items))

# 3. Reduce: Dono aapas me jud kar ek final single bill banenge -> 82.6
grand_total = reduce(lambda x, y: x + y, taxed_items)

print(round(grand_total, 2)) # Output: 82.6





# Backward Looping (Peeche se Shuru Karo)

numbers = [1, 2, 3, 4, 5, 6]

# len(numbers)-1 se lekar -1 tak peeche ki taraf chalo
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] < 5:
        numbers.pop(i) # Peeche se safely uda diya!

print(numbers) # Output: [5, 6] (Ekdam Perfect!)




# List Comprehension (Naya Saaf Ghar)

numbers = [1, 2, 3, 4, 5, 6]

# Sirf unhi ko rakho jo >= 5 hain
clean_numbers = [item for item in numbers if item >= 5]

print(clean_numbers) # Output: [5, 6]