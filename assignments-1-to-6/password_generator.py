import random
import string

def generate_password(length):
    """Generate a random password of given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))

    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        print(generate_password(password_length))

if __name__ == "__main__":
    main()
