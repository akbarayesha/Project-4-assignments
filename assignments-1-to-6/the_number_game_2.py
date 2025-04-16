import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    print(f"Think of a number between 1 and {x}, and I will try to guess it!")

    while feedback != "c":
        guess = random.randint(low, high)  # Computer makes a guess
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == "h":
            high = guess - 1  # Adjust range downward
        elif feedback == "l":
            low = guess + 1  # Adjust range upward

    print(f"Yay! I guessed your number {guess} correctly! 🎉")

def main():
    x = int(input("Enter the upper limit for the number: "))
    computer_guess(x)

if __name__ == "__main__":
    main()
