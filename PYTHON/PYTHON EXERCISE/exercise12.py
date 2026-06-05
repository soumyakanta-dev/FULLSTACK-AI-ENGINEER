my_diet = {
    "target_kcal" : 2000,
    "diet_type" : "Vegetarian",
    "protein_target_g" : 160
}

for k , v in my_diet.items():
    print(f"\nMy diet's {k} parameter is {v}")


supplier_ledger = {
    "Khushboo Agency": 4500,
    "Mahadev Company": 6200,
    "Sriram Enterprises": 3100
}

total_pending = 0

for x in supplier_ledger.values():
    if x > 0:
        total_pending += x
    else:
        continue


print(f"Total Pending Business Credit: {total_pending}rs")




diet_protein = {
    "Tempeh": 32,
    "Amul Buttermilk": 15,
    "Milky Mist Paneer": 24,
    "Oats Shake": 12
}

for food, protein_quant in diet_protein.items():
    if protein_quant < 20:
        print(f'Low Protein Warning ⚠️: {food} gives only {protein_quant}g')