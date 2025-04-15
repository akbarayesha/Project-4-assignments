def greet(name: str) -> None:
    """
    Prints a greeting message for the given name.
    """
    print("Greetings", name + "!")

def main():
    name = input("What's your name? ")
    greet(name)

if __name__ == "__main__":
    main()