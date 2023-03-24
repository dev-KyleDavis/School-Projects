# Write a program that calculates the amount of money a person would earn over a period, 
# if his or her salary increased by one dollar each day. The program should ask the 
# user for the number of days. Display a table showing what the salary was for each 
# day, starting at one dollar for the first day, two dollars for the second day 
# (total of three dollars for the two days), three dollars for the third day 
# (total of six dollars for the three days), and so on, and then show the total 
# pay at the end of the period. The output should be displayed in a dollar amount.

dollar = 0
dollar_total = []
increments = 0
days = []
while True:
    try:
        days = int(input("How many days do you want to calculate?: "))
        if days <= 0:
            print("Error: Please enter a positive number for the number of days you want to calculate.")
            continue
    except ValueError:
        print("Error: Please enter a positive number for the number of days you want to calculate.")
        continue
    
    for i in range(days):
        increments += 1
        dollar += 1
        dollar_total.append(dollar)
        print("Day", increments, ":", sum(dollar_total))
    
    play_again = input("Do you want to calculate again? Enter Y for Yes or N for No: ")
    if play_again.lower() == "y":
        continue
    if play_again.lower() == "n":
        input("Press Enter to close the program.")
        exit()
    else:
        input("Press Enter to close the program.")
        exit()      
