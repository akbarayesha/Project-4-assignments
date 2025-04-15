def print_ones_digit(num: int):
    """
    Prints the ones digit of the given number.
    """
    print("The ones digit is", num % 10)

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

if __name__ == '__main__':
    main()