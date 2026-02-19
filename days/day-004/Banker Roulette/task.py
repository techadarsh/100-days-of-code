# Figure out how to pick a random name from the list of friends.
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_name = friends[random.randint(0, len(friends)-1)]

print(random_name)

random_choice_name = random.choice(friends)

print(random_choice_name)