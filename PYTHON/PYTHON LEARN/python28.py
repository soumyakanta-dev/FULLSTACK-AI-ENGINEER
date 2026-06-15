# THE zip() ENGINE (Parallel Processing)

products = ["Paneer", "Buttermilk", "Tempeh"]
stock_levels = [50, 120, 30]

for item, qty in zip(products, stock_levels):
    print(f'Product: {item} | Stock: {qty}')