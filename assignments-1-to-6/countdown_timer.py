import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert to minutes and seconds
        timer = f"{mins:02}:{secs:02}"  # Format as MM:SS
        print(timer, end="\r")  # Print on the same line
        time.sleep(1)  # Pause for 1 second
        seconds -= 1

    print("Time's up! ⏰")

def main():
    seconds = int(input("Enter the countdown time in seconds: "))
    countdown_timer(seconds)

if __name__ == "__main__":
    main()
