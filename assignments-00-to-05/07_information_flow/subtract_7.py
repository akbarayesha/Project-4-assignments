def subtract_seven(num):
    """
    Subtracts 7 from the given number and returns the result.
    """
    return num - 7

########## No need to edit code beyond this point :) ##########

def main():
    num = 7  # Initial value
    num = subtract_seven(num)  # Call helper function
    print("this should be zero:", num)

if __name__ == '__main__':
    main()
