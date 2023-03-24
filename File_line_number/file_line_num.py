#Write a program that asks the user for the name of a file. 
#The program should display the contents of the file with each line preceded with the word 
#“line” and a line number followed by a colon. The line numbering should start at 1.

#Sample output:
#line 1: contents of line 1
#line 2: contents of line 2
#Etc. for as many lines are in the file.

print("Welcome to the Line Numbers Program\n")

def main():
    user_input = str(input("Enter the Full path of a file: "))
    try:
         user_input = str(user_input)
         user_input = open(user_input, 'r')
         if user_input == "":
             print("The file is empty.")
         else:
             for i, line in enumerate(user_input):
                print("line", i+1, ":", line)
    except FileNotFoundError:
        print("Error: File not found.")
        main()

main()
input("Press Enter to close the program.")
