# 1. The Direct Single-Cell Pull

stock_ledger = [
    {"product": "Keyboard", "rate": 450},
    {"product": "Mouse", "rate": 250},
    {"product": "Monitor", "rate": 8500}
]

print(f'\nName of the 3rd product of stock_ledger : {stock_ledger[-1]["product"]}')
print(f'Rate of the 3rd product of stock_ledger : {stock_ledger[2]["rate"]}\n')


# 2. Master Ledger Scanner

invoice_records = [
    {"id": "INV-01", "amount": 1200},
    {"id": "INV-02", "amount": 450},
    {"id": "INV-03", "amount": 3100}
]

for record in invoice_records:
    print(f"\nInvoice Identification: {record['id']} | Total Value: {record['amount']}rs")


# 3. Premium Inventory Audit

warehouse_items = [
    {"item_name": "Oats Pack", "price": 150},
    {"item_name": "Tempeh Block", "price": 160},
    {"item_name": "Premium Walnuts", "price": 650}
]

for item in warehouse_items:
    if item["price"] > 200:
        print(f"\nPremium Item Found: {item['item_name']} costing {item['price']}rs")


# 4. Total Math Value Accumulator

pending_dues = [
    {"client": "Vendor A", "due": 1500},
    {"client": "Vendor B", "due": 4200},
    {"client": "Vendor C", "due": 800}
]

total_due = 0

for costumer in pending_dues:
    if costumer["due"] > 0:
        total_due += costumer["due"]


print(f"\nGrand Total Outstanding Balance: {total_due}rs\n")



# 5. Dynamic Append Mutation

client_registry = [
    {"agency": "Khushboo Agency", "city": "Puri"}
]

client_registry.append({"agency" : "Mahadev Company", "city" :"Bhubaneswar"}) 


print(f'{client_registry}')
