try:
    filename = input("Kon si file read karni hai? ")
    with open(filename, "r") as file:
        data = int(file.read().strip())
        print(f"File data ka double: {data * 2}")

except FileNotFoundError:
    # Plan A: Agar file computer me mili hi nahi
    print("Error Code 404: Woh file computer me maujood nahi hai!")

except ValueError:
    # Plan B: Agar file mili, par usme number ki jagah text likha tha
    print("Error Code 500: File toh mili, par uske andar ka data corrupt/text hai!")


# Multi-Error Continuous Loop

while True:
    try:
        filename = input("Apni dynamic bill file ka naam daalo: ") # User ne likha: "bills.txt"
        
        with open(filename, "r") as file:
            raw_data = file.read().strip()
            amount = int(raw_data) # Agar yahan galti hui toh ValueError
            
        print(f"Success! Aapka bill amount ₹{amount} load ho gaya.")
        break # Dono cheez sahi hone par hi loop break hoga
        
    except FileNotFoundError:
        print("❌ Error: Woh file folder me nahi hai! Sahi naam check karke daalo.\n")
        
    except ValueError:
        print("❌ Error: File toh mil gayi, par usme number nahi, galat text likha hai!\n")