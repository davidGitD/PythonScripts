print('My first py line!!')

# Functions with console input
def whoIs():
    whoIs = input("Who are you?")
    print("Ahh! So you are ",whoIs)

def ageIs():
    AgeIs = input()
    print("Wow you are",int(AgeIs)+100,"Sooo old")

# Functions manipulating Strings
def wordSpell(word):
    for letter in word:
        print(letter)

def checkLetter(letter,word):
    if letter in word:
        print('Correct')
    else:
        print('The word doesn`t contains '+letter)
# MAIN
#word = input("Enter a word: ")
#wordSpell(word)

letter = input('Enter a letter: \n')
word = input('Enter a word: \n')
letterCut = letter[:1]
checkLetter(letterCut,word)
