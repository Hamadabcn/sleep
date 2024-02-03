def main():
    # Get the number of sheeps from the user
    n = int(input("How many Sheeps? "))
    
    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Print a row of sheep emojis based on the current loop index
        print("🐏" * i)

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function if the script is being run
    main()
