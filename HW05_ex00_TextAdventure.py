#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body

def infinite_stairway_room(name,count=0):
    print("{} walks through the door to see a dimly lit hallway.".format(name))
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print('{} take the stairs'.format(name))
        if (count > 0):
            print("but {} is not happy about it".format(name))
        infinite_stairway_room(name, count + 1)
    # option 2 == ?????
    if next == option_2:
        pass


def gold_room(name):
    print("This room is full of gold.  How much do {} take?".format(name))

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, {} is not greedy, {} wins!".format(name, name))
        exit(0)
    else:
        dead("{} greedy goose!".format(name))


def bear_room(name):
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is {} going to move the bear?".format(name))
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take" or next == "honey":
            dead("The bear looks at {} then slaps {} face off.".format(name, name + "\'s"))
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. {} can go through it now.".format(name))
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open" or next == "door" and bear_moved:
            gold_room(name)
        else:
            print("I got no idea what that means.")


def cthulhu_room(name):
    print("Here {} see the great evil Cthulhu.".format(name))
    print("He, it, whatever stares at {} and you go insane.".format(name))
    print("Do {} flee for {} life or eat {} head?".format(name, name + '\'s', name + '\'s'))

    next = input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(name)


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    name = input("Hi, what is your name? ")
    print("{} is in a dark room.".format(name))
    print("There is a door to {} right and left.".format(name + '\'s'))
    print("Which one does {} take?".format(name))

    next = input("> ")

    if next == "left":
        bear_room(name)
    elif next == "right":
        cthulhu_room(name)
    else:
        dead("{} stumbles around the room until {} starve.".format(name, name))

if __name__ == '__main__':
    main()
