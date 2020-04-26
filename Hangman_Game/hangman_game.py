#------------- Import Modules --------------
import string                                                                             #Used for playable letters list
import random                                                                             #Randomized turn selection
import time                                                                               #Stylization of text

# ------------ Global Variables ------------
gameStillGoing = True
winner = None
limbsRemaining = 7
secretWord = ''
guessedLetters = []
nextMove = ''

player_1 = ''
player_2 = ''
players = [player_1, player_2]                                                            # Who are playing this game?
currentTurn = random.choice(players)                                                      # Who's turn is it?

# ------------ Lists and vars --------------                                              #Lists and vars are later used in the code to be randomely selected
letters = string.ascii_uppercase                                                          #Only uppercase ASCII letters may be used in this game

# ------------ Functions -------------------
def getPlayers():
  global player_1, player_2, currentTurn
  player_1 = input("Input player 1 > ")
  player_2 = input("Input player 2 > ")

def getWord():
  try:
    secretWord = input(f"\n{currentTurn}, which word do you want your opponent to guess: \n > ").upper()
    if secretWord.isalpha():
      if len(secretWord) > 4:
        print(secretWord)
      else:
        print(f"\nYour word '{secretWord}' is too short. Minimum of 5 characters")
    else:
      print(f"\nYour word '{secretWord}' contains characters other than letters.")
  except NameError:
    print("\nThe word is not defined")

def hangman():
  global currentTurn, limbsRemaining, guessedLetters, nextMove
  while limbsRemaining > 0:
    for char in secretWord:
      if char in guessedLetters:
        print(char)
      else:
        print("-")
  print(f"\n{currentTurn} you have {limbsRemaining} limbs remaining.")
  print(f"The following letters are still available: {letters}")
  print(f"You have guessed the following letters: {guessedLetters}")

  if nextMove in secretWord:
    print
  else:
    limbsRemaining -= 1

def playerMove():
  global currentTurn, limbsRemaining, guessedLetters, nextMove
  try:
    nextMove = input(f"{currentTurn} what is your next guess? \n > ").upper()
    if len(nextMove) < 1 or len(nextMove) > 1:
      print(f"You can only input 1 letter")
    elif nextMove.isalpha == False:
      print(f"You can only enter letters")
    else:
      return nextMove
  except NameError:
    print("\nThe word is not defined")

def gallows():
  print(None)

def execution():
  global currentTurn
  getPlayers()
  getWord()

# ------------ Execute ---------------------
execution()                                                                               #Runs entire program

# ------------ Comments --------------------
'''
  # Hangman Game
  # - User input: Play against a second player, or versus the computer
  # - All capitalized letters
  # - Computer must get a list of words from a text file. (https://github.com/Xethron/Hangman/blob/master/words.txt)
  # - Keep scores! How many limbs did it cost you?
  # - Give it an UI in python (optional)
  # - Check the validity of a word using a dictionary (optional)
'''

'''
# Discord Bot (Optional)
# - For those who are done with the creation of the base program you can also port your work into a discord bot.
# - Play versus another player, or versus a computer
# - Playing versus another player is done turn-based. This means that if player 1 inputs a word, player 2 gets to take guesses until he guesses the word or is hanged. Then player 2 inputs their word, and the roles are flipped. 
# - First to X amount of wins (must be an equal amount of turns taken) - if game is tied (Who lost the least amount of limbs)
# - Please test your bots on your own server to reduce spam in the python buddies discord.
# - The completed bot will be implemented in the Python Buddies discord for everyone to use!
'''