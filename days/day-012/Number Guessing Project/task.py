"""
The goal is to build a guess the number game.

Demo
https://appbrewery.github.io/python-day12-demo/

ASCII Art
You can get hold of ASCII art using the link below: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
"""
"""
The goal is to build a guess the number game.
Demo
TODO 1: ask user to the level they want to play
TODO 2: create a random number b/w 1 to 100
TODO 3: check for 
"""
import random
import art
def play_game():
    print(art.logo)
    print("Welcome to Number Guessing Project\nI'm thinking of a number between 1 and 100")
    game_level = input("Choose a difficulty level: easy, medium, hard: ").lower()

    random_number = random.randint(1,100)
    game_level_dist = {
        "easy":15,
        "medium":10,
        "hard":5
    }

    lives = game_level_dist[game_level]
    game_continue = True

    while game_continue:
        user_guess = int(input("Make a guess: "))
        if user_guess == random_number:
            game_continue = False
            lives = 0
            print(f"You got it! The number was {random_number}")
        elif user_guess > random_number:
            lives -= 1
            print("Your guess is too high!")
            print("Guess again!")
            print(f"You have {lives} attempts remaining to guess the number.")
        elif user_guess < random_number:
            lives -= 1
            print("Your guess is too low!")
            print("Guess again!")
            print(f"You have {lives} attempts remaining to guess the number.")
        else :
            game_continue = False

        if not lives:
            game_continue = False

play_game()