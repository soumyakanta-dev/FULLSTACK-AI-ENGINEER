supplier_master = {
    "vendor_alpha" : {
        "name" : "Khushboo Agency",
        "pending" : 4500
    },
    "vendor_beta" : {
        "name" : "Mahadev Company", 
        "pending" : 6200
    }
}


print(f'\n{supplier_master['vendor_alpha']["name"]}')
print(f'\n{supplier_master['vendor_beta']["pending"]}')




product_registry = {
    "prod_01": {"item": "Tempeh Block", "stock": 45, "critical_limit": 50},
    "prod_02": {"item": "Amul Buttermilk", "stock": 150, "critical_limit": 100},
    "prod_03": {"item": "Premium Walnuts", "stock": 12, "critical_limit": 20}
}


for product_id, product_details in product_registry.items():
    if product_details["stock"] < product_details["critical_limit"]:
        print(f'\nCRITICAL ALERT 🚨: {product_details["item"]} is running low! Current Stock: {product_details["stock"]} (Limit: {product_details["critical_limit"]})')