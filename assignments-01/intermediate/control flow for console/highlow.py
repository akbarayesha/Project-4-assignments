import random

NUM_ROUNDS = 5

print("Welcome to the High-Low Game!")
print("--------------------------------")

score = 0

for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")
    
    your_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"Your number is {your_number}")

    # Get user input with validation
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess != "higher" and guess != "lower":
        guess = input("Please enter either higher or lower: ").lower()

    # Determine result
    correct = False
    if guess == "higher" and your_number > computer_number:
        correct = True
    elif guess == "lower" and your_number < computer_number:
        correct = True

    # Display result
    if correct:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")

    print(f"Your score is now {score}\n")

# Final message
print("Thanks for playing!")

if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")
