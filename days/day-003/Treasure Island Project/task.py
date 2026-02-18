print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/ ADARSH /______/______/______/______/_____/
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("The air is salty. The jungle is quiet. Somewhere out there… the treasure is waiting.")
print("Your mission: survive the island and find the hidden chest.")

start = input("DO you really want to play this game ? Y/Yes/y/yes for Yes or N/No/n/no for No: ")
speed = ""
lucky_number = ""

if start == "Y" or start == "y" or start == "Yes" or start == "yes":
    print(" You reach a cracked stone crossroad. The sign is broken.\n To the LEFT: a narrow jungle path with faint footprints.\n To the RIGHT: a dark tunnel where cold wind whispers.\n")
    direction = input(" Which way do you go? Type 'left' or 'right': ")

    if direction == "Right" or direction == "RIGHT" or direction == "right":
        print("You step into the tunnel… the ground suddenly disappears!")
        print("You fall into a hidden pit.\n !! Game Over. !! ")
    elif direction == "left" or direction == "LEFT" or direction == "Left":
        print(" You push through vines and thorns… and the trees open to a moonlit lake.")
        print(" The lake water looks deep and silent.\n You can WAIT near the dock… or SWIM across to the island you can barely see.")
        decision = input("What will you do? Type 'wait' or 'swim': ")
        if decision == "wait" or decision == "WAIT" or decision == "Wait":
            print(
                " You wait… minutes feel like hours.\n Finally, ripples appear. A boat drifts in by itself, as if the lake is helping you.\n You step in and reach the island safely.")
        elif decision == "swim" or decision == "SWIM" or decision == "Swim":
            print(
                " You take a deep breath and enter the water… it’s freezing!\n Halfway through, something brushes your leg.\n Swim FAST to rush through… or swim SLOW to stay quiet and careful.")
            speed = input("What do you do? Type 'fast' or 'slow': ")
            if speed == "fast" or speed == "FAST" or speed == "fast":
                print(
                    " You panic and splash wildly!\n A shadow darts under the surface—SNAP!\n Something pulls you down. \n !! Game Over. !! ")
            elif speed == "slow" or speed == "SLOW" or speed == "slow":
                print(
                    " You move slowly… barely making a sound.\n The shadow follows… then fades away.\n You reach the shore, trembling but alive.")
                print(
                    " On the shore, an old stone statue blocks the path.\n Its eyes glow faintly. A message is carved:\n 'Only the lucky number may pass.'")
                lucky_number = input("Enter the code (type 7 or 3): ")
                if lucky_number == "3":
                    print(
                        " The statue rumbles… and the ground opens beneath you.\n You drop into darkness.\n !! Game Over. !! ")
                elif lucky_number == "7":
                    print(
                        " The statue’s eyes dim. The stone slides aside.\n A hidden staircase leads down into an ancient chamber.")
                else:
                    print(
                        " Nothing happens… then the statue wakes up.\n It does not like wrong answers. \n !! Game Over. !! ")
            else:
                print("You freeze in the water… and the lake decides your fate. \n !! Game Over. !! ")

        if speed == "slow" or speed == "SLOW" or speed == "slow":
            if lucky_number != "3":
                print(
                    " Three doors stand before you, each covered in dust.\n RED door: warm air leaks out like fire.\n BLUE door: you hear low growls behind it.\n YELLOW door: complete silence… too calm.")
                door = input("Which door will you choose? Type 'red', 'yellow', or 'blue': ")
                if door == "red" or door == "RED" or door == "Red":
                    print(" You open the red door… flames roar out!\n Burned by fire. \n !! Game Over. !! ")
                elif door == "yellow" or door == "YELLOW" or door == "Yellow":
                    print(
                        " You open the yellow door… light floods the room.\n A golden chest sits in the center.\n You found the treasure.\n !! You Win! !! ")
                elif door == "blue" or door == "BLUE" or door == "Blue":
                    print(
                        " You open the blue door… a dark den.\n Two glowing eyes appear. Then another.\n You can try to face a BEAR… or scare a WOLF with noise.")
                    animal = input("Type 'bear' or 'wolf': ")
                    if animal == "bear" or animal == "BEAR" or animal == "Bear":
                        print(" The bear charges. No time to run.\n Eaten by a bear. \n !! Game Over. !! ")
                    elif animal == "wolf" or animal == "WOLF" or animal == "Wolf":
                        print(
                            " You clap and shout—LOUD!\n The wolf retreats into the shadows.\n Behind the den, you spot a hidden tunnel… leading to the treasure room!\n !! You Win! !! ")
                    else:
                        print("You freeze… and the den chooses for you.\n !! Game Over. !! ")
    else:
        print("You hesitate too long… the island doesn't like indecision. \n !! Game Over. !! ")

