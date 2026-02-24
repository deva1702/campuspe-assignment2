# Number Guessing Game

import random

best_score = None  # Track minimum attempts

def play_game():
    global best_score

    secret_number = random.randint(1, 100)
    attempts = 7

    print("\nI have selected a number between 1 and 100.")
    print("You have 7 attempts!")

    for i in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {i}: Enter your guess: "))
        except ValueError:
            print("Invalid input!")
            continue

        if guess == secret_number:
            print("Congratulations! You guessed correctly.")
            print("Attempts used:", i)

            if best_score is None or i < best_score:
                best_score = i
                print("New Best Score!")

            return
        elif abs(guess - secret_number) <= 5:
            print("Very close!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        print("Attempts remaining:", attempts - i)

    print("You failed! The number was:", secret_number)


while True:
    play_game()
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        break
