#im starting my Practice

# _username = "John"  # string variable
# username  = "John"  # string variable
# user_name = "John"  # valid variable name, underscore is allowed

# int = 10  # integer variable
# float = 10.5  # float variable

myName = 'Ammar'
print(myName) #Output Ammar

my_id = 3523
print(my_id) #Output 3523

her_name = "Kitty"
print(her_name) #Output Kitty

print("Hello Ammar")

print ("Ammar is Working on 'Cyber Security' whith full potential")

pi = 3.14
print(pi, type(pi))

complexnum = 6+5j
print(complexnum, type(complexnum))

a,b,c = 5, 10, 5
a = b = c = 5
print(a, b, c) #Output 5 5 5 

myName = 'Ammar Masood'
Myname = 'Hamza Masood'
print(myName) #Output Ammar Masood
print(Myname) #Output Hamza Masood

#End of Variables

#Start of typecasting
a = "10" #String
b = "5" #String

print(a+b) #Output will be 105 as this will be condsidered as string

a = int(a) #Convert String into Integer
b = int(b) #Convert String into Integer
print(a+b)

pi = 3.14
print(pi, type(pi)) #Output Class Float
number1 = int(pi)
print(number1, type(number1)) #Output Class Integer

id = 30
print(float(id)) #Output is 30.0
print(type(id)) #Output is integer

complexnumm = 5+7j
print(complexnumm, type(complexnumm)) #Output is complex
number3 = int(complexnumm.real) #Out put will be in Integer as 5 is Real number without any alphabet
print(number3,type(number3)) #Output is integer

newadd = str(number3)
print(newadd, type(newadd)) #Convert int into str (5 class 'str')

#This is a string

txt = 'Caterpillar'
print(txt)

print(txt[0]) #string indexing
print(txt[-1]) #length
print(txt[-3]) #length
print(txt[3]) #length

print("hello \"Ammar\" World") # \ Escape Character Treat it as normal "" will be ignored in string
print("Hello\nWorld") #It is used to start a New line 
print("\n Ammar is coming Home") #It is used print Acutual Characters in the String
print("Hello\tWorld") #\t is used to add a space

#List making and testing

students = ["Ammar", "Hassan", "Sohail", "Qais", "Ammad", "Saad"]
print(students)

print(len(students)) #tells the Length
print(students[0]) #0 is the index tell the first word.

students.append("Ali") #Add from last in the list
print(students)

students.insert(2, "Awais") #Telling the specific location to place
print(students)

students.pop(0) #Remove the first Character
print(students)

students.pop() #Remove the last character
print(students)

students.pop(3) #Remove the specfied character
print(students)

# students.clear() #Clear all from list
# print(students)

#random

import random

num= random.randint(20,50) #Select the random
print(num)

luckyStudent = random.choice(students) #Select the random Student name
print(luckyStudent)

name = "My name is Ammar im Working on my Assignment"

print(name.upper())  #All words will be capital alphabets
print(name.lower())  #All words will be in small alphabets
print(name.capitalize()) #only first word of line will be capital
print(name.title()) #All first words of the line get Capital
print(name.split(" ")) #All words are split and become list


Myname = "Ammar"
age = 26
print(f"I'm a Pakistani citizen. {Myname} is my name and my age is {age}.") #f Telling to add variables in string

para = """
lets walk through the horror way in life once.
Which will tell the cost of living.
So Everyone must forget the fear of dieing
"""
print(para) #Multiline text

pick = "let eat missing mangoes slices in dreams"
print(pick[1]) #pick index 1 after first index 0
print(pick[4:24]) #pick from 4 to 24
print(pick[-6:]) #tell -1 -2 -3 -4 -5 -6
print(pick.replace("in dreams", "From My Fridge")) #Replaces the words 
print(pick.find("missing")) #Tell the start position from 0 index to 8 the m starts 8 index
print(pick.count("slices")) #It counts how many time word is repeated or simply displayed one time.


email = "ammar@gmail.com"
print(email.find("@")) # tell the location on index from 0

massage = "Ammar is working on Assignment, So Ammar can submit it again."
print(massage.count("Ammar")) #counts Ammar as it is repeated total counts 2