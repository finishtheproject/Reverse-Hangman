"""
Program: Project 3 (Word Game)
Author: Kenny Truong
Course: CS 115
Description: Reverse hangman.
"""

from ghost_support import *
from graphics import *
from collections import Counter

def readfile(filename):
    """
    Reads the entire contents of a file into a single string using
    the read() method.

    Parameter: the name of the file to read (as a string)
    Returns: the text in the file as a large, possibly multi-line, string
    """

    infile = open(filename, "r")
    filetext = infile.read().lower().split()
    infile.close()

    return filetext



def print_list(list_to_print):
    """
    Print the contents of a list.

    Parameter: the list to print
    Returns: nothing
    """

    for i, item in enumerate(list_to_print):
        print(i, ': ', item, sep="")


def main():
    '''
    Main will go through the process of each step and will call other functions when necessary.
    '''

    List = []
    user = input("Enter a dictionary filename: ")
    print("")
    if user == "wordlist_short.txt" or user == "wordlist_long.txt":
        print("Neato dictionary, pal. Here is some info about it.")
    print("")
    user2 = readfile(user)
    for i in range(len(user2)):
        if user2[i].isalpha():
            if not user2[i] in List:
                List.append(user2[i])
    print("  Size of dictionary:", len(List))
    print("  Frequency of each letter:")
    count = []
    for _ in range(26):
        count.append(0)
    for word in List:
        for char in word:
            index = ord(char) - ord("a")
            count[index] += 1
    for i in range(len(count)):
        letter = chr(i+ord("A"))
        print("\t", letter, count[i])
    print("")
    while True:
        userplay = input("Would you like to play a nice game of Ghost word?" )
        userplaylow = userplay.lower()
        if userplaylow == "n":
            print("Have a super awesome day, friend!")
            sys.exit(1)
        elif userplaylow == "y" or userplaylow == "yes":
            window = GraphWin("GAME!", WINSIZE, WINSIZE)
            window.setBackground("White")
            stickman = human(window)
            wordgame(List, window, stickman)
        else:
            print("Sorry, I didn't understand that.")

def human(window):
    '''
    Draws a human.
    
    :param window: the game window
    :return: leftLeg, rightLeg, leftArm, rightArm, body, head
    '''

    head = Circle(Point(800/2, 800/6), 800/10)
    head.draw(window)
    body = Line(Point(400, 213), Point(800//2, 600))
    body.draw(window)
    rightArm = Line(Point(400, 385), Point(500, 285))
    rightArm.draw(window)
    leftArm = Line(Point(400, 385), Point(300, 285))
    leftArm.draw(window)
    leftLeg = Line(Point(400, 600), Point(300, 685))
    leftLeg.draw(window)
    rightLeg = Line(Point(400, 600), Point(500, 685))
    rightLeg.draw(window)
    return [leftLeg, rightLeg, leftArm, rightArm, body, head]

def wordgame(user, window, stickman):
    '''
    The essential code that makes the game work properly.

    :param user: the game window
    :param window: GraphWin("GAME!", WINSIZE, WINSIZE)
    :param stickman: human(window)
    :return: None
     '''

    secret = choose_word(user)
    secret = secret.upper()
    matches = 0
    w = [] #  Words that are printing.
    guessed = []  #  All guesses.
    incorrectGuess = []
    print("")
    print("\tHINT: ", end = "")
    for i in range(len(secret)):
        w.append("_")
    for i in w:
        print(" ", i, end="", sep="")
    print("")
    print("\tNot in the word: ", incorrectGuess)
    count = 0
    for word in user:
        word = word.upper()
        if len(word) != len(secret):
            continue
        good = True
        for i in range(len(w)):
            if w[i] == "_":
                continue
            if w[i] == word[i]:
                continue
            else:
                good = False
        if good:
            count += 1
    print("\tPossible words matching the pattern: ", count)
    print("")

    while True:
        useranswer = input("Guess: ")
        useranswer = useranswer.upper()
        if len(useranswer) > 1:
            print("Error, only 1 input at a time.")
        elif not useranswer.isalpha():
            print("Error, only alphabetical inputs.")
        elif useranswer in guessed:
            print("Error, you already tried that letter!!!!!")
        else:
            guessed.append(useranswer)
            if useranswer not in secret:
                print("Incorrect!!!!")
                incorrectGuess.append(useranswer)
                stickman[len(incorrectGuess)-1].undraw() # Remove a body part if incorrect guess.
            else:
                for i in range(len(secret)):
                    if useranswer == secret[i]:
                        w[i] = useranswer
                        matches += 1
            if len(incorrectGuess) == 6:
                print("YOU LOSER.")
                print(secret)
                return
            print("")
            print("\tHINT: ", end="")
            for i in w:
                print(" ", i, end="", sep="")
            print("")
            print("\tNot in the word: ", incorrectGuess)
            count = 0
            for word in user:
                word = word.upper()
                if len(word) != len(secret):
                    continue
                good = True
                for i in range(len(w)):
                    if w[i] == "_":
                        continue
                    if w[i] == word[i]:
                        continue
                    else:
                        good = False
                if good:
                    count += 1
            print("\tPossible words matching the pattern: ", count)
            print("")
            if matches == len(secret):
                print("WINNER")
                window.close()
                return
                print("Do you want to play a game?")

main()
