print("Welcome to the treasure island!") 
crossroad = input("You are at a crossroad. Where do you want to go? Type left or right.")
if crossroad == "left":
    lake = input("you come to a lake. There is an island in the middle of the lake. Type wait to wait for the boat, or swim to swim across the lake: ")
    if lake == "wait":
        doors = input("You arrive to the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which do you choose? ")
        if doors == "yellow":
            print("You found the treasure! You win!")
        else:
            print("You chose a wrong door!")
    else:
        print("You get attacked by an angry trout. You Lose!")
else: 
    print("You lost")

