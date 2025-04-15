import random

# Probability of stopping
DONE_LIKELIHOOD = 0.3  # Adjust this value as needed

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Ends function execution, returning to main()
        print(curr_num, end=" ")

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done")

if __name__ == "__main__":
    main()
