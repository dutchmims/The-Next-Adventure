import time

import os


"""
add print_delay function to create a more immersive experience
"""


def print_delay(text, delay=3):
    print(text)
    time.sleep(delay)


def title():

    print("============================================================")
    print("                                                            ")
    print("                   The Next Adventure                       ")
    print("                                                            ")
    print("============================================================")


def welcome():

    print_delay("Welcome to The Next Adventure.")

    print_delay("Here you will learn your fate in The Next Adventure.")

    username = input("Please enter your username:\n")

    print_delay("Hello, " + username + "!")

    print_delay("============================================================")


def instructions():

    print_delay("Instructions:")

    print_delay("You have to choose between different doors, rooms and paths.")

    print_delay("Your task is to get to the end and win the game.")

    print_delay("Be careful though! The decisions you make will be your fate.")

    print_delay("============================================================")


def intro():
    
    print_delay("You wake up in a strange room confused and scared.")
    
    print_delay("You have no memory of how you got there!")

    print_delay("You get yourself together and decide to go and explore.")
    
    print_delay("The right path could save your life")
    
    print_delay("the wrong door could end it!")

    print_delay("In front of you there are 3 doors for you to choose from.")
    
    print_delay("A black door, a yellow door, and a white door.")

    print_delay("============================================================")


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

        print("Invalid choice. Try again.")

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

        print_delay("You go left and walk for a bit.")
        
        print_delay("Eventually you come across a mirror!")

        print_delay("You look into the mirror and nothing!")

        print_delay("After a few seconds, you start to see you entire future.")
        
        print_delay("It all unfolds in the mirror, it all happens so quickly!")

        print_delay("You pass out!")

        print_delay("Suddenly you wake up and It's morning.")

        print_delay("There is an Elf standing over you with a big grin.")

        print_delay("He tells you the way out of the maze.")

        print_delay("You listen intently and bid farewell.")
        
        print_delay("You set off to find your way out of the maze.")

        print_delay("After walking for a while you eventually see the exit.")
        
        print_delay("Its guarded by two Trolls.")

        print_delay("YWill you fight or try and sneak by the Trolls.")

        print_delay("Which way will you choose? (fight/sneak)")

    elif choice == "right":

        print_delay("The noise coming towards gets louder and louder.")

        print_delay("You try to find somewhere to hide, but it's too late.")

        print_delay("A couple of guards come around the corner and spot you.")

        print_delay("You look up and realise they have spotted you!")

        print_delay("They chase you down and catch you.")

        print_delay("You are brought to the dungeon and locked up.")

        print_delay("You have no way of escape!")
        
        print_delay("You shall remain here until death takes you.")

        print_delay("Game Over!")

    else:
        print("Invalid choice. Try again.")

        choose_door()
   
    choice = input().lower()

    if choice == "fight":

        print_delay("You decide to take on the two Trolls!")
        
        print_delay("Attacking them while their backs are turned.") 

        print_delay("You surprise them and get the upper hand.")
        
        print_delay("The Trolls gain the upper hand and kill you.")

        print_delay("Game Over!")

    elif choice == "sneak":

        print_delay("You manage to climb the wall of the maze.")
        
        print_delay("You find a way out without the Trolls spotting you.")

        print_delay("There are two paths in front of you.")

        print_delay("One leads into a cave and the other to a river.")

        print_delay("Which path do you choose? (cave/river)")

    else:
        print("Invalid choice. Try again.")

        black_door()	

    choice = input().lower()

    if choice == "cave":

        print_delay("You head into the cave.")

        print_delay("It's late, you decide to collect wood and light a fire.")

        print_delay("Your fire warms up the cave and you fall asleep.")

        print_delay("Unfortunatley a bear lives deep inside this cave.")
        
        print_delay("The bear kills you in the middle of the night.")

        print_delay("You are never seen or heard from again.")

        print_delay("Game over.")

    elif choice == "river":

        print_delay("You follow the river for several hours.")
        
        print_delay("You eventually come across a rope bridge.")

        print_delay("It's very old and on its last legs!")
        
        print_delay("Crossing it will be trecherous.")

        print_delay("You decide to use the rope bridge and cross the river.")

        print_delay("Once across you continue to follow the river.")
        
        print_delay("All of a sudden you come upon a settlement.")

        print_delay("Several natives spot you approaching!")

        fight_or_flee()


def yellow_door():

    print_delay("You open the door to darkness.")

    print_delay("Scared and alone, you cant see past your nose.")

    print_delay("You scuffle along the wall until you feel a draft.")

    print_delay("Unable to see anything, you keep going towards the draft.")

    print_delay("Eventually, you come across a secret passage.")

    print_delay("Do you go down the secret passage or search the room?")
  
    print_delay("Which way will you choose? (passage/room)")

    choice = input().lower()

    if choice == "passage":

        print_delay("You head down the passage.")

        print_delay("Its dark and damp with a stench of sewers.")

        print_delay("You move down the passage extremely slowly.")
        
        print_delay("Wondering where it goes and what is ahead of you.")

        print_delay("You see a light! Its getting brighter and brighter.")

        print_delay("Eventually you seen to have run out of passage.")
        
        print_delay("You peer out, you look down the side of a mountain!")

        print_delay("Confused and exhausted, with nowhere to go.")
        
        print_delay("You stop to take breath and think.")

        print_delay("All of a sudden, you hear a distant noise.")
        
        print_delay("A strong gush of wind goes past you.")

        print_delay("The noise gets lounder and louder.")
        
        print_delay("The wind blows fierce.")
        
        print_delay("You hang on to the sides of the passage!")

        print_delay("You start to panic!")

        print_delay("Then, a torrent of water barrels down the passage.")
        
        print_delay("It sweeps you out the mountain and to certain death!")

        print_delay("Game Over!")

    elif choice == "room":

        print_delay("You decide to stay in the room.")
        
        print_delay("To find out what secrets are hidden inside.")

        print_delay("After shuffling past the passage")
        
        print_delay("You trip over something on the ground!")

        print_delay("Still unable to see past you nose!")
        
        print_delay("You bend down to investigate, to find a pile of bones!")

        print_delay("Terrified, unable to see anything, you hear something!")

        print_delay("The smell in the room becomes stronger!")

        print_delay("You hear something that resembles yawning.")

        print_delay("Before you know it, growling takes over, then snarling.")

        print_delay("Terrified, you crouch down and wait your doom!")

        print_delay("Out of nowhere!")
        
        print_delay("A pack of wolves pounce on you and tear you apart.")

        print_delay("Game Over!")

    else:
        print("Invalid choice. Try again.")

        yellow_door()


def white_door():

    print_delay("You find yourself in an overgrown, dark and damp forest.")
    
    print_delay("There's a thick and heavy fog all around.")

    print_delay("Not knowing where you are or being able to see the sun.")
    
    print_delay("You have a tough choice to make.")

    print_delay("You decide to walk straight ahead, with caution.")
    
    print_delay("Avoiding deadly sharp and spikey bushes, watching your back.")

    print_delay("After a while without getting far, you decide to rest.")
    
    print_delay("You gather your bearings before moving forward.")

    print_delay("You give yourself the lift needed to carry on.")

    print_delay("Eventually you come across two paths.")

    print_delay("One leads to a cave and the other to a river.")

    print_delay("Which path do you choose? (cave/river)")

    choice = input().lower()

    if choice == "cave":

        print_delay("You head in to the cave")

        print_delay("It's late, so you decide to collect wood")
        
        print_delay("You light a fire to stay warm.")

        print_delay("Your fire warms up the cave and you fall asleep.")

        print_delay("Unfortunately a bear lives deep inside this cave.")
        
        print_delay("It wakes up and kills you in the middle of the night.")

        print_delay("You are never seen or heard from again.")

        print_delay("Game over.")
    
    elif choice == "river":

        print_delay("You follow the river for several hours.")
        
        print_delay("You eventually come across a rope bridge.")

        print_delay("It's very old and on its last legs!")
        
        print_delay("Crossing it will be treacherous.")

        print_delay("You decide to use the rope bridge and cross the river.")

        print_delay("Once across you continue to follow the river.")
        
        print_delay("Suddenly you come upon a settlement.")

        print_delay("Several natives spot you approaching!")

        fight_or_flee()

    else:
        print("Invalid choice. Try again.")
        
        white_door()


def fight_or_flee():

    print_delay("Do you want to fight or flee? (fight/flee)")

    choice = input().lower()

    if choice == "fight":
        
        print_delay("You try to fight, but the natives overpower you.")

        print_delay("They bring you to their leader.")

        print_delay("Here, your fate will be decided!")

        print_delay("You are executed then and there!")

        print_delay("Game Over!")

    elif choice == "flee":

        print_delay("You manage to escape and find a safe place.")

        print_delay("You continue your journey.")

        continue_journey()

    else:

        print("Invalid choice. Try again.")

        fight_or_flee()


def continue_journey():

    print_delay("You come across a village.")

    print_delay("The villagers chat to you and ask some questions.")
    
    print_delay("They tell you that a wizard resides in the nearby mountains.")

    print_delay("They believe the wizard can help you find your way home.")

    print_delay("Do you want to visit the wizard? (yes/no)")

    choice = input().lower()

    if choice == "yes":

        print_delay("You decide to visit the wizard.")

        mountain_path()

    elif choice == "no":

        print_delay("You decide not to visit the wizard.")
        
        print_delay("You continue on your own journey.")

        print_delay("You trek into the wilderness, never to be seen again!")

        print_delay("Game Over!")

    else:

        print("Invalid choice. Try again.")

        continue_journey()


def mountain_path():

    print_delay("You embark on a treacherous journey towards the mountain.")

    print_delay("After a long difficult climb, you reach the wizard's lair.")

    print_delay("The wizard welcomes you in.")
    
    print_delay("He asks you to complete a task to prove your worth.")

    print_delay("He presents you with two doors.")

    print_delay("Behind one door lies the ultimate knowledge.")
    
    print_delay("Behind the other lies enlightenment.")

    print_delay("Which door do you choose? (knowledge/enlightenment)")

    choice = input().lower()

    if choice == "knowledge":

        print_delay("You open the door and find the ultimate knowledge.")

        print_delay("The wizard is impressed and offers to help you.")
        
        print_delay("He gives you details to find your way back home.")

        print_delay("Before you leave he warns you about an ancient curse.")

        print_delay("To break the curse, you must retrieve a sacred artifact.")

        print_delay("The artifact is hidden deep in a forbidden temple.")

        print_delay("Will you accept the wizard's quest? (yes/no)")

        choice = input().lower()

        if choice == "yes":

            print_delay("You accept the wizard's quest.")
            
            print_delay("You set off to find the forbidden temple.")

            print_delay("Your journey is perilous, but after many hardships.")
            
            print_delay("You arrive at the temple.")

            temple()

        elif choice == "no":

            print_delay("You decline the wizard's quest.")
            
            print_delay("You decide to find your own way back home.")

            print_delay("You lose, Game over!")

        else:
            print("Invalid choice. Try again.")

            mountain_path()

    elif choice == "Enlightenment":

        print_delay("You open the door and are consumed by darkness.")

        print_delay("Game Over!")

    else:

        print("Invalid choice. Try again.")

        mountain_path()


def temple():

    print_delay("You enter the forbidden temple.")
    
    print_delay("You feel the weight of ancient power.")

    print_delay("The temple is filled with traps and guardians.")
    
    print_delay("They test your every step.")

    print_delay("As you navigate through the treacherous halls.")
    
    print_delay("You finally reach the chamber of the sacred artifact.")

    print_delay("But retrieving it won't be easy.")
    
    print_delay("A guardian stands between you and the artifact.")

    print_delay("Will you fight the guardian or use stealth ? (fight/stealth)")
    
    choice = input().lower()

    if choice == "fight":

        print_delay("You engage in a fierce battle with the guardian.")

        print_delay("He gains the upper hand and hits you.")

        print_delay("You fall to the ground, but manage to get back up.")

        print_delay("You start to become dominat and strike the guardian.")

        print_delay("After a grueling fight, you emerge victorious.")

        print_delay("You claim the sacred artifact and break the curse.")

        print_delay("The wizard is grateful for your bravery.")
        
        print_delay("He grants you safe passage back home.")

        print_delay("Congratulations! You win the game.")


    elif choice == "stealth":

        print_delay("You decide to use your stealth skills")
        
        print_delay("You try to navigate past the guardian.")

        print_delay("Your attempt to sneak past the guardian fails.")

        print_delay("The guardian captures you.")
        
        print_delay("You fail to retrieve the artifact.")

        print_delay("You look to escape.")

        print_delay("After careful exploration, you find a hidden passage.")

        print_delay("You bypass the guardian and reach the sacred artifact.")

        print_delay("You can't break the ancient curse")

        print_delay("The artifact devours you")

        print_delay("You lose, Game Over!")

    else:
        print("Invalid choice. Try again.")

        temple()


def play_game():
    title()
    welcome()
    instructions()
    intro()
    choose_door()


play_game()

