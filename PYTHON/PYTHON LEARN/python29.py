# DICTIONARY COMPREHENSION (Inline Dict Generator)


items_list = ["Paneer", "Buttermilk", "Tempeh"]


stock_ledger = {product: 0 for product in items_list}
print(stock_ledger)

