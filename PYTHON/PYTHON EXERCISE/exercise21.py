import os

def smart_system_logger(directory_name, file_name, log_message):

    os.makedirs(directory_name, exist_ok=True)

    perfect_path = os.path.join(directory_name, file_name)

    with open(perfect_path, "a") as file:
        file.write(f"{log_message}\n")

    with open(perfect_path, "r") as file:
        read = file.read()
        print(read)   


smart_system_logger("Daily_Audit_Vault", "system_logs.txt", "Cash counter closed by Soumya with 15000rs balance.")

