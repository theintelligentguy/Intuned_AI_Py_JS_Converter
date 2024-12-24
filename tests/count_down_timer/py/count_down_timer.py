# countdown_timer.py
import time

def countdown(start):
    for i in range(start, -1, -1):
        print(f"Countdown: {i}")
        time.sleep(1)
    print("Time's up!")

if __name__ == "__main__":
    start = int(input("Enter the starting number for the countdown: "))
    countdown(start)
