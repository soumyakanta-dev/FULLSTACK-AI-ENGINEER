supplier_register = {"Khushboo Agency", "Mahadev Company", "Khushboo Agency"}

print(supplier_register)

supplier_register.add("Sriram Enterprises")

print(supplier_register)


raw_log = ["Puri", "Bhubaneswar", "Puri", "Cuttack", "Bhubaneswar"]

casting_layer = set(raw_log)

for u_city in casting_layer:
    print(f"\nTracked Location ➡️   {u_city}")