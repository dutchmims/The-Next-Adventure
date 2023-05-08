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
    print("==========================================================================================================")
    print("                                                                                                          ")
    print("                                                The Next Adventure                                        ")
    print("                                                                                                          ")
    print("==========================================================================================================")


def instructions():
    print_delay("Instructions:")

    print_delay("You have to choose between different doors, rooms and path to find your way.")

    print_delay("Your task is to get to the end and win the game.")

    print_delay("Be careful though! The decisions you make will be your fate.")

    print_delay("===========================================================================================================")

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
    print_delay("You find yourself in a walled maze!")
    print_delay("You need to find your way out of the maze before it devours you.")
    print_delay("You hear some rustling and voices!")
    print_delay("You must choose which way to go.")
    print_delay("You can either choose to go left or right.")

    print_delay("Which way will you choose? (left/right)")
    choice = input().lower()
    if choice == "left":
        print_delay("You go left and eventually come across a mirror!")
        print_delay("You look into the mirror and nothing!")
        print_delay("After a few seconds, you start to see you entire future unfold in the mirror, but it all happens so quickly!")
        print_delay("You pass out!")
        print_delay("Suddenly you wake up and Its morning.")
        print_delay("There is an Elf standing over you with a big grin on his face")
        print_delay("He introduces himself as Ernie the Elf and tells you the way out of the maze")
        print_delay("You listen intently to his instructions, bid farewell and set off to find your way out of the maze")
        print_delay("After walking for a while you eventually see the exit, but Its guarded by two Trolls")
        print_delay("You have to decide to fight your way out or try and sneak by the Trolls")
        print_delay("Which way will you choose? (fight/sneak)")
    choice = input().lower()
    if choice == "fight":
        print_delay("You decide to take on the two Trolls! Attacking them while their backs are turned.") 
        print_delay("you surprise them and get the upper hand. After a long struggle, the Trolls gain the upper hand and kill you")
        print_delay("Game Over!")
    elif choice == "sneak":
        print_delay("You manage to climb the wall of the maze and find a way out without the Trolls spotting you")
        print_delay("There are two paths in front of you")
        print_delay("One leads to a cave and the other to a river.")
        print_delay("Which path do you choose? cave/river")
    else:
        print_delay("Invalid choice. Try again.")
        black_door()	

     print_delay("Which path do you choose? (cave/river)")
    choice = input().lower()
    if choice == "cave":
        print_delay("You enter a cave and find a hidden treasure!")
        print_delay("Congratulations! You win the game.")
    elif choice == "river":
        print_delay("You follow the river and encounter a group of hostile creatures.")
        fight_or_flee()


def yellow_door():
    print_delay("You enter a room full of beasts.")
    print_delay("The beasts devour you.")
    print_delay("Game Over!")
    print_delay("Game Over!")
print_delay("Game Over!")
print_delay("Game Over!")
print_delay("Game Over!")
print_delay("Game Over!")
print_delay("Game Over!")
print_delay("Game Over!")
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

def temple():
    print_delay("You enter the forbidden temple, feeling the weight of ancient power.")
    print_delay("The temple is filled with traps and guardians, testing your every step.")
    print_delay("As you navigate through the treacherous halls, you finally reach the chamber of the sacred artifact.")
    print_delay("But retrieving it won't be easy. A guardian stands between you and the artifact.")

    print_delay("Will you fight the guardian, use stealth, or find another way? (fight/stealth/another)")
    choice = input().lower()
    if choice == "fight":
        print_delay("You engage in a fierce battle with the guardian.")
        print_delay("After a grueling fight, you emerge victorious.")
        print_delay("You claim the sacred artifact and break the ancient curse.")
        print_delay("The wizard is grateful for your bravery and grants you safe passage back home.")
        print_delay("Congratulations! You win the game.")
    elif choice == "stealth":
        print_delay("You decide to use your stealth skills to navigate past the guardian.")
        chance = random.randint(0, 1)  # Randomly determine success or failure
        if chance == 0:
            print_delay("Your attempt to sneak past the guardian fails.")
            print_delay("The guardian captures you, and you fail to retrieve the artifact.")
            print_delay("Game Over!")
        else:
            print_delay("Your stealthy approach succeeds!")
            print_delay("You retrieve the sacred artifact and break the ancient curse.")
            print_delay("The wizard is impressed by your resourcefulness and grants you safe passage back home.")
            print_delay("Congratulations! You win the game.")
    elif choice == "another":
        print_delay("You look for another way around the guardian.")
        print_delay("After careful exploration, you discover a hidden passage.")
        print_delay("You successfully bypass the guardian and reach the sacred artifact.")
        print_delay("You break the ancient curse")

        print_delay("You break the ancient curse and retrieve the sacred artifact.")
        print_delay("The wizard commends your ingenuity and grants you safe passage back home.")
        print_delay("Congratulations! You win the game.")
    else:
        print_delay("Invalid choice. Try again.")
        temple()


def play_game():
    title()
    instructions()
    intro()
    choose_door()

play_game()
