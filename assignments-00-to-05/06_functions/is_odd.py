def is_odd(value: int) -> bool:
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    return value % 2 == 1

def main():
    for i in range(10, 20):  # Loop through numbers 10 to 19
        if is_odd(i):
            print(i, "odd")
        else:
            print(i, "even")

if __name__ == '__main__':
    main()