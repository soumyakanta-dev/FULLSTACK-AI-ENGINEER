# Shuruat me list bahar tayaar hai
my_orders = ["Khushboo Agency", "Mahadev Company", "Sriram Enterprises"]

# Loop chalaya - temporary variable ka naam rakha 'supplier'
for supplier in my_orders:
    print(f"Sending Email to: {supplier}")


# Real-world Corporate Example
item_prices = [120, 450, 80, 950]  # List bahar taiyaar hai
total_bill = 0                     # Accumulator bahar taiyaar hai

for price in item_prices:
    total_bill += price            # Har round me math plus ho raha hai

print(f"Final Payable Amount: {total_bill}rs")



# Real-world Example: Finding Expensive Items
stock_prices = [400, 1200, 250, 3000, 850]

for price in stock_prices:
    if price > 1000:  # Sirf unhi ko chunega jo 1000 se bade hain
        print(f"Alert: Premium Product Detected with price {price}rs")