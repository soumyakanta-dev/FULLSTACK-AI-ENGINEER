# SAFE DICTIONARY AUDITING (.get() DEPTH ANALYSIS)

vendor_data = {"vendor": "Khushboo Agency", "code": 401} #

print(vendor_data.get('status', 'Not Verified'))



# Master store ledger
store_inventory = {"Paneer": 50, "Buttermilk": 100}

def update_stock(product, new_quantity):
    # Check karo ki kya product pehle se ledger me hai 
    current_stock = store_inventory.get(product, None) # Fallback is None
    
    if current_stock is None:
        print(f"🆕 ALERT: {product} ek naya item hai! Creating record.")
        store_inventory[product] = new_quantity
    else:
        print(f"🔄 UPDATE: {product} pehle se hai. Adding fresh quantity.")
        store_inventory[product] += new_quantity

# --- RUNTIME CRASH TEST ---
update_stock("Tempeh", 30)     # Output: 🆕 ALERT: Naya item record banega.
update_stock("Buttermilk", 20) # Output: 🔄 UPDATE: Purane stock me +20 ho jayega (120).

print(store_inventory)



