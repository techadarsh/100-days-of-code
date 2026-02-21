import random
word_list = ["aardvark", "baboon", "camel", "apple"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
for letter in chosen_word:
    placeholder += "_"

print(placeholder)
guess = input("Guess a letter: ").lower()
fill_paceholder = ""
# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
for letter in chosen_word:
    if guess == letter:
        fill_paceholder += letter
    else:
        fill_paceholder += "_"
print(fill_paceholder)

