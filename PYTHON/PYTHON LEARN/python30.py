# THE try-except-else-finally METRIC


try:
    user_input = input("Enter quantity: ")
    quantity = int(user_input) # Agar user ne text dala toh crash!

except ValueError:
    print("❌ Error: Aapne galat number dala!")

else:
    print(f"✅ Success: Quantity {quantity} safely converted!")

finally:
    print("🔒 System Security: Memory space cleaned up successfully.")