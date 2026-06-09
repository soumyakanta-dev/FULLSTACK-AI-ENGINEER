# ==============================================================================
#            CHAPTER 1: COMPLETE CORE SYNTAX CHEATSHEET (CLASS 1 - 22)
# ==============================================================================
import os
import math
import random
import shutil

# --- CLASS 1: Hello World Execution ---
print("System Engine Ready")

# --- CLASS 2: Variables Allocation ---
user_name = "Soumya"
base_cash = 2000
tax_rate = 18.5
is_active = True

# --- CLASS 3: Raw Input Ingestion ---
user_entry = input("Enter Item Name: ")

# --- CLASS 4: Type Casting Execution ---
raw_quantity = input("Enter Quantity: ")
clean_quantity = int(raw_quantity) # Integer target

# --- CLASS 5: Basic Condition Check ---
if clean_quantity > 5:
    print("Bulk Order Triggered")

# --- CLASS 6: Full Choice Logic (If-Elif-Else) ---
if base_cash > 5000:
    print("Premium Tier Account")
elif base_cash >= 10000:
    print("Standard Tier Account")
else:
    print("Basic Tier Account")

# --- CLASS 7: Pre-known Iterations (For Loop) ---
for round_step in range(1, 4):
    print(f"Loop Rotation Number: {round_step}")

# --- CLASS 8: Event Condition Iteration (While Loop) ---
live_counter = 1
while live_counter <= 3:
    print(f"While Loop Execution: {live_counter}")
    live_counter += 1

# --- CLASS 9: Forcing Loop Termination (Break) ---
for target in range(1, 10):
    if target == 4:
        break
    print(f"Break Check Item: {target}")

# --- CLASS 10: Skipping Iteration Segment (Continue) ---
for index in range(1, 5):
    if index == 2:
        continue
    print(f"Continue Check Item: {index}")

# --- CLASS 11: Multi-Dimensional Loops (Nested) ---
for row in range(1, 3):
    for col in range(1, 3):
        print(f"Row coordinate={row} | Col coordinate={col}")

# --- CLASS 12: List Operations (Mutable Array) ---
store_items = ["Paneer", "Buttermilk"]
store_items.append("Tempeh")
store_items[0] = "Oats"

# --- CLASS 13: Tuple Operations (Locked Array) ---
fixed_location = ("Puri", "Odisha")

# --- CLASS 14: Dictionary Operations (Key-Value Setup) ---
vendor_ledger = {"vendor": "Khushboo Agency", "code": 401}
safe_extract_vendor = vendor_ledger.get("vendor", "Not Listed")

# --- CLASS 15: Set Operations (Duplicates Filter) ---
raw_batch_ids = {551, 552, 552, 553} # Output yields only -> {551, 552, 553}

# --- CLASS 16: Basic Block Construction (Functions) ---
def trigger_system_ping():
    print("Core Core Operational Ping Triggered")

trigger_system_ping()

# --- CLASS 17: RAM Variable Pipeline Storage (Return) ---
def evaluate_net_price(amount, tax):
    total_bill = amount + (amount * tax / 100)
    return total_bill

captured_net_invoice = evaluate_net_price(1000, 18)

# --- CLASS 18: Dynamic Unlimited Parameters (*args Tuple) ---
def sum_all_bulk_orders(*args):
    return sum(args)

total_bulk_amount = sum_all_bulk_orders(450, 120, 300, 90)

# --- CLASS 19: Dynamic Named Parameters (**kwargs Dictionary) ---
def register_vendor_configs(**kwargs):
    for settings_key, settings_val in kwargs.items():
        print(f"Configuration Captured -> {settings_key}: {settings_val}")

register_vendor_configs(status="Verified", clearance="Level_1")

# --- CLASS 20: Storage Writing Pipeline (File Context) ---
with open("production_manifest.txt", "a") as file_stream:
    file_stream.write("Log Transaction Entry Processed safely\n")

# --- CLASS 21: Operating System Interface (OS Control) ---
target_vault = "Business_Logs_Vault"
os.makedirs(target_vault, exist_ok=True)
compiled_path = os.path.join(target_vault, "daily_report.txt")

with open(compiled_path, "w") as f:
    f.write("Operational Data Locked\n")

# --- CLASS 22: Precision Boundaries & Random Generator ---
final_ceil_value = math.ceil(840.12)   # Upward -> 841
final_floor_value = math.floor(840.92) # Downward -> 840
standard_round_val = round(840.45)     # Nearest -> 840

random_secure_otp = random.randint(100000, 999999) # 6-Digit Verification
random_lucky_pick = random.choice(store_items)       # Select from list array
# ==============================================================================