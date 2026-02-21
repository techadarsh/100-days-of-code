import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
display = ""
guess = ""
letter_count = 0
while display != chosen_word: # aa___a__
    guess = input("Guess a letter: ").lower()

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for i, letter in enumerate(chosen_word):
        if letter_count > 0:
            if letter == guess and display[i] == "_":
                display = display[:i] + guess + display[i+1:]
        elif letter == guess:
            display += letter
        else:
            display += "_"

    letter_count += 1
    print(display + '\n')

print("You Win.")