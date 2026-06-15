items = ["Amul Buttermilk", "Milky Mist Paneer", "Tempeh"]
prices = [15, 120, 140]

for prdct, qty in zip(items, prices):
    print(f'{prdct} cost is {qty}')