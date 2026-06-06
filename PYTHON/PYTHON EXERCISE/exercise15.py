diet_basket = [
    {
        "item" : "Tempeh",
        "protein" : 32
    },
    {
        "item" : "Amul Buttermilk",
        "protein" : 15
    }
]

print(f'2nd value of diet_basket : {diet_basket[1]["item"]}')
print(f'2nd value of diet_basket : {diet_basket[1]["protein"]}')


supplier_database = [
    {"name": "Khushboo Agency", "bill": 1500},
    {"name": "Mahadev Company", "bill": 5200},
    {"name": "Sriram Enterprises", "bill": 850}
]

for i in supplier_database:
    if i["bill"] > 1000:
        print(f'Alert 🚨: {i["name"]} has a major pending bill of {i["bill"]}rs')