#Write a program that asks the user for the name of a file. 
#The program should display only the first five lines of the file’s contents. 
#If the file contains less than five lines, it should display the file’s entire contents.

print("Welcome to the File Reader Program\n")

def main():
    user_input = str(input("Enter the Full path of a file: "))
    try:
        user_input = str(user_input)
        file = open(user_input, 'r')
        for i in range(5):
            line = file.readline()
            print("\n",line)
        file.close()
        if file == "":
            print("The file is empty.")
        else:
            print("\n******************************\nThis is the end of the file.")
         
    except FileNotFoundError:
        print("Error: File not found.")
        main()

main()
input("Press Enter to close the program.")