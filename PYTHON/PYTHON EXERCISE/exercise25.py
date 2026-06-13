stock = [5, 12, 3, 20, 8]

even_stock = list(filter(lambda x : x % 2 == 0, stock))

map_stock = list(map(lambda x : x * 3, even_stock))


print(map_stock)



quantities = [12, 0, 4, 0, 45, 8, 0]

for i in range(len(quantities)-1, -1, -1):
    if quantities[i] == 0:
        quantities.pop(i)
print(quantities)


clean_quantities = [item for item in quantities if item != 0]
print(clean_quantities)