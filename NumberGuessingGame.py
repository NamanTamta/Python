# Number guessing game where the player has to guess a randomly generated number within a certain range.
import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Set range values
    low_value = 1
    high_value = 100
    
    # setup game variables
    number_to_guess = random.randint(low_value, high_value) # Randomly generate number to guess
    attempts = 0  # attempt counter
    max_attempts = 6 # maximum attempts allowed
    guessed = False # check if the number is guessed
    print("Max attempts allowed:", max_attempts)

    while attempts < max_attempts and guessed == False:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Make a guess:"))
            attempts += 1

            if guess < low_value or guess > high_value:
                print("Please guess a number within the range(1 - 100)!")
                continue
            if guess < number_to_guess:
                print("Too Low!")
            elif guess > number_to_guess:
                print("Too High!")
            else:
                guessed = True
                print(f"Congratulation! You've guessed the number {number_to_guess} correctly in {attempts} attempts!")

            if not guessed and attempts == max_attempts:
                print(f"Sorry, you've used all your attempts. The number was {number_to_guess}. Better luck next time!")
               
        except ValueError:
            print("Invalid input! Please enter a vaild interger.")
            break


number_guessing_game()