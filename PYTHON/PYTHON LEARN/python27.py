while True:
    raw_data = input("Enter supply info (Format: VendorName,Quantity): ") # User ne dala: Khushboo,fifty
    
    # Step 1: Comma se tod kar alag karo
    parts = raw_data.split(",")
    
    # Validation Guard: Pehle check karo do parts bane ya nahi
    if len(parts) != 2:
        print("❌ Error: Aapne comma (,) nahi lagaya! Format sahi karo.\n")
        continue
        
    vendor_name = parts[0].strip()
    quantity_str = parts[1].strip()
    
    # Step 2: Dono parts ko alag-alag shield se check karo
    if not vendor_name.isalpha():
        print("❌ Error: Vendor ke naam me sirf alphabets hone chahiye!\n")
        continue
        
    if not quantity_str.isdigit():
        print("❌ Error: Quantity me sirf pure numbers hone chahiye!\n")
        continue
        
    # Agar saare guards clear ho gaye:
    final_quantity = int(quantity_str)
    print(f"✅ Shield Cleared! Registered {final_quantity} items from {vendor_name}.")
    break