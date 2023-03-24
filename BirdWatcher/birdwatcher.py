#A bird watcher watches birds every day for four days. 
# Write a program that keeps a running total of the number of birds seen during the four days. 
# The loop should ask for the number of birds seen each day, and when the loop is finished, 
# the program should display the total number birds seen, as well as the average number of birds seen per day.

bird_total = []
days = int
user_birds = int

while True:
    try: # Try to convert user input to an integer
        user_birds = int(input("How many birds did you see today?: "))
    except ValueError:
        print("Error: Please enter a positive number for the number of birds you saw.")
        continue

    if user_birds < 0: # Check if the number is positive
        print("Error: Please enter a positive number for the number of birds you saw.")
        continue
    
    bird_total.append(user_birds) # Add the number of birds to the list
     
    while True:
        days = input("Do you want to enter another day? Enter Y for Yes or N for No: ")
        if days.lower() == "y":
            break
        elif days.lower() == "n":
            print("The total number of birds you saw was", sum(bird_total)) # Print the sum of the list
            print("The average number of birds you saw per day was", sum(bird_total)/len(bird_total)) # Print the average of the list
            input("Press Enter to close the program.") # Pause program
            exit()  # Exit program
        else:
            input("Press Enter to close the program.")
            exit()