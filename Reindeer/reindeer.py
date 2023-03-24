# Define the reindeer names and their corresponding numbers
reindeer_names = {1: "Dasher", 2: "Dancer", 3: "Prancer", 4: "Vixen", 5: "Comet", 6: "Cupid", 7: "Donner", 8: "Blitzen"}

while True:
    # Take input from user
    reindeer_number = int(input("Welcome to Reindeer Roulette! Pick a number between 1 and 8: "))

    # Check if input is within range of 1-8
    if reindeer_number < 1 or reindeer_number > 8:
        print("Error: Invalid input. Please enter a number between 1 and 8.")
    else:
        # Get the corresponding reindeer name using the dictionary
        reindeer_name = reindeer_names[reindeer_number]
        print("Congratulations! You picked", reindeer_name, "!")
        
        # Ask user if they want to pick again
        while True:
            choice = input("Do you want to pick again? Enter Y for Yes or N for No: ")
            if choice.lower() == "y":
                break  # Break out of inner loop and pick again
            elif choice.lower() == "n":
                print("Thank you for playing Reindeer Roulette!")
                exit()  # Exit program
            else:
                print("Invalid input. Please enter Y or N.")
