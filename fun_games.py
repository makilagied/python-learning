#importing the random function library
import random
#defing a display function
def displayMenu():
    print('''
          choose 1 or 2 to play one of the following games, or 3 to quit playing
          1. cornhole
          2. guessing medals
          3. quit
          enter your choice:
          ''')

#defing a cornhole function 
def cornhole():
    print("welcome to Game cornhole")
    #a computer toss points  function
    def computerTossPoints():
        comp=random.randint(0,34)
     
    #a function to print the winner
    def printWinner():
        pass
    
 #a function to allow the second game to be played   
def guessingMedals():
    #allowing user to guess a random number
    guess=int(input("enter your guess as a number (50 to 150): "))
    #a random function to print a computer number
    comprand=random.randint(0,200)
    #checking the conditions for the prizes
    results=comprand-guess
    if results>=50:
        print(f"you were off by {results} hence you have obtained bronze")
    elif results>=20 and results<=49:
        print(f"you were off by {results} hence you have obtained silver")
    elif results>=5 and results<=19:
        print(f"you were off by {results} hence you have obtained gold")
    elif results>=0 and results<=4:
        print(f"you were off by {results} hence you have obtained platinum")



#a function to quit the game
def quitGame():
    print("goodbye. hope you enjoyed playing!")
    
#the mai function for our program
def main():
    i=0
    while i>=0:
        displayMenu()
        choice=int(input("your choice: "))
        if choice == 1:
            cornhole()
        elif choice==2:
            guessingMedals()
        elif choice==3:
            quitGame()
        else:
            print("unknown input")
    i+=1
        
            
main()
