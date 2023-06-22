import time
import random


def print_pause(*messages):
    for message in messages:
        print(message)
        time.sleep(2)


def intro():
    print_pause(
        "You find yourself standing in an open field, filled with grass "
        "and yellow wildflowers."
    )
    print_pause(
        "Rumor has it that a wicked fairy is somewhere around here, "
        "and has been terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand, you hold your trusty (but not very effective) "
        "dagger."
    )


def house():
    print_pause("You approach the door of the house.")
    print_pause(
        "You are about to knock when the door opens and out "
        "steps a wicked fairy."
    )
    print_pause("Eep! This is the wicked fairy's house!")
    print_pause("The wicked fairy attacks you!")

    # New scenarios and outcomes
    while True:
        choice = input(
            "Would you like to (1) fight, (2) run away, "
            "or (3) bribe the fairy with gold?\n"
        )
        if choice == "1":
            if random.choice(["win", "lose"]) == "win":
                print_pause("You manage to defeat the wicked fairy!")
                print_pause("Congratulations! You win!")
            else:
                print_pause("Unfortunately, "
                            "you are no match for the wicked fairy.")
                print_pause("Game Over.")
            break
        elif choice == "2":
            print_pause("You run away from the wicked fairy.")
            print_pause("As you flee, "
                        "you stumble upon a hidden path leading "
                        "to a secret treasure.")
            print_pause("Congratulations! You win!")
            break
        elif choice == "3":
            print_pause("You try to bribe the wicked fairy with gold.")
            print_pause("The fairy's greed gets the better of her, "
                        "and she accepts the bribe.")
            print_pause("You successfully bypass the fairy "
                        "and enter the house.")
            print_pause("Inside, you discover a powerful artifact. "
                        "Congratulations! You win!")
            break
        else:
            print_pause("Invalid input. Please enter a valid choice.")


def cave():
    print_pause("You peer cautiously into the cave.")

    # New scenarios and outcomes
    while True:
        choice = input(
            "Do you want to (1) search for treasure or "
            "(2) explore deeper into the cave?\n"
        )
        if choice == "1":
            if random.choice(["win", "lose"]) == "win":
                print_pause("You enter the cave and "
                            "find a hidden treasure chest!")
                print_pause("Congratulations! You win!")
            else:
                print_pause("As you search for treasure, "
                            "you trigger a trap and get caught.")
                print_pause("Game Over.")
            break
        elif choice == "2":
            print_pause("You decide to explore deeper into the cave.")
            print_pause("As you venture deeper, you encounter a "
                        "legendary dragon guarding its hoard.")
            while True:
                choice = input(
                    "Would you like to (1) fight the dragon or "
                    "(2) try to steal some treasure quietly?\n"
                )
                if choice == "1":
                    if random.choice(["win", "lose"]) == "win":
                        print_pause("You bravely face the dragon and "
                                    "emerge victorious!")
                        print_pause("Congratulations! You win!")
                    else:
                        print_pause("The dragon's fiery breath "
                                    "overwhelms you.")
                        print_pause("Game Over.")
                    break
                elif choice == "2":
                    print_pause("You attempt to quietly steal some treasure.")
                    print_pause("However, the dragon wakes up and "
                                "catches you in the act.")
                    print_pause("Game Over.")
                    break
                else:
                    print_pause("Invalid input. Please enter a valid choice.")
            break
        else:
            print_pause("Invalid input. Please enter a valid choice.")


def play_game():
    intro()
    while True:
        choice = input(
            "Enter 1 to knock on the door of the house.\n"
            "Enter 2 to peer into the cave.\n"
            "What would you like to do?\n(Please enter 1 or 2).\n"
        )
        if choice == "1":
            house()
            break
        elif choice == "2":
            cave()
            break
        else:
            print_pause("Invalid input. Please enter 1 or 2.")


def play_again():
    while True:
        choice = input("Would you like to play again? (y/n)\n").lower()
        if choice == "y":
            print_pause("Great! Restarting the game...")
            play_game()
        elif choice == "n":
            print_pause("Thanks for playing! Goodbye.")
            break
        else:
            print_pause("Invalid input. Please enter 'y' or 'n'.")


def main():
    play_game()
    play_again()


if __name__ == "__main__":
    main()
