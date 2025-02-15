# Import required libraries
from tabulate import tabulate
from pyfiglet import Figlet
from time import sleep
import os

def welcome_message():
    """ Display the welcome screen and wait to press ENTER """
    clear()
    welcome = [
        ["Welcome to the Ultimate Tic-Tac-Toe Game!"],
        ["Created with Passion by Artur Jodkowski"],
        ["as the Final Project for CS50P - Harvard's Python Programming Course, 2025"],
        ["* * * * * * *"],
        ["Press ENTER to Begin the Battle!"]
    ]

    # Display the welcome screen
    print(tabulate(welcome, tablefmt="heavy_grid", colalign=("center",)))

    # Wait for ENTER
    while True:
        if input() == "":
            break
        else:
            clear()
            print(tabulate(welcome, tablefmt="heavy_grid", colalign=("center",)))


def level_message():
    """ Promt the user to select a difficulty level """
    level = [
        ["Choose Your Difficulty Level!"],
        ["Press 1 --> Easy: Just for Fun"],
        ["Press 2 --> Medium: Warm Up Your Brain"],
        ["Press 3 --> Hard: Ready for a Challenge?"],
        ["Press 4 --> Impossible: Dare to Beat the Code?"],
        ["* * * * * * *"],
        ["Make Your Choice and Press ENTER!"],
    ]

    while True:
        clear()
        print(tabulate(level, tablefmt="heavy_grid", colalign=("center",)))

        # Validate user input
        try:
            number = int(input())
            if number in [1, 2, 3, 4]:
                return number
        except ValueError:
            pass


def size_message(level):
    """ Promt the user to select the board size """
    size = [
        ["Choose Your Board Size!"],
        ["Press 2 --> Tiny 2x2 (Quick and Easy)"],
        ["Press 3 --> Classic 3x3 (The Original Duel)"],
        ["Press 4 --> Tactical 4x4 (More Moves, More Fun)"],
        ["Press 5 --> Master 5x5 (Think Bigger!)"],
        ["Press 6 --> Grandmaster 6x6 (Ultimate Brain Workout)"],
        ["Press 7 --> Legend 7x7 (For the Brave)"],
        ["Press 8 --> Titan 8x8 (Think Like a Supercomputer)"],
        ["* * * * * * *"],
        ["Select Your Board Size and Press ENTER!"],
    ]

    # Restrict size options if the level == 4
    if level == 4:
        size = size[0:1] + size[2:3] + size[8:]

    while True:
        clear()
        print(tabulate(size, tablefmt="heavy_grid", colalign=("center",)))

        # Validate board size
        try:
            number = int(input())
            if level in [1, 2, 3] and number in [2, 3, 4, 5, 6, 7, 8]:
                return number
            elif level == 4 and number in [3]:
                return number
        except ValueError:
            pass


def your_turn_message(board, size):
    """ Promt the player to make a move or exit """
    from project import print_board
    message = [
        ["Make Your Move! Enter a Cell Number"],
        ["Or Press 0 to Exit"],
    ]
    # print(tabulate(message, tablefmt="heavy_grid", colalign=("center",)))

    while True:
        # Show current board and instructions
        #clear()
        print_board(board)
        print(tabulate(message, tablefmt="heavy_grid", colalign=("center",)))

        # Validate user imput
        try:
            number = int(input())
            if number in list(range(1, size * size + 1)):
                return number
            elif number == 0:
                clear()
                print(tabulate([["YOU HAVE LEFT THE GAME"]], tablefmt="heavy_grid", colalign=("center",)))
                exit()
        except ValueError:
            pass


def occupied():
    """ Notify the player that the chosen cell is occupied """
    print(tabulate([["This Cell is Occupied. Try Again!"]], tablefmt="heavy_grid", colalign=("center",)))
    sleep(1)


def result_message(result):
    """ Display the result of the game """
    message = ["YOU WON", "YOU LOST", "IT'S A TIE"]

    f = Figlet(font="big")

    if result == "win":
        print(f.renderText(message[0]))
    elif result == "lost":
        print(f.renderText(message[1]))
    elif result == "tie":
        print(f.renderText(message[2]))


def replay_message():
    """ Ask the user to play again """
    replay = [
        ["Would You Like to Play Again?"],
        ["* * * * * * *"],
        ["Press Y --> to Play Again!"],
        ["Press N --> to Quit the Game"],
    ]

    while True:
        # clear()
        print(tabulate(replay, tablefmt="heavy_grid", colalign=("center",)))

        # Validate the response
        reply = input().strip().lower()
        if reply in ["y", "n"]:
            if reply == "y":
                return reply
            else:
                clear()
                exit()
        else:
            pass


def clear():
    """ Clear the console screen """
    # return os.system("clear")
    return os.system("cls" if os.name == "nt" else "clear")
