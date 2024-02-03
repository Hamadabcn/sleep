def main():
    # Get the number of sheeps from the user
    n = int(input("How many Sheeps? "))
    
    # Iterate over the list of strings returned by the sheep function and print each string
    for s in sheep(n):
        print(s)

def sheep(n):
    # Initialize an empty list to store the strings
    flock = []
    
    # Loop from 0 to n-1
    for i in range(n):
        # Append a string of "🐏" repeated i times to the list
        flock.append("🐏" * i)
    
    # Return the list of strings
    return flock

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function if the script is being run
    main()
