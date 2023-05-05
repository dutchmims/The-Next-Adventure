# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time

"""
add print_delay function to create a more immersive experience
"""

def print_delay(text, delay=1.5):
    print(text)
    time.sleep(delay)

def title():
    print("======================================")
    print("                                      ")
    print("         The Next Adventure           ")
    print("                                      ")
    print("======================================")

def instructions():
    print_delay("Instructions:")
    print_delay("You wake up in a strange and mysteriuos room, confused and scared.")
    print_delay("You get yourself together and decide to go and explore.")
    print_delay("You have to choose between different doors, rooms and path to find your way.")
    print_delay("Your task is to get to the end and win the game.")
    print_delay("Be careful though! The decisions you make will be your fate.")
    print_delay("======================================")

def intro():
    print_delay("You wake up in a mysterious room, confused and scared, without any memory of how you goy there!")
    print_delay("There are three doors. The right door could save yout life, the wrong door could end it!")
    print_delay("There are 3 doors, a red door, a blue door, and a green door.")

def choose_door():
    print_delay("Which door do you choose? (red/blue/green)")
    choice = input().lower()
    if choice == "red":
        print_delay("You open the red door.")
        red_door()
    elif choice == "blue":
        print_delay("You open the blue door.")
        blue_door()
    elif choice == "green":
        print_delay("You open the green door.")
        green_door()
    else:
        print_delay("Invalid choice. Try again.")
        choose_door()

def choose_door():
    print_delay("Which door do you choose? (red/blue/green)")
    choice = input().lower()
    if choice == "red":
        print_delay("You open the red door.")
        red_door()
    elif choice == "blue":
        print_delay("You open the blue door.")
        blue_door()
    elif choice == "green":
        print_delay("You open the green door.")
        green_door()
    else:
        print_delay("Invalid choice. Try again.")
        choose_door()



def play_game():
    title()
    instructions()
    intro()
    choose_door()

play_game()
