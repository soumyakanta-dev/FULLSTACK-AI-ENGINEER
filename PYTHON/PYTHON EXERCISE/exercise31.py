role = input('Enter your role :- ').lower()

match role:
    case 'admin':
        print(f"Full Access granted")
    case 'supplier':
        print(f'Inventory Access granted')
    case _:
        print(f"Access Denied")