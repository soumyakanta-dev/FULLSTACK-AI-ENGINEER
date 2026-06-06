def beard_care_engine(day , product_used):
    print(f"\nGrooming Logs 🛡️ | Day: {day} -> Applied {product_used} for optimal growth and cleanliness.\n")


beard_care_engine("Monday", "Beard Oil")
beard_care_engine("Thursday", "Beard Wash")




def macro_calculator(item, protein, calories = 2000):
    print(f"\nNutritional Logs 🥗 | Target Item: {item} -> Protein: {protein}g | Calories Allocated: {calories}kcal\n")

macro_calculator("Tempeh", 32, 350)
macro_calculator("Amul Buttermilk", 15)