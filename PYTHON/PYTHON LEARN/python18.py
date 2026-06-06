# Functions (Part 2 — Return Values & Scope Rules)

# System with PRINT (No memory retention)
def add_print(a, b):
    print(a + b)

result1 = add_print(10, 5)  # Screen par 15 dikhega, par result1 khali (None) rahega.


# System with RETURN (Data is saved in memory)
def add_return(a, b):
    return a + b

# Processing value is caught in a variable outside
final_bill = add_return(10, 5)  
print(f"Final Bill saved in memory: {final_bill}rs")  # Ab hum final_bill ko aage use kar sakte hain


print(result1)
print(final_bill)







# def total_protein_print(oats, milk):
#     print(oats + milk)

# # Function instantly chala aur screen par 40 dikha diya
# my_shake_protein = total_protein_print(30, 10) 

# # Lekin agar aap agle din ka protein isme jodna chaho:

# # new_total = my_shake_protein + 20  

# # ❌ CRASH! TypeError: NoneType and int ko nahi jod sakte.
# # Kyunki my_shake_protein ke andar '40' nahi hai, wo khali (None) hai!


def total_protein_print(oats, milk):
    return (oats + milk)


my_shake_protein = total_protein_print(30, 10)

new_total_protein = my_shake_protein + 20

print(new_total_protein)



# Variable Scope Rules (Global vs Local)


# Global Variable (Sabke liye visible hai)
business_location = "Puri"

def calculate_tax():
    # Local Variable (Sirf is function ke andar zinda hai)
    tax_rate = 0.18
    print(f"Operational City: {business_location}") # Pass (Global variable accessible hai)

calculate_tax()
# print(tax_rate) # ❌ CRASH! NameError: name 'tax_rate' is not defined (Kyuki tax_rate function ke bahar mar chuka hai)