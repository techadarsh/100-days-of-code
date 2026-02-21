# while loop
#  while something_is_true
    # DO this

#  Below is the link for Reeborg's World Problem for while loop

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# def jump_hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while at_goal() != True:
#     jump_hurdle()

# When would I use While loop and when Should I use For Loop

# For Loop are really great when Iterate over something and you need to do something with each thing that you iterating over,
# for example, here you iterating list and you say fruit in fruits and you need to add pie in every fruit We should use for loop

# similarly we've used range function where range we use 1, 6

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     if wall_on_right() and wall_in_front():
#         turn_left()
#     elif not wall_on_right():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
