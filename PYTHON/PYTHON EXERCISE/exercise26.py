ledger = {"supplier": "Khushboo Agency", "tax_clearance": True}


user_key = input("Enter key to search: ")


print(ledger.get(user_key, "Data Not Found"))