for i in range(1, 11):
    if i == 5:
        print("Break triggered! Stopping the loop.")
        break  # Loop yahi khatam ho jayega, 5 ke baad kuch print nahi hoga
    print(f"Number: {i}")


for i in range(1, 6):
    if i == 3:
        print("Do Not Disturb, Skipping Room 3!")
        continue  # Iske niche wala print Room 3 ke liye nahi chalega
    print(f"Checking Room: {i}")