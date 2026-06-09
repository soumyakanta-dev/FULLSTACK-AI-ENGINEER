# # 1. Automatic Daily Supplier Ingestion Folder

import os

current_dir = os.getcwd()

# def initiate_business_vault(folder_name):

#     if os.path.exists(folder_name):
#         print(f"\n{folder_name} already exists, bypass encryption.\n")
#     else:
#         os.mkdir(folder_name)
#         print(f"\n{folder_name} Created Successfully!.\n")

# initiate_business_vault("folder_name")


# # 2. The Safe Path Log Ingestor

# def secure_file_dump(directory, filename, data_string):

#     perfect_path = os.path.join(directory, filename)

#     os.makedirs(directory, exist_ok=True)

#     with open(perfect_path, "a") as f:
#         f.write(f"{data_string}\n")

# secure_file_dump("Khushboo_Agency_Vault", "bills.txt", "Amul High Protein Buttermilk - 200 Packs Received")


# # 3. Live Directory Inspector (Audit System)

# def audit_storage_folder(folder_path):

#     files_list = os.listdir(folder_path)

#     with open("files_list.txt", "a") as f:
#         f.write(f"Files List in {folder_path} are :- \n")

#         for file in files_list:
#             print(f"{file}")
#             f.write(f"{file}\n")

# audit_storage_folder("PYTHON")


# # 4. The Folder Auditor (Files Scan Matrix)

# def audit_my_warehouse(folder_name):
    
#     if not os.path.exists(folder_name):
#         print(f"❌ Audit Cancelled: Target Folder doesn't exist.")
#     else:
#         lists = os.listdir(folder_name)
#         with open("files_list.txt", "a") as f:
#             f.write(f"List of files in {folder_name }are :- ")

#             for i in lists:
#                 print(f"\n{i}")
#                 f.write(f"{i}")

# audit_my_warehouse("PYTHON")



# # 5. The Bulk Ledger Backup System

# def bulk_ledger_backup(vault_name, file_list):

#     os.makedirs(vault_name, exist_ok=True)

#     for item in file_list:
#         perfect_path = os.path.join(vault_name, item)

#         with open(perfect_path, "w") as f:
#             f.write(f'Backup Logs Secured\n')

# bulk_ledger_backup("vault_name", ["morning.txt", "evening.txt"])


# 6. The Intelligent Janitor (Old Logs Deleter)

def system_cleaner(folder_name, file_to_delete):

    perfectPath = os.path.join(folder_name, file_to_delete)
    

    if os.path.exists(perfectPath):
        os.remove(perfectPath)
        print(f'"{perfectPath}" Deleted Successfully')
    else:
        print(f'⚠️ File not found. Clean operation bypassed.')

system_cleaner("vault_name", "morning.txt")
system_cleaner("vault_name", "evening.txt")
system_cleaner("PYTHON", "june_cash_ledger.txt")
system_cleaner("Khushboo_Agency_Vault", "bills.txt")
system_cleaner(current_dir, "files_list.txt")
system_cleaner(current_dir, "approved_suppliers.txt")
system_cleaner(current_dir, "business_directory.txt")
system_cleaner(current_dir, "cash_ledger.txt")
system_cleaner(current_dir, "daily_expenses.txt")
system_cleaner(current_dir, "inventory_log.txt")
system_cleaner(current_dir, "security_key.txt")
system_cleaner(current_dir, "session_log.txt")
system_cleaner(current_dir, "system_logs.txt")
system_cleaner(current_dir, "supplier_ledger.txt")



# 7. Folder termination permanently

import shutil

def folder_terminator(sub_folder):


    perfectpath = os.path.join(current_dir, sub_folder)

    if os.path.exists(perfectpath):
        os.rmdir(perfectpath)
        print(f"Path termination successfully")
    else:
        print(f'⚠️ Path not found. Clean operation bypassed.')

folder_terminator("Daily_Audit_Vault")
