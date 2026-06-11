food_database = []

def options_menu():
    print(f'''
1. Log Meal (Breakfast/Lunch/Dinner)
2. View Today's Nutrition Summary
3. Lock & Save Diary to Disk ''')
    
def data_capture():
    meal_type = input(f"Enter Meal Type (e.g., Breakfast, Shake, Lunch) :- ")
    calorie_count = input(f"Enter Calorie Count for this Meal :- ")
    protein_content = input(f"Enter Protein Content in this Meal :- ")

    if calorie_count.isdigit() == True and protein_content.isdigit() == True:
        if int(calorie_count) >= 0 and int(protein_content) >= 0:
            food_database.append({'Meal Type' : meal_type, 'Calorie Count' : int(calorie_count), 'Protein Content' : int(protein_content)})
        else:
            print(f"Please Enter Actual Value.")

    else:
        print(f'Please Enter Numeric Value for accord to those Input.')


def display_meal():
        total_calorie = 0
        total_protein = 0

        if not food_database:
            print(f"List is Empty now.")
            return
           
        for item in food_database:
            print(f'("Meal Type" : {item["Meal Type"]} | "Calorie Count" : {item["Calorie Count"]} | "Protein Content" : {item["Protein Content"]})\n')

            total_calorie += item['Calorie Count']
            total_protein += item['Protein Content']

        print(f'(Total Calorie - {total_calorie}')
        print(f'(Total Protein - {total_protein}')


def storage_engine():
    with open('diet_history.txt', 'a') as file:
        for item in food_database:
            file.write(f'("Meal Type" : {item["Meal Type"]} | "Calorie Count" : {item["Calorie Count"]} | "Protein Content" : {item["Protein Content"]})\n')
        
        print(f'Data Saved Successfully, Exiting Goodbye......👋')



while True:
    options_menu()
    user_options_choices = input('Enter 1 or 2 or 3 :- ') 

    if user_options_choices == "1":
        data_capture()

    elif user_options_choices == "2":
        display_meal()

    elif user_options_choices == "3":
        storage_engine()
        break

    else:
        print(f'Enter 1 or 2 or 3 for options Menu...')
        continue

