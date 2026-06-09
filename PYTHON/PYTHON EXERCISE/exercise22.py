import math
import random
import os

def process_perfect_bill(base_price, tax_percentage):
    total = base_price + (base_price * tax_percentage / 100)
    
    return math.ceil(total)



realBill = process_perfect_bill(123, 10)

print(realBill)


def generate_supplier_ticket(supplier_name, total_amount):
    randNum = random.randint(1000, 9999)

    with open("all_invoices.txt", "a") as f:
        f.write(f"Invoice #ID-{randNum} | Supplier: {supplier_name} | Amount: {total_amount} rs\n")

    print(f"Invoice #ID-{randNum} | Supplier: {supplier_name} | Amount: {total_amount} rs\n")

generate_supplier_ticket("Sridhar Sahoo Store", 10000000000)

current = os.getcwd()
path = os.path.join(current, "all_invoices.txt")

if os.path.exists(path):
    os.remove(path)
else:
    print(f"we dont have the access")

