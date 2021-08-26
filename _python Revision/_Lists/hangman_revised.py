# Hangman Game
#
# The classic game of Hangman.  The computer picks a random word
# and the player has to guess it, one letter at a time.  If the player
# can't guess the word in time, the little stick figure gets hanged.
# Modified By
# Eamonn Godfrey
# 13214814
# 15/07/21

# imports
import random

# constants
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ["OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON"]
#add 5 cars to word list
WORDS += "NAVARA", "COMMODORE", "BERINA", "SWIFT", "PROTEGE"
#delete 2 elements
value1 = random.randrange(0, len(WORDS))
del WORDS[value1]
value2 = random.randrange(0, len(WORDS))
del WORDS[value2]

# initialize variables
playername = ""
word = random.choice(WORDS)   # the word to be guessed
so_far = "-" * len(word)      # one dash for each letter in word to be guessed
wrong = 0                     # number of wrong guesses player has made
used = []                     # letters already guessed

#assigning playername and implementing into greeting message
print("\n=========================================================================")
playername = input("Welcome to Hangman! Who is playing? >> ")
print("Welcome", playername, "and good luck!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()
    
    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nYes!", guess, "is in the word!")

        # create a new so_far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]              
        so_far = new

    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    msg = "\nSorry, {}, but you've been hanged!"
    print(msg.format(playername))
else:
    msg = "\nCongratulations {}! You guessed the word!"
    print(msg.format(playername))
    
print("\nThe word was", word)
print("\nThe possible words were", WORDS)

input("\n\nPress the enter key to exit.")
