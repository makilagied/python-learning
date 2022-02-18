'''The Centaurs and Centaurides from Centauros have contacted Mr. Coder, an earthling, to create a program to simulate two games: 
Cornhole and Guessing Medals. The program should be menu-driven and should use different functions to play each game. Call the file containing your program fun_games.py. 
Your code should include the following functions:
• function displayMenu which displays the menu (given below), allows the user to choose a game to be played and returns the number associated with the game selected by the user, or 3 to quit playing.
Choose 1 or 2 to play one of the following games, or 3 to quit playing
1. Cornhole
2. Guessing Medals
3. Quit
Enter your choice:
• function main that
o repeatedly uses the function displayMenu until the user decides to stop playing the games
o invokes the function to play the chosen game
o prints a goodbye message for the player when they choose to stop playing
• function cornhole to simulate playing the game where a board is mounted at a slant with a hole in the top center part of the board. 
Three oval concentric rings are painted yellow, blue and green around the hole. The nearest oval ring to the hole is yellow then blue then green.
The player tosses each of the 4 corn kernel-filled coloured (red, blue, green and yellow) baggies in the direction of the board, 
attempting to get them in the hole or land them on the surface of the board in any of the coloured rings. After all 4 of the player's bags are tossed from the pitcher's box , 
the player's points are calculated based on the following rules:
o 10 points for the red baggie tossed right into the hole
o 8 points for any other colour baggie tossed right into the hole
o 3 points for any baggie landing on the yellow ring, but twice the points for the yellow baggie landing on the yellow ring
o 2 points for any baggie landing on the blue ring, but twice the points for the blue baggie landing on the blue ring
o 1 point for any baggie landing on the green ring, but twice the points for the green baggie landing on the green ring
The game is played against the computer. Points for the computer are randomly generated between and including 0 to 34 points. 
If the player's points are more than the computer's points then your program will print the message "Congratulations! You won the game by N points.", 
where N is the difference between the player's points and the computer's points. Likewise, if the player's points are less than the computer's,
your program will print "Sorry, you lost the game by N points."; a draw is reported as "The game was a draw with N points each.".
Your program should include the following functions to play the Cornhole game:
o function computeTossPoints which, given the colour of the bag that was tossed and a number representing where the bag landed (0=outside of the hole and rings,
1=in the hole, 2=on the yellow ring, 3=on the blue ring, 4=on the green ring), prints the colour and location of the landed bag and determines the points awards for that toss,
as described above
o function printWinner which, given the points awarded to the player, generates the computer's points (between 0 and 34, inclusive) and print the points for each 
as well as the message of who won and by how much, as described above
o the cornhole function itself should allow 4 tosses, relying on the user to enter which colour bag they are tossing each time, 
it should generate the random number for the location of where the bag landed (between 0 and 4, inclusive) and call on the other functions 
to compute the user points for each toss and declare the winner based on the total toss points. Note that you do not need to check that the user has entered 4 unique colours 
each time, you may assume the user will toss all four coloured bags in some order.'''

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
