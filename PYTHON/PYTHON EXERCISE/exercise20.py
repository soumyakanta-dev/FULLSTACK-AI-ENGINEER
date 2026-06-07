with open("session_log.txt", "w") as log_file:
    log_file.write(f"System Starts from  here")

def generate_session_log(task_name, *args):
    print(f"Executing System Task: {task_name}")
    print("-" * 20)

    with open("session_log.txt", "a") as log_file:
      log_file.write(f"\nTask Name : {task_name}\n")

      for i in args:
        print(f"Executing System Task: {i}")
        log_file.write(f"Details -> {i}\n")

generate_session_log("Daily Settlement", "Cash engine verified", "Ledger updated with 300rs", "System closed securely")

with open("session_log.txt", "r") as file:
    all_log = file.read()
    print(f"{all_log}")


with open("business_directory.txt", "w") as file:
    file.write("=== LOG DIRECTORY START ===\n")

def save_dynamic_transaction(transaction_type, **kwargs):
   print(f"⚙️ Processing: {transaction_type}")

   with open("business_directory.txt", "a") as file:
        file.write(f"\nType: {transaction_type}\n")

        for k, v in kwargs.items():
            print(f"{k.upper()}  : {v}")

            file.write(f"    {k} : {v} \n")


save_dynamic_transaction("Customer Sale", name="Soumya", cash_paid=150)
print("-" * 35)

save_dynamic_transaction("Supplier Purchase", supplier="Khushboo Agency", item="Amul Buttermilk", due=4500)