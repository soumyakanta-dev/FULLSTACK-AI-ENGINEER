with open("supplier_ledger.txt", "w") as file:
    file.write("Supplier Profile: Khushboo Agency | Pending: 4500rs\n")
with open("supplier_ledger.txt", "a") as file:
    file.write("Supplier Profile: Mahadev Company | Pending: 6200rs\n")
with open("supplier_ledger.txt", "r") as file:
    content = file.read()
    print(content)

