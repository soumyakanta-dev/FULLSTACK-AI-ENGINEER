# Ek high-protein diet product ki dictionary banate hain label ke sath
# Syntax: product_profile = { "Key" : Value }

product_info = {
    "name": "Amul Buttermilk",
    "price": 30,
    "protein_g": 15,
    "is_vegetarian": True
}

supplier_profile = {
    "agency_name" : "Khushboo Agency",
    "pending_bill" : 4500,
    "location" : "Puri"
}

# ACCESSING THE VALUE
print(supplier_profile["agency_name"])
print(supplier_profile["pending_bill"])


# ADDING AND UPDATING

# dictionary_name [ "Key_Name" ] = New_Value

# 1. Update karna (Bill badal gaya)
supplier_profile["pending_bill"] = 5000  # Ab 4500 mit jayega aur 5000 ho jayega

# 2. Add karna (Naya phone number jodhna)
supplier_profile["phone"] = 9876543210   # Yeh ek naya pair jodh dega


# DELETING AND CHECKING

user_profile = {"username": "soumya_puri", "status": "Active"}

# 1. Safety check karna ki key hai ya nahi
if "status" in user_profile:
    print("Yes, status is in the database!")

# 2. Status key ko permanently delete karna
del user_profile["status"] 
print(user_profile) # Output sirf bacha: {'username': 'soumya_puri'}