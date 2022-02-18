'''write a python program to solve the following program: Each robot model for a company is designed and created by a single engineer whose nickname is used as the name of their robot; the robot model number is derived using a series of steps. Given the nickname, age (as an integer) and years of service (as a float value) of an engineer, generate the model number for the robot created by that engineer as follows:
• extract the first and the last character from the engineer's nickname and convert the first extracted character to lower case and the last extracted character to upper case to form a string of three characters which includes a # concatenated at the end
• compute the sum of the years of service and age and multiply that sum by 5, then convert it to an integer (by truncation, not rounding)
• generate the complete model number as a string by joining the digits of the sum with the reverse of the digits of the sum and repeating the string thus formed, twice; concatenate this string of digits after the string of three characters described above
Your Python code should ask the user for the require information and compute and display the robot's name and model number.'''


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

