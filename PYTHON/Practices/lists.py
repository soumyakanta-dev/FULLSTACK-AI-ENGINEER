# 1. The Basic Grocery Bucket

my_breakfast = ['Oats', 'Milk' , 'Banana']
print(f'\n{my_breakfast}')


# 2. Target Value Fetcher

prices = [150, 240, 560, 890]
print(f"\nList's Second element is : {prices[1]}")
print(f"\nList's Forth element is : {prices[3]}")


# 3. Reverse Indexing Challenge

brands = ["Amul", "Milky Mist", "Quaker"]
print(f"\nList's last element is : {brands[-1]}")
print(f"\nList's first element is : {brands[-3]}")


# 4. Vendor Addition Flow

vendors = ["Brahmam Agency", "Mahadev Company"]
vendors.append("Sriram Enterprises")
print(f"\n{vendors}")


# 5. VIP Seat Assignment

queue = ["Token 1", "Token 3", "Token 4"]
queue.insert(1, "Token 2")
print(f"\n{queue}")


# 6. The Inventory Stock Out

products = ["Keyboard", "Mouse", "Monitor", "CPU"]
products.pop(2)
print(f"\n{products}")


# 7. The Slice Box

numbers = [10, 20, 30, 40, 50, 60]

new_numbers = numbers[2:5]
print(f"\n{new_numbers}")


# 8. Dynamic Append from User Input

user_skills = []

user_enter_skills = input("Enter your skills :-   ")

user_skills.append(user_enter_skills)

print(f"\n{user_skills}")



# 9. Edge To Edge Slice

items = ["A", "B", "C", "D"]
new_items = items[:2]
print(f"\n{new_items}")


# 10. Combined Mutation Drive

data = [100, 300]
data.insert(1, 200)
data.append(400)

print(f"\n{data}")