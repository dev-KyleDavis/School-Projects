# Write a program that asks the user to enter a person’s age. 
# The program should display a message indicating whether the person gets free admission, 
# gets a discount, or must pay full price for admission into a theme park.
# If the person is 2-year-old or less, he or she gets free admission.
# If the person is older than 2 years, but younger than 14 years, he or she pays half price.
# If the person is at least 14 years old, but less than 55 years old, he or she pays full price.
# If the person is at least 55 years old, he or she pays half price.

admission_prices = []  #store admission prices

while True:
    # input from user
    admission_age = int(input("Welcome to the Amusement Park Ticket Calculator\nEnter person's age to get pricing info: "))

    # Determine admission price based on age
    if admission_age <= 2:
        admission_price = 0
        message = "gets free admission"
    elif admission_age >= 3 and admission_age <= 14:
        admission_price = 10
        message = "gets a half price discount"
    elif admission_age >= 55:
        admission_price = 20
        message = "gets a senior discount"
    else:
        admission_price = 30
        message = "must pay full price admission"

    # Display admission message and store admission price
    admission_prices.append(admission_price)
    print("This person", message,",the ticket cost will be $",admission_price)

    # Ask user if they want to enter another age group
    while True:
        choice = input("Do you want to add another age group to your party? Enter Y for Yes or N for No: ")
        if choice.lower() == "y":
            break  # loop to enter another age
        elif choice.lower() == "n":
            total_price = sum(admission_prices)  # Calculate total admission price
            print("The total admission cost for your party is $", total_price)
            input("Press Enter to close the program.") # Pause program
            exit()  # Exit program
        else:
            print("Invalid input. Please enter Y or N.")

    
