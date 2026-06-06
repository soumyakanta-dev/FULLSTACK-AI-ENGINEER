# Machine Engine Setup (Declaration)
def trigger_security_alarm():
    print("ALERT 🚨: Intrusion detected in Node Alpha!")
    print("Action: Firewalls locked down instantly.")

# Machine Execution (Calling the Engine)
trigger_security_alarm()  # Engine active ho jayega aur dono lines print kar dega


# 'supplier' aur 'bill' yahan variables (Parameters) hain
def process_purchase_invoice(supplier, bill):
    print(f"Logging bill from: {supplier}")
    print(f"Amount Added to Ledger: {bill}rs")

# Real execution with real data (Arguments)
process_purchase_invoice("Khushboo Agency", 4500)
process_purchase_invoice("Mahadev Company", 6200)



# Default Parameters (The Infra Fallback Pattern)

# 'location' ka default fallback pipeline set kiya gaya hai
def generate_shipping_bill(agency, location="Puri"):
    print(f"Vendor: {agency} | Logistics Destination: {location}")

# Case A: User ne dono arguments diye
generate_shipping_bill("Khushboo Agency", "Bhubaneswar") 
# Output: Destination ho jayega Bhubaneswar (Overwrite ho gaya)

# Case B: User ne doosra argument miss kar diya
generate_shipping_bill("Mahadev Company") 
# Output: Destination automatically ho jayega Puri (Crash se bach gaya!)