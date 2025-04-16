def access_element(lst, index):
    try:
        return f"Element at index {index}: {lst[index]}"
    except IndexError:
        return "Error: Index out of range."

def modify_element(lst, index, new_value):
    try:
        old_value = lst[index]
        lst[index] = new_value
        return f"Modified index {index}: '{old_value}' → '{new_value}'"
    except IndexError:
        return "Error: Index out of range."

def slice_list(lst, start, end):
    try:
        sliced = lst[start:end]
        return f"Sliced list from index {start} to {end}: {sliced}"
    except Exception as e:
        return f"Error during slicing: {e}"

def main():
    # Initial list
    my_list = ['apple', 'banana', 42, 'grape', 'pineapple']

    while True:
        print("\nCurrent List:", my_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            idx = int(input("Enter index to access: "))
            print(access_element(my_list, idx))

        elif choice == '2':
            idx = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            print(modify_element(my_list, idx, new_val))

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(my_list, start, end))

        elif choice == '4':
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Try again.")

# Run the game
main()
