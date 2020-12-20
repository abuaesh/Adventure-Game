import time
import random
import unicodedata

#############################################################################


def print_pause(msg):
    print(msg)
    time.sleep(2)

#############################################################################


def pick_enemy():
    return random.choice(["dragon", "vampire",
                          "giant spider", "ghost",
                          "crazy robot", "malicious clown",
                          "alien", "goblin"])

#############################################################################


def fight(enemy, items):
    # Things that happen when the player fights
    if "sword" in items:
        print_pause(f"As the {enemy} moves to attack, "
                    "you unsheath your new sword."
                    "The Sword of Ogoroth shines brightly in your hand "
                    f"as you brace yourself for the attack. \n But the {enemy}"
                    " takes one look at your shiny new toy and runs away!"
                    f"\nYou have rid the town of the {enemy}."
                    "\n\nYou are victorious!")
    else:
        print_pause("You do your best..."
                    f"\nbut your dagger is no match for the {enemy}."
                    "\n\nYou have been defeated!")

#############################################################################


def cave(items):
    # Things that happen to the player goes in the cave
    print_pause("You peer cautiously into the cave.")
    if "sword" not in items:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    " and take the sword with you.")
        items.append("sword")

    elif "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")

    print_pause("You walk back out to the field.")
    msg = "\nEnter 1 to knock on the door of the house." +\
          "\nEnter 2 to peer into the cave." +\
          "\nWhat would you like to do?" +\
          "\n(Please enter 1 or 2.)"
    return validate_input(input(msg), "door", "cave", msg)

#############################################################################


def field():
    # Things that happen when the player runs back to the field
    print_pause("You run back into the field."
                " Luckily, you don't seem to have been followed.")
    print_pause("You walk back out to the field.")
    msg = "\nEnter 1 to knock on the door of the house." +\
          "\nEnter 2 to peer into the cave." +\
          "\nWhat would you like to do?" +\
          "(Please enter 1 or 2.)"
    return validate_input(input(msg), "door", "cave", msg)

#############################################################################


def house(enemy, items):
    # Things that happen to the player in the house
    print_pause("You approach the door of the house."
                f" You are about to knock when the door opens"
                f" and out steps a {enemy}. Eep! This is the {enemy}'s house!"
                f" The {enemy} attacks you!")
    if "sword" not in items:
        print_pause("You feel a bit under-prepared for this, "
                    "with only having a tiny dagger.")
    msg = "\nWould you like to (1) fight or (2) run away?"
    return validate_input(input(msg), "fight", "run", msg)

#############################################################################


def intro(enemy):
    #  The introduction story
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")

    msg = "Enter 1 to knock on the door of the house." +\
        "\nEnter 2 to peer into the cave." +\
        "\nWhat would you like to do?" +\
        "\n(Please enter 1 or 2.)"
    return validate_input(input(msg), "door", "cave", msg)

#############################################################################


def start():
    items = []
    enemy = pick_enemy()

    choice = intro(enemy)  # user chooses 1 for house, 2 for cave
    while(True):
        if choice == 1:  # door
            choice = house(enemy, items)  # user chooses 1 for fight, 2 for run
            if choice == 1:  # fight
                fight(enemy, items)
                break
            else:  # run away!
                field()
        else:  # cave
            choice = cave(items)


#############################################################################


def validate_input(choice, option1, option2, invalid_msg):
    while(True):
        choice = choice.lower()
        if '1' in choice or option1 in choice:
            return 1
        elif '2' in choice or option2 in choice:
            return 2
        else:
            print_pause("Sorry! I didn't understand")
            choice = input(invalid_msg)

#############################################################################


def play_again():
    choice = input("Would you like to play the game again? (Y/N)")
    again = validate_input(choice, 'y', 'n',
                           "Would you like to play the game again? (Y/N)")
    if again == 1:
        print_pause("Great! Let's play again.")
        return True  # I do not want to use recursion
    elif again == 2:
        print_pause("Thank you for playing my game! Bye bye.")
        return False
