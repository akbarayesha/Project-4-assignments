def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = sum(1 for num in lst if num % 2 == 0)  # Count even numbers using list comprehension
    print(count)  # Print the count of even numbers

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  # Stop when the user presses enter
            break
        lst.append(int(user_input))  # Convert input to integer and add to list
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

if __name__ == '__main__':
    main()