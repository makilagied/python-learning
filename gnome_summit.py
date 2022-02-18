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
    