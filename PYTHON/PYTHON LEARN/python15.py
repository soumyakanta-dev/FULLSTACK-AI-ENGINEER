# LISTS OF DICTIONARIES (NESTED CONTAINERS)



# Ek badi master list jisme saare suppliers ka profile lock hai
business_database = [
    {
        "agency_name": "Khushboo Agency",
        "pending_bill": 4500,
        "location": "Puri"
    },
    {
        "agency_name": "Mahadev Company",
        "pending_bill": 6200,
        "location": "Bhubaneswar"
    }
]


business_database = [
    {"agency_name": "Khushboo Agency", "pending_bill": 4500},
    {"agency_name": "Mahadev Company", "pending_bill": 6200}
]

# Loop chalane par har round me ek poori dictionary 'vendor' variable me aayegi
for vendor in business_database:
    # Ab hum 'vendor' dictionary se direct keys pull kar sakte hain
    print(f"Supplier: {vendor['agency_name']} owes {vendor['pending_bill']}rs")