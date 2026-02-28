"""
Day 21: Snack game Part 2

Step 4: Create a Snack Food: we will create a snack food by using turtle module, and
we will use circle shape to create the food of the snack.
We will also set the color of the food to red, and we will set the speed of the food to 0.

Step 5: Detect Collision with Food: we will create a function to detect collision between the snack and
the food, and we will call this function every 100 milliseconds using ontimer() method.

Step 6: Detect Collision with Wall: we will create a function to detect collision between the snack and
the wall, and we will call this function every 100 milliseconds using ontimer() method.

Step 7: Detect Collision with Tail: we will create a function to detect collision between the snack and
the tail, and we will call this function every 100 milliseconds using ontimer() method.

"""

# Class Inheritance:
"""
class FIsh(Animal):
    def __init__(self):
        super().__init__()
"""
# example of class inheritance, we have a class called Fish that inherits from the Animal class, and we use the super() function to call the __init__() method of the parent class.

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, Exhale")

    def swim(self):
        print("Moving on water")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Doing this underwater")

    def swim(self):
        super().swim()
        print("Doing this underwater")


nemo = Fish()
nemo.breath()
nemo.swim()
print(nemo.num_eyes)

# slicing in Python, is work with list, tuple, string, and other iterable objects,
# and it allows us to extract a portion of the iterable object by specifying the start, stop, and step parameters.
my_list = [1, 2, 3, 4, 5]
# my_list[start:stop(n - 1):step]
print(my_list[1:4:2]) # [2, 4]
print(my_list[::2]) # [1, 3, 5]
print(my_list[:3]) # [1, 2, 3]
print(my_list[3:]) # [4, 5]