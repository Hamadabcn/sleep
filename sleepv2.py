def main():
    # Get the number of hearts from the user
    n = int(input("How many Hearts? "))
    
    # Loop from 0 to n-1
    for i in range(n):
        # Call the sheep function to generate the heart emojis and print the result
        print(sheep(i))

def sheep(n):
    # Generate a string of heart emojis based on the input parameter n
    return "❤️" * n

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function if the script is being run
    main()
