# 1. Direct Coordinate Pull

system_nodes = {
    "node_alpha": {"ip": "192.168.1.1", "status": "Active"},
    "node_beta": {"ip": "192.168.1.2", "status": "Maintenance"}
}

print(f'\nStatus of "node_beta" : {system_nodes["node_beta"]["status"]}')


# 2. Configuration Mutation

vendor_registry = {
    "v_01": {"name": "Khushboo Agency", "rating": 4.2},
    "v_02": {"name": "Mahadev Company", "rating": 4.5}
}

vendor_registry["v_02"]["rating"] = 4.8

print(f'\n{vendor_registry}\n')


# 3. Real-Time Inventory Scan Loop

diet_inventory = {
    "item_01": {"name": "Tempeh", "stock_packets": 12},
    "item_02": {"name": "Amul Buttermilk", "stock_packets": 85},
    "item_03": {"name": "High Protein Curd", "stock_packets": 8}
}

for name, stock in diet_inventory.items():
    print(f'\nProduct Name : {stock["name"]} | Available Units : {stock["stock_packets"]}')



# 4. Financial Audit Filter

ledger_accounts = {
    "acc_101": {"client": "Supplier A", "pending_amount": 1500},
    "acc_102": {"client": "Supplier B", "pending_amount": 0},
    "acc_103": {"client": "Supplier C", "pending_amount": 5400}
}

for account, details in ledger_accounts.items():
    if details["pending_amount"] > 0:
        print(f'\nAction Required 🚨: {details["client"]} owes {details["pending_amount"]}rs\n')


# 5. Dynamic Field Injection

user_access = {
    "admin_user": {"username": "soumya_ai"}
}

user_access["admin_user"]["clearance_level"] = "Level_5"

print(f'\n{user_access}\n')