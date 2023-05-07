# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time

"""
add print_delay function to create a more immersive experience
"""

def print_delay(text, delay=2):
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

    print_delay("You have to choose between different doors, rooms and path to find your way.")

    print_delay("Your task is to get to the end and win the game.")

    print_delay("Be careful though! The decisions you make will be your fate.")

    print_delay("======================================")

def intro():
    print_delay("You wake up in a strange and mysterious room, confused and scared, without any memory of how you goy there!")

    print_delay("You get yourself together and decide to go and explore.")
    
    print_delay("The right path could save yout life, the wrong door could end it!")

    print_delay("In front of you there are 3 doors, a black door, a yellow door, and a white door.")


def choose_door():
    print_delay("Which door do you choose? (black/yellow/white)")
    choice = input().lower()
    if choice == "black":
        print_delay("You open the black door.")
        black_door()
    elif choice == "yellow":
        print_delay("You open the yellow door.")
        yellow_door()
    elif choice == "white":
        print_delay("You open the white door.")
        white_door()
    else:
        print_delay("Invalid choice. Try again.")
        choose_door()


def black_door():
    print_delay("You enter a room filled with treasure!")
    print_delay("Congratulations! You win the game.")

def yellow_door():
    print_delay("You enter a room full of beasts.")
    print_delay("The beasts devour you.")
    print_delay("Game Over!")

def white_door():
    print_delay("You enter a dark forest.")
    print_delay("There are two paths in front of you.")
    print_delay("One leads to a cave and the other to a river.")

    print_delay("Which path do you choose? (cave/river)")
    choice = input().lower()
    if choice == "cave":
        print_delay("You enter a cave and find a hidden treasure!")
        print_delay("Congratulations! You win the game.")
    elif choice == "river":
        print_delay("You follow the river and encounter a group of hostile creatures.")
        fight_or_flee()


def fight_or_flee():
    print_delay("Do you want to fight or flee? (fight/flee)")
    choice = input().lower()
    if choice == "fight":
        print_delay("You try to fight, but the creatures overpower you.")
        print_delay("Game Over!")
    elif choice == "flee":
        print_delay("You manage to escape and find a safe place.")
        print_delay("You continue your journey.")
        continue_journey()
    else:
        print_delay("Invalid choice. Try again.")
        fight_or_flee()


def continue_journey():
    print_delay("You come across a village.")
    print_delay("The villagers inform you that a powerful wizard resides in the nearby mountains.")
    print_delay("They believe the wizard can help you find your way back home.")
    print_delay("Do you want to visit the wizard? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        print_delay("You decide to visit the wizard.")
        mountain_path()
    elif choice == "no":
        print_delay("You choose not to visit the wizard and continue your own journey.")
        print_delay("Congratulations! You win the game.")
    else:
        print_delay("Invalid choice. Try again.")
        continue_journey()

def mountain_path():
    print_delay("You embark on a treacherous journey towards the mountain.")
    print_delay("After a long and difficult climb, you reach the wizard's lair.")
    print_delay("The wizard welcomes you and asks you to complete a task to prove your worth.")
    print_delay("He presents you with two doors.")
    print_delay("Behind one door lies the ultimate knowledge, and behind the other lies doom.")

    print_delay("Which door do you choose? (knowledge/doom)")
    choice = input().lower()
    if choice == "knowledge":
        print_delay("You open the door and find the ultimate knowledge.")
        print_delay("The wizard is impressed and offers to help you find your way back home.")
        print_delay("But before you leave, he warns you about an ancient curse.")
        print_delay("To break the curse, you must retrieve a sacred artifact.")
        print_delay("The artifact is hidden deep in a forbidden temple.")
        print_delay("Will you accept the wizard's quest? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            print_delay("You accept the wizard's quest and set off to find the forbidden temple.")
            print_delay("Your journey is perilous, but after many hardships, you arrive at the temple.")
            temple()
        elif choice == "no":
            print_delay("You decline the wizard's quest and decide to find your own way back home.")
            print_delay("Congratulations! You win the game.")
        else:
            print_delay("Invalid choice. Try again.")
            mountain_path()
    elif choice == "doom":
        print_delay("You open the door and are consumed by darkness.")
        print_delay("Game Over!")
    else:
        print_delay("Invalid choice. Try again.")
        mountain_path()



def play_game():
    title()
    instructions()
    intro()
    choose_door()

play_game()
