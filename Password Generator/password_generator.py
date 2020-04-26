#------------- Import Modules --------------
import random                                                                 #Used for randomizing characters
import pyperclip                                                              #Used for copying to clipboard

# ------------ Global Variables ------------
input_length = ""
input_number = ""
input_special = ""
password = []

# ------------ Lists and vars --------------                                  #Lists and vars are later used in the code to be randomely selected
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
specials = ['!','@','#','$','%','&']

# ------------ Functions -------------------
def getUserInput():                                                           #User inputs desired password length, and amount of numbers and special characters
  global input_length, input_number, input_special
  print("\n Please input your desired password length: ")
  input_length = int(input("> "))
  print("\n Please input the amount of numbers that need to be in the password: ")
  input_number = int(input("> "))
  print("\n Please input the amount of special characters that need to be in the password: ")
  input_special = int(input("> "))
  return int(input_length), int(input_number), int(input_special)             #Returns user inputs for later usage

def generatePassword(input_length, input_number, input_special):              #Actual password generation
  global letters, numbers, specials, password                                 #Needs global variables to work
  lengthCount = 0                                                             #counts needed for length determination
  numberCount = 0
  specialCount = 0
  while lengthCount < input_length:                                           #Stops the password from getting too long
    while numberCount < input_number:                                         #Adds number to the password
      password.append(random.choice(numbers))                                 #Randomly selects number from the list
      numberCount += 1
      lengthCount += 1
      #print(f'A number has been added - {numberCount}') #Testing purposes
    while specialCount < input_special:                                       #Adds special character to the password
      password.append(random.choice(specials))                                #Randomly selects special character from the list
      specialCount += 1
      lengthCount += 1
      #print(f'A special character has been added - {specialCount}')          #Testing purposes
    while lengthCount < input_length:                                         #Adds special character to the password
      password.append(random.choice(letters))                                 #Randomly selects special character from the list
      lengthCount += 1
      #print(f'A letter has been added')                                      #Testing purposes
  return random.shuffle(password)


def execution():                                                              #Executes the program
  print(f'\n Welcome to password generator 3000X. The most secure and customizable generator on the market.')

  getUserInput()

  print(f'\nlength: {input_length}')
  print(f'Numbers: {input_number}')
  print(f'Specials: {input_special}')

  generatePassword(input_length, input_number, input_special)                 #Runs password generator
  passwordString = ''.join(password)                                          #Concatenate password list to string

  print(f"\nWe recommend the following password: {passwordString}")
  pyperclip.copy(passwordString)                                              #Copies to clipboard
  print(f"Your new password has been copied to your clipboard.")              #Commented out, repl.it does not have this module

# ------------ Execute ---------------------
execution()                                                                   #Runs entire program

# ------------ Comments --------------------
'''
  # - A program that generates a random password for the user. [✔]
  # - User input: Length  of password, amount of numbers, amount of special characters. [✔]
  # - Mix of upper and lower case numbers [✔]
  # - Minimum of 6 characters [✔]
  # - Instantly copy to clipboard (optional) [✔]
  # - Give it an UI (optional)
'''