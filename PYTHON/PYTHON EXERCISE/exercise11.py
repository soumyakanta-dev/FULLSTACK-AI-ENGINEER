supplier_profile = {
    "agency_name" : "Khushboo Agency",
    "pending_bill" : 4500,
    "location" : "Puri"
}

print(f'\n{supplier_profile}\n')


print(f'\nSupplier : {supplier_profile["agency_name"]}')
print(f'Due Amount : {supplier_profile["pending_bill"]}')

supplier_profile["pending_bill"] = 6000
supplier_profile["rating"] = "5-Star"

print(f"\n{supplier_profile}")

if "location" in supplier_profile:
    print(f"Yes 'location' is present.")
    del supplier_profile["location"]

print(f'\n{supplier_profile}')
