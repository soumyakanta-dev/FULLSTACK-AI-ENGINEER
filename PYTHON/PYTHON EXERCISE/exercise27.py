while True:
    user_key = input('enter product description format (ProductName-Price) :- ')
    
    parts = user_key.split('-')

    if len(parts) != 2:
        print(f'Format is wrong')
        continue

    product_name = parts[0].strip()
    quantity_name = parts[1].strip()

    if not product_name.isalpha():
        print(f'Product nmae should be only in alphabet')
        continue

    if not quantity_name.isdigit():
        print(f'Quantity name should be in numeric')
        continue

    print(f'{product_name} - {int(quantity_name)}')
    break