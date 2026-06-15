# THE match-case ENGINE (Structural Pattern Matching)

command = input("Enter command: ").strip()

match command:
    case "start":
        print("🚀 System starting...")
    case "stop":
        print("🛑 System stopping...")
    case "restart" | "reboot": # Pipe '|' ka matlab hai "OR" (ya toh restart ya reboot)
        print("🔄 System restarting...")
    case _:
        # Underscore '_' default case hota hai (Else block ki tarah)
        print("❌ Unknown command!")



# enumerate()

items = ["Paneer", "Tempeh"]
for index, name in enumerate(items):
    print(f"Index {index} par hai: {name}")


# **`any()` aur `all()` (Boolean Array Checker):**
# any()

print(any(items))


# all()

print(all(items))


# .join()

complete_word = " ".join(items)
print(complete_word)