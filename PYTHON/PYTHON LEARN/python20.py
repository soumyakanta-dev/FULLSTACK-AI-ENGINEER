# DYNAMIC PACKETS (*args & kwargs)


# 1. *args (Non-Keyword / Unlimited Values Pitara)


def calculate_counter_total(*args):
    print(f"📦 Backend Bundle Received (Tuple): {args}")

    total = 0

    for price in args:
        if price >= 0:
            total += price
        else:
            continue
    return total


bill1 = calculate_counter_total(54, 56)
print(f"💰 Bill 1 Total: {bill1}rs\n")

bill2 = calculate_counter_total(100, 200, 300, 400)
print(f"💰 Bill 2 Total: {bill2}rs\n")


# 2. kwargs (Keyword / Label-Value Pitara)

# ** ka matlab hai: Labeled inputs ko Dictionary bana kar collect karo
def create_supplier_profile(**kwargs):
    print(f"🗂️ Backend Dictionary Created: {kwargs}")
    
    # Hum directly dictionary ke keys ko access kar sakte hain
    if "name" in kwargs:
        print(f"Active Supplier: {kwargs['name']}")
    if "pending_due" in kwargs:
        print(f"⚠️ Alert: Pending Balance is {kwargs['pending_due']}rs")

# Case A: Khushboo Agency ka basic data aaya
create_supplier_profile(name="Khushboo Agency", city="Puri")
print("-" * 40)

# Case B: Milky Mist ka advanced details aaya
create_supplier_profile(name="Milky Mist", state="Odisha", pending_due=6200, rating=5)