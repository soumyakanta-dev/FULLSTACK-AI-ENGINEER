# # FILE HANDLING

# # with open("filename.txt", "mode") as file:
# #     # Aapka operations area

# with open("supplier_ledger.txt", "w") as file:
#     "Supplier Profile: Khushboo Agency | Pending: 4500rs\n"



# # Step 1: Write mode me file banayi aur pehla data likha
# with open("supplier_ledger.txt", "w") as file:
#     file.write("Supplier Profile: Khushboo Agency | Pending: 4500rs\n")

# # Step 2: Append mode me khol kar doosra data joda
# with open("supplier_ledger.txt", "a") as file:
#     file.write("Supplier Profile: Mahadev Company | Pending: 6200rs\n")

# # Step 3: Read mode me khol kar data nikaala aur screen par dikhaya
# with open("supplier_ledger.txt", "r") as file:
#     content = file.read()  # Poora data is variable me aa gaya
#     print(content)         # Terminal par output dekhne ke liye



# # Real-World Business Input System

# # 1. User se naye supplier ki detail lena
# supplier_name = input("Enter Supplier Name: ")  # Maan lijiye aapne dala: Khushboo Agency
# pending_amount = input("Enter Pending Bill Amount (rs): ") # Maan lijiye aapne dala: 4500

# # 2. Data ko ek clean format me set karna
# new_entry = f"Supplier: {supplier_name} | Balance Due: {pending_amount}rs\n"

# # 3. REAL-WORLD PERSISTENCE: Isko hamesha ke liye hard-disk me save karna
# with open("business_database.txt", "a") as file: # "a" lagaya taaki purana data delete na ho
#     file.write(new_entry)
#     print("✅ System Notification: Ledger Entry Saved Permanently to Hard-Disk!")




#. tell()

with open("security_key.txt", "w") as file:
    file.write("")
    # Abhi hamne 3 characters likhe: N, E, W
    
    position = file.tell()
    print(position)  # Output aayega: 3 (Kyunki cursor 3 characters aage badh chuka hai)


# with open("security_key.txt", "r") as file:
#     first_time = file.read()
#     print(first_time)  # Output: NEW_SECRET_KEY_999
    
#     # Is waqt cursor file ke bilkul END me khada hai!
#     second_time = file.read()
#     print(second_time)  # Output: (Bilkul khali! Kuch print nahi hoga)
    
#     # 🛠️ Safety Switch Tool Action: Cursor ko wapas line ke shuru me bhejo
#     file.seek(0) 
    
#     third_time = file.read()
#     print(third_time)  # Output: NEW_SECRET_KEY_999 (Wapas se read ho gaya!)