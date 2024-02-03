def main():
    # Get the number of sheeps from the user
    n = int(input("How many Sheeps? "))
    
    # Iterate over the values yielded by the sheep generator function and print each value
    for s in sheep(n):
        print(s)


def sheep(n):
    # Generator function using yield to produce values on the fly
    for i in range(1, n + 1):
        # Generate a string with equal lengths on both sides of the pyramid
        yield " " * (n - i) + "🐏" * (2 * i - 1) + " " * (n - i)


# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function if the script is being run
    main()
