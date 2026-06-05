protein_foods = ["Tempeh", "Amul Buttermilk", "Milky Mist Paneer"]

for i in protein_foods:
    print(f"Today I will consume: {i}")



purchase_bills = [1500, 4200, 850, 2300]

total_bills = 0

for bills in purchase_bills:
    if bills > 0:
        total_bills += bills
    else:
        print(f"Invalid.")
print(f"Total Purchase Investment : {total_bills}")



order_quantities = [45, 120, 8, 250, 65, 310]

for i in order_quantities:
    if i >= 100:
        print(f"High volume stock detected: {i}")
