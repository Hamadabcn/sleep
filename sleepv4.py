# A generator is a function that returns an iterator that produces a sequence of values when iterated over
# We should use yield when we want to iterate over a sequence, but don't want to store the entire sequence 
# in memory
def main():
    # Get the number of sheeps from the user
    n = int(input("How many Sheeps? "))
    
    # Iterate over the values yielded by the sheep generator function and print each value
    for s in sheep(n):
        print(s)


def sheep(n):
    # Generator function using yield to produce values on the fly
    for i in range(n):
        yield "🐏" * i


# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function if the script is being run
    main()
