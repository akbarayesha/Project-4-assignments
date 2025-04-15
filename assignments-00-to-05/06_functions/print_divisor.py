def print_divisors(num: int):
    """
    Prints all divisors of the given number.
    """
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Loop from 1 to num inclusive
        if num % i == 0:
            print(i, end=" ")
    print()  # Print newline for formatting

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == '__main__':
    main()
