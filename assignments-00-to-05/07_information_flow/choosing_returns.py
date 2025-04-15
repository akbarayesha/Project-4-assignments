ADULT_AGE: int = 18  # U.S. age of adulthood

def is_adult(age: int) -> bool:
    """
    Returns True if the given age is greater than or equal to ADULT_AGE, otherwise returns False.
    """
    return age >= ADULT_AGE

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

if __name__ == "__main__":
    main()