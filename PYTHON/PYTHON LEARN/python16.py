# Master Configuration Registry
inventory_config = {
    "Oats": {
        "brand": "Quaker",
        "stock": 50,
        "price_per_unit": 180
    },
    "Buttermilk": {
        "brand": "Amul",
        "stock": 120,
        "price_per_unit": 20
    }
}

print(inventory_config["Buttermilk"])
print(inventory_config["Buttermilk"]["stock"])


# Stock update operation logic
inventory_config["Oats"]["stock"] = 65  # Existing value updated

# New sub-attribute injection logic
inventory_config["Oats"]["expiry_days"] = 90  # New pair injected dynamically



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

# System configurations loop engine
for vendor_id, vendor_data in supplier_master.items():
    # vendor_id = "vendor_alpha"
    # vendor_data = {"name": "Khushboo Agency", "pending": 4500}
    
    print(f"System ID: {vendor_id} | Corporate Title: {vendor_data['name']}")