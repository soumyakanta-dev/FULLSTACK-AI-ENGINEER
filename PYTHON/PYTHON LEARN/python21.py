# CLASS 21: THE OPERATING SYSTEM AUTOMATION ENGINE (os)

# 1. Directory Structure Navigation (Kahan Khade Hain?)

import os

# current_folder = os.getcwd()
# print(f"\n{current_folder}\n")



# # 2. Automated Folder Creation (Naya Folder Banana)


# folder_name = "PYTHON"

# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
#     print(f"📁 Status: Fresh folder '{folder_name}' successfully created!")
# else:
#     print(f"⚠️ Alert: Folder '{folder_name}' already exists. Skipping creation.")


# # 3. Smart Path Joining (The Slash / vs \ Trap)

# folder = "PYTHON"
# file = "june_cash_ledger.txt"

# perfectpath = os.path.join(folder, file)

# print(f"Engineered safe path: {perfectpath}")

# with open(perfectpath, "w") as f:
#     f.write("Total Cash Collection for June: 45000 rs\n")
# print("💾 Data locked inside the newly created sub-folder file!")



python = os.listdir("PYTHON ")
print(python)



