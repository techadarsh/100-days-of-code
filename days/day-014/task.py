"""
Approach we should take for this game

1. Breakdown the Problem
2. TO DO list -> Start with easiest
3. Turn the problem into comments
4. Write Code -> Run Code -> Fix Code (Repeat step 4)
"""

# TODO: generate two random numbers for comparing two personality in range of 0 to len(data)
# TODO: print specific entity from data list for user output
# TODO: ask user to give input about how have more follower and check with if the user have correct guess
# TODO: shift second entity to first entity if user guess correct other otherwise end the game
# TODO: repeat the process when user guess correct

import random
import art
from game_data import data

# define variables
game_end = False
first_party = {}
second_party = {}
correct_answer = ""
user_score = 0

def get_random_number():
    random_number = random.randint(0,len(data)-1)
    return random_number

random_one = get_random_number()
random_two = get_random_number()

def print_content(r1,r2):
    global first_party,second_party, correct_answer
    if not len(first_party.keys()):
        first_party = data[r1]
    second_party = data[r2]
    print("first_party", first_party)
    if int(first_party["follower_count"]) > int(second_party["follower_count"]):
        correct_answer = "a"
    else:
        correct_answer = "b"
    print("\n" * 2000)
    print(art.logo)
    if user_score:
        print(f"You're right! Current score: {user_score}.")
    print(f"Compare A: {first_party['name']}, a {first_party['description']}, from {first_party['country']}.")
    print(art.vs)
    print(f"Compare B: {second_party['name']}, a {second_party['description']}, from {second_party['country']}.")

while not game_end:
    print_content(random_one,random_two)
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_guess == correct_answer:
        user_score += 1
        print(f"first_part : {first_party}, \nsecond_party : {second_party}, \ncorrect_answer : {correct_answer}")
        first_party = second_party
        random_two = get_random_number()
    else:
        game_end = True
        print(f"Sorry, that's wrong. Final score: {user_score}")


