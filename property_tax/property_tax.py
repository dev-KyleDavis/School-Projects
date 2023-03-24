# A county collects property taxes on the assessment value of property, 
# which is 70 percent of the property’s actual value. For example, if an acre of land is 
# valued at $10,000, its assessment value is $7,000. The property tax is then 75¢ for each $100 
# of the assessment value. The tax for the acre assessed at $7,000 will be $52.50. 
# Write a program that asks for the actual value of a piece of property and displays the assessment value and property tax.

print("Welcome to the Property Tax Calculator!")

def assessment_value(actual_value):
    return actual_value * .7

def property_tax(_assessment):
    return _assessment * .0075

while True:
    actual_value = (input("Enter the actual value of the property: "))
    try:
        actual_value = float(actual_value)
        if actual_value <= 0:
            print("Invalid input. Please enter a positive number.")
        else:
            break
    except ValueError:  # Handle non-numeric input
        print("Invalid input. Please enter a number.")
        continue

print("\nHere are the results of your tax assesment: \n*******************************************")
print("You reported the actual value of the property was ${:.2f}.".format(actual_value))
print("The assessment value of the property is ${:.2f}.".format(assessment_value(actual_value)))
print("The property tax owed is ${:.2f}.".format(property_tax(assessment_value(actual_value))))

input("Press Enter to close the program.") # Pause program

