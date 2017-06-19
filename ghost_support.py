''' Ghost Word support library '''

from graphics import *
import random

# --- Your code should use WINSIZE for the window size.
# If someone changes the value of this variable, your window
# size should change too. Do not create a different version
# of this variable in your code.

# Valid values of WINSIZE are 600 to 1000.
WINSIZE = 800


# --- Call this function to get the next word.
def choose_word(word_list):
   """
   Parameter: a list of strings (words)
   Return: a word chosen at random from the list
   """

   # --- Comment the line below back in if you want
   # to force a specific word for testing
   # return 'BLAH'

   return random.choice(word_list)