#There are three seating categories at a stadium. For a softball game, Class A seats cost $30,
#Class B seats cost $20, and Class C seats cost $15. Write a program that asks how many tickets
#for each class of seats were sold, and then displays the amount of income generated from ticket sales.
print("Welcome to the Stadium Ticket Sales Calculator!")


CLASS_A_PRICE = 30
CLASS_B_PRICE = 20
CLASS_C_PRICE = 15

def total_income(class_a, class_b, class_c):
    return class_a * CLASS_A_PRICE + class_b * CLASS_B_PRICE + class_c * CLASS_C_PRICE

while True:
    class_a = input("Enter the number of Class A tickets sold: ")
    try:
        class_a = int(class_a)
        if class_a < 0:
            print("Invalid input. Please enter a positive number.")
            continue
        else:
            break
    except ValueError:  # Handle non-numeric input
        print("Invalid input. Please enter a number.")
        continue

while True:
    class_b = input("Enter the number of Class B tickets sold: ")
    try:
        class_b = int(class_b)
        if class_b < 0:
            print("Invalid input. Please enter a positive number.")
            continue
        else:
            break
    except ValueError:  # Handle non-numeric input
        print("Invalid input. Please enter a number.")
        continue    

while True:
    class_c = input("Enter the number of Class C tickets sold: ")
    try:
        class_c = int(class_a)
        if class_c < 0:
            print("Invalid input. Please enter a positive number.")
            continue
        else:
            break
    except ValueError:  # Handle non-numeric input
        print("Invalid input. Please enter a number.")
        continue
    
print("The total income generated from ticket sales is ${:.2f}.".format(total_income(class_a, class_b, class_c)))
input("Press Enter to close the program.") # Pause program    