ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
VALID_CHOICES = {ROCK, PAPER, SCISSORS}
def game_rules(choice1, choice2):
    if choice1 == choice2:
        print("It's a tie!")
    elif choice1 == ROCK and choice2 == PAPER:
        print("Paper covers rock, Player 2 wins!")
    elif choice1 == ROCK and choice2 == SCISSORS:
        print("Rock breaks scissors, Player 1 wins!")
    elif choice1 == PAPER and choice2 == ROCK:
        print("Paper covers rock, Player 1 wins!")
    elif choice1 == PAPER and choice2 == SCISSORS:
        print("Scissors cut paper, Player 2 wins!")
    elif choice1 == SCISSORS and choice2 == ROCK:
        print("Rock breaks scissors, Player 2 wins!")
    elif choice1 == SCISSORS and choice2 == PAPER:
        print("Scissors cut paper, Player 1 wins!")
  
while True:   
    choice1 = input("Player 1, enter your choice: ")
    if choice1 not in VALID_CHOICES:
        print("Error: Invalid input. Please enter rock, paper or scissors.")
        continue
    choice2 = input("Player 2, enter your choice: ")
    if choice2 not in VALID_CHOICES:
        print("Error: Invalid input. Please enter rock, paper or scissors.")
        continue

    for i in range(1):
        game_rules(choice1, choice2)

    while True:
        choice = input("Do you want to play again? Enter Y for Yes or N for No: ")
        if choice.lower() == "y":
            break
        elif choice.lower() == "n":
         print("Thank you for playing!")
        exit()  # Exit program
    else:
        exit()  # Exit program