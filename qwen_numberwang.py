import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!\n")

    while True:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too small! Try again.\n")
            elif guess > secret_number:
                print("Too big! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempt(s).")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

if __name__ == "__main__":
    number_guessing_game()
