import math

#accept inputs 
nickname=str(input("Enter the engineer's nickname: ")) 
age=int(input("Enter the engineer's age: "))
year_of_service=float(input("Enter engineer's years of service: "))

#computing the sum of age , years of service times 5
sum=(age+year_of_service)*5

#truncating the sum
num=math.trunc(sum)

#reversing the computed sum
str_num=str(num)
rev_str=str_num[::-1]
rev=int(rev_str)

#converting the first and last letter of the nickname
last=nickname[-1].upper()
first=nickname[0].lower()

#concatinating the values
model=first+last+'#'+str(num)+str(rev)+str(num)+str(rev)

#printing our final output
print("The Robotdoc has model number: ",model)

