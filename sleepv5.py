# iterator is an object that allows you to iterate over collections of data, 
# such as lists, tuples, dictionaries, and sets
def main():
    n = int(input("How many Sheeps? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐏" * i
    
if __name__ =="__main__":
    main()