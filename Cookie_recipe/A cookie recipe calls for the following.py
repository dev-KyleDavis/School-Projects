#A cookie recipe calls for the following ingredients:
#•	3 cups of sugar
#•	1.5 cups of butter
#•	4 cups of flour

#The recipe produces 100 cookies with this amount of the ingredients. 
# Write a program that 
# 1) asks the user how many cookies he or she wants to make, and then 
# 2) displays the number of cups of each ingredient needed for the specified number of cookies.


#ammount of sugar needed for 100 cookies
CUPS_SUGAR = 3
#ammount of butter needed for 100 cookies
CUPS_BUTTER = 1.5
#ammount of flour needed for 100 cookies
CUPS_FLOUR = 4
#input from user for how many cookies they want to make
user_cookies = int(input("How many cookies do you want to make?: "))
#variable to hold the number of cookies
number_of_cookies = user_cookies
#constant amount of cookies if using the amount of sugar, butter and flour above for the recipe
RECIPE_COOKIES = 100

#equation to calculate the amount of sugar, butter and flour needed for the amount of cookies the user wants to make
cups_sugar_usage = (number_of_cookies / RECIPE_COOKIES) * CUPS_SUGAR
cups_butter_usage = (number_of_cookies / RECIPE_COOKIES) * CUPS_BUTTER
cups_flour_usage = (number_of_cookies / RECIPE_COOKIES) * CUPS_FLOUR

#display the amount of sugar, butter and flour needed for the amount of cookies the user wants to make
print('To make a total of', user_cookies, "cookies\n", 
      "You need", cups_sugar_usage, "cups of sugar\n", 
      cups_butter_usage, "cups of butter\n" , cups_flour_usage, "cups of flour")

input("Press Enter to close the program.")


