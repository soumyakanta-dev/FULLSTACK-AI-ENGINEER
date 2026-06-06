def calculate_invoice_total(rate, quantity):
    return (rate * quantity)

purchase_ledger_entry = calculate_invoice_total(160,5)

print(f"Ledger Registry Locked 🔒 | Total Outstanding Value: {purchase_ledger_entry}rs")





system_status = "ONLINE"

def node_monitor():
    local_node_id = "Node_Beta"
    print(f"Inside Function: {system_status} | {local_node_id}")

node_monitor()
print(system_status)
# print(local_node_id)