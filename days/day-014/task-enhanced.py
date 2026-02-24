import random
from game_data import data
from art import logo, vs

def clear_screen():
    print("|\n"*30)

def format_account(account):
    name = account['name']
    desc = account['description']
    country = account['country']
    return f"{name}, a {desc}, from {country}"

def get_random_account():
    return random.choice(data)

def get_correct_answer(a, b):
    if a["follower_count"] > b["follower_count"]:
        print("a")
        return "a"
    else:
        print("b")
        return "b"

def get_valid_guess():
    guess = input("Who has more followers? Type 'a' or 'b': " ).lower()
    while guess != 'a' and guess != 'b':
        guess = input("Invalid input. Please Type 'a' or 'b': ").lower()
    return guess

def play_game():
    score = 0
    game_should_continue = True

    account_a = get_random_account()
    account_b = get_random_account()
    while account_b == account_a:
        account_b = get_random_account()

    while game_should_continue:
        clear_screen()
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Compare B: {format_account(account_b)}")

        correct_answer = get_correct_answer(account_a, account_b)
        user_guess = get_valid_guess()

        if user_guess == correct_answer:
            score += 1
            account_a = account_b
            account_b = get_random_account()
            while account_b == account_a:
                account_b = get_random_account()
        else:
            print(f"Sorry, That's wrong. Final score: {score}")
            game_should_continue = False

play_game()