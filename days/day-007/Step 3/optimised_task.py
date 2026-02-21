import random

word_list = ["aardvark", "baboon", "camel", "penselvania", "pineapple"]

chosen_word = random.choice(word_list)
print(chosen_word)

# create display as list of underscores
display = []
for _ in range(len(chosen_word)):
    display.append("_")

print("".join(display))

# keep guessing until no underscores left
while "_" in display:
    guess = input("Guess a letter: ").lower()

    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter

    print("".join(display))
    print()

print("You Win.")