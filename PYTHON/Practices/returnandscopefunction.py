# 1. The Return Aggregator Pipeline

def calculate_shake_calories(oats_cal, milk_cal,  banana_cal):
    return (oats_cal + milk_cal + banana_cal)

breakfast_calories = calculate_shake_calories(190, 150, 100)
print(breakfast_calories)


# 2. The Local Scope Boundary Test

def protein_tracker():
    daily_protein = 140
    print(daily_protein)

# print(daily_protein)  # name 'daily_protein' is not defined


# 3. The Global Access Registry

preferred_buttermilk = "Amul High Protein Buttermilk"

def display_diet_preference():
    print(f"Diet Plan Locked 📝 | Daily Beverage: {preferred_buttermilk}")

display_diet_preference()



# 4. Multi-Layer Arithmetic Return

def apply_business_discount(total_bill, discount_amount):
    return (total_bill - discount_amount)

final_ledger_payment = apply_business_discount(4500, 500)

print(f"Final Ledger Payment : {final_ledger_payment}")



# 5. Global Modification Trap (Conceptual)

stock_count = 50

def update_stock():
    stock_count = 80
    print(stock_count)

update_stock()

print(stock_count)


