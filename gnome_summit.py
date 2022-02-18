'''Dwarf-like earth spirits called gnomes guard underground treasures. 
Zeph the gnome is given charge of the hidden treasure at the top of an icy mountain with an elevation that not easy for a gnome to climb.
Zeph takes the option of a cable car which goes part of the way up the mountain and the rest of the distance to the summit has to be covered by Zeph on foot.
While climbing, Zeph takes little naps after every 30 metres of distance travelled. 
Each time Zeph naps on a patch of ice, he risks sliding back down the mountain by 8 metres during his nap time.
Given the height of the mountain (in metres) and the height of the cable car drop off point (in metres),
calculate the number of attempts Zeph has to make to climb up to the summit. Each time Zeph naps on a particularly icy patch, 
display a message indicating the nap number on which he slides down. Please note that once the climb puts Zeph at the top of the mountain, 
he cannot slide back down anymore. Note: Use the random module and 
the randint function to randomly generate values between 0 and 1 (inclusive) indicating whether Zeph is napping on a very icy patch and is sliding back down (1) or not (0).'''

#random library
import random
#accepting user inputs for height and drop off points
height=int(input("enter the height of the mountain: "))
drop_off_point=int(input("enter car cable drop point"))
#calculating the distance to climb
dist=height-drop_off_point
#conditions to test the requred conditions for zeph
if dist==0:
    print("already at the top.")

trials=1
while dist>0:
    sleep=random.randint(0,1)
    slide=random.randint(0,1)
    
    if sleep ==1 and slide==0:
        dist+=8
        print(f"uh oh! zeph slid during nap number {trials} !")
    else:
        dist-=30
    trials+=1
    # printing the final output
print(f'''
      it took zeph {trials} tries to climb {height-drop_off_point} meters
      from the cable car dropoff point to the summit
      '''
      )
    
