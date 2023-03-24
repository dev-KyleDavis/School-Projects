#Many financial experts advise that, in order to save for retirement, 
# an individual needs at least 70% of their working salary to spend per year in retirement. 
# Write a program that asks the user their current salary and then displays how much they should expect to spend per year in retirement.


def retirement(salary): # Define the function
    return salary * .7 # Return the value

#salary = float(input("Enter your current salary: ")) # Get the salary from the user

while True:
    salary = input("Enter your current salary: ")
    
    try:
        salary = float(salary)  # Convert the input to a float
        if salary <= 0:  # Check if the salary is negative or zero
            print("Invalid input. Please enter a positive number.")
            continue
        else:
            break  # Exit the loop
    except ValueError:  # Handle non-numeric input
        print("Invalid input. Please enter a number.")
        continue
    
print("You should expect to spend ${:.2f} per year in retirement.".format(retirement(salary))) # Display the result   

input("Press Enter to close the program.") # Pause program
exit()  # Exit program 
    