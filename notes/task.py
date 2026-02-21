import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
random_word = random.choice(word_list)
print(random_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

# we can either use list or we can use string directly in for loop
# random_word_list = list(random_word)

for letter in random_word:
    if letter == user_guess:
        print("Right")
    else:
        print("Wrong")
