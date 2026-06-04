supplier_names = ["Sriram Enterprises", "Mahadev Agency", "Brahmam Store"]

stock_quantities = [45, 63, 89]

# print(f"{supplier_names}")

# print(f"{stock_quantities}")

print(f"\nSupplier Name : {supplier_names[1]}")
print(f"Its Stock Quantity: {stock_quantities[1]}\n")

print(f'\nLast Supplier: {supplier_names[-1]}')
print(f'First Supplier by negative index: {supplier_names[-3]}\n')


suppliers = ["Sriram Enterprises", "Brahmam Store"]
suppliers.append("Narayan Agency")
suppliers.insert(1, "Mahadev Company")
suppliers.pop(2)

print(suppliers)

my_stock = ["Oats", "Milk", "Banana", "Chia Seeds", "Dates", "Figs"]
# Index:            0          1           2                 3                4           5

new_stock = my_stock[1:4]
print(f'\n{new_stock}')


