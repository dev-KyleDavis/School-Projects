user_calories = int; total_calories = int; calories_breakfast = []; calories_lunch = []; calories_dinner = []; 
over = user_calories; under = user_calories
def calories(user_calories, total_calories):
    if total_calories > user_calories:
        print("You ate", total_calories, "calories today.\nwhich is", total_calories - user_calories, 
          "calories over your daily limit.")
    elif total_calories < user_calories:
        print("You ate", total_calories, "calories today.\nwhich is", user_calories - total_calories, 
          "calories under your daily limit.")
    else:
        print("You ate", total_calories, "calories today.\nyou have", user_calories - total_calories, 
          "calories left of your daily limit.")
while True:
    try: # Try to convert user input to an integer
        user_calories = int(input("How many calories should you eat in a day?: "))
        calories_breakfast = int(input("How many calories did you eat for breakfast?: "))
        calories_lunch = int(input("How many calories did you eat for lunch?: "))
        calories_dinner = int(input("How many calories did you eat for dinner?: "))
    # If the user enters a non-integer value, display an error message and restart the loop
    except ValueError:
        print("Error: Please enter a positive number for the number of calories you should eat.")
        continue

    # Add the number of birds to the list
    total_calories = (calories_breakfast + calories_lunch + calories_dinner)
    
    for i in range(1):
        calories(user_calories, total_calories)
    
    ask_again = input("Do you want to calculate again? Enter Y for Yes or N for No: ")
    if ask_again.lower() == "y":
        continue
    else:
        input("Press Enter to close the program.") # Pause program
        exit()


