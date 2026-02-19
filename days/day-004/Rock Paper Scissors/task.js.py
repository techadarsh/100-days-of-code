# You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about
# randomisation and Lists to achieve this.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

game_item = [rock,paper,scissors]
user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choice > 2:
    print("you choose Invalid number, You loose !")
else:
    user_input = game_item[user_choice]
    bot_choice = game_item[random.randint(0,2)]
    if user_input == rock:
        print("You choose, Rock")
        print(rock)
        if bot_choice == paper:
            print("Computer choose, Paper")
            print(paper)
            print("Bot Wins!")
        elif bot_choice == scissors:
            print("Computer choose, Scissors")
            print(scissors)
            print("You Win!")
        elif bot_choice == rock:
            print("Computer choose, Rock")
            print(rock)
            print("Draw !")

    elif user_input == paper:
        print("You choose, Paper")
        print(paper)
        if bot_choice == paper:
            print("Computer choose, Paper")
            print(paper)
            print("Draw !")
        elif bot_choice == scissors:
            print("Computer choose, Scissors")
            print(scissors)
            print("Bot Wins!")
        elif bot_choice == rock:
            print("Computer choose, Rock")
            print(rock)
            print("You Win !")
    elif user_input == scissors:
        print("You choose, Scissors")
        print(scissors)
        if bot_choice == paper:
            print("Computer choose, Paper")
            print(paper)
            print("You Win !")
        elif bot_choice == scissors:
            print("Computer choose, Scissors")
            print(scissors)
            print("Draw !")
        elif bot_choice == rock:
            print("Computer choose, Rock")
            print(rock)
            print("Bot Win!")
