# English: Using a for loop to repeat code 5 times
# Hinglish: for loop ka use karke code ko 5 baar repeat karna

for i in range(1, 6):
    print(f"Round Number: {i}")

name = "soumya"

# Computer se puch rahe hain: Kya 'a' letter name ke andar hai?
print("a" in name)  # Output: True
print("z" in name)  # Output: False (Kyunki 'z' aapke naam me nahi hai)


user_input = input("Enter traffic color: ").lower() # Agar user ne 'g' dala

# Check karega: Kya user ka input is list ['green', 'g'] ke andar aata hai?
if user_input in ["green", "g"]:
    print("GO.")
else:
    print("Invalid.")