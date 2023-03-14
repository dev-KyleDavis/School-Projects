#A cookie recipe calls for the following ingredients:
#•	3 cups of sugar
#•	1.5 cups of butter
#•	4 cups of flour

#The recipe produces 100 cookies with this amount of the ingredients. 
# Write a program that 
# 1) asks the user how many cookies he or she wants to make, and then 
# 2) displays the number of cups of each ingredient needed for the specified number of cookies.

CUPS_SUGAR = 3
CUPS_BUTTER = 1.5
CUPS_FLOUR = 4


RECIPE_COOKIES = 100

cups_sugar_usage = (CUPS_SUGAR / RECIPE_COOKIES) * CUPS_SUGAR
cups_butter_usage = (CUPS_BUTTER / RECIPE_COOKIES) * CUPS_BUTTER
cups_flour_usage = (CUPS_FLOUR / RECIPE_COOKIES) * CUPS_FLOUR


user_cookies = int(input("How many cookies do you want to make?: "))

print('To make' user_cookies "You need", cups_sugar_usage, "cups of sugar\n" + cups_butter_usage, "cups of butter\n" + cups_flour_usage, "cups of flour")
