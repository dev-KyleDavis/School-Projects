import random

def main():
    file_path = r"C:\Users\kyled6\OneDrive - kochind.com\Desktop\School Work\Fund of Programming\Module 3\random.txt"
    try:
        user_input = int(input("Enter how many random numbers you want to generate: "))
        if user_input < 1:
            print("Error: Invalid input. Please enter a number greater than 0.")
            main()
        else:
            with open(file_path, "w") as file:
                for i in range(user_input):
                    file.write(str(random.randint(1,1000)) + "\n")
                print("The file has been created.")

            read_file = input("Do you want to read the file? (y/n): ")
            if read_file.lower() == "y":
                with open(file_path, "r") as file:
                    print(file.read())
    except ValueError:
        print("Error: Invalid input. Please enter a number greater than 0.")
        main()

if __name__ == "__main__":
    main()
    input("Press Enter to close the program.")
