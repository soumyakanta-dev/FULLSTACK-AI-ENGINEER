try:
    # 🔴 RISK ZONE
    # Yahan woh code likho jisme crash hone ka darr hai.
    pass 

except Exception:
    # 🟢 SAFETY LAYER
    # Agar upar wale code me koi bhi galti hui, toh program crash nahi hoga.
    # Python chupchaap is block ke andar aakar yahan ka code chala dega.
    pass


try:
    user_input = input("Sahi number daalo: ") # User ne likha: 50
    clean_number = int(user_input)
    print(f"Bhai tumne perfect number dala: {clean_number}")

except Exception:
    print("Kuch toh gadbad hai daya!")



try:
    user_input = input("Sahi number daalo: ") # User ne galti se likha: Soumya
    clean_number = int(user_input) # ❌ Yahan crash hone laga!
    print(f"Bhai tumne perfect number dala: {clean_number}")

except Exception:
    print("Trap Activated! Aapne number ki jagah text daal diya hai.")
    clean_number = 0 # Backup data set kar diya


while True:
    try:
        raw_input = input("Apna scale size number me daalo: ") # User ne likha: "one"
        clean_size = int(raw_input.strip()) # ❌ Galti hui! Seedhe except me bhaago...
        
        # 🟢 Agar upar koi galti nahi hui, toh hi code is line par aayega:
        print(f"Perfect! Aapka scale size {clean_size} save ho gaya.")
        break # Sahi input milne par loop se bahar nikal jao
        
    except Exception:
        # 🛡️ Galti hone par loop break nahi hoga, yeh warning print karke loop phir ghumega!
        print("Kachra input! Please alphabet nahi, sirf integer number daalo.\n")