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
    print_delay("You wake up in a mysterious room.")
    print_delay("Explore different rooms, make choices, and see how the story unfolds.")
    print_delay("Your goal is to reach the end and win the game.")
    print_delay("Be careful! Some choices may lead to failure.")
    print_delay("======================================")

def intro():
    print_delay("You wake up in a mysterious room.")
    print_delay("There are three doors in front of you.")
    print_delay("One is red, one is blue, and one is green.")

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
