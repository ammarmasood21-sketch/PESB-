cart = ["milk", "Bread", "Eggs"] #variable   #[] brackets are used for list
print(cart)
cart.append("Juice") #add a letter in the end of list
print(cart)
cart.insert(1, "butter") #add juice after 0 then on 1 see butter
print(cart)
cart.pop(2) #0, 1 then on 2 The Bread will be removed
print(cart)
cart.remove("milk") #milk will be remove
print(cart)


#Understanding of copy

a = [10,20,30,40,]

b=a  #Perform as a. if changes take place will affect b

c=a.copy() #in copy if a is changed c will not be affected.

print(a)
print(b)
print(c)

a.append(50) #added integer
print(a) #changes affected as it is the main list
print(b) #changes will take place as b is the same list of a
print(c) #copy it will stay as it was saved 


#table of 7

table = [7 * x for x in range(1, 11)] #1 to 10 will be used as 11 will not be counted. ends at 10
print(table)
#value of x will be 1
#then x will be 2 
#then till 10 x will take values from sub list and multiple with 7


#tuples

student = (101, "Ammar", 85) #tuple
print(student)

roll_no,name,marks=student         #unpacking of tuple
print(f"Roll Number: {roll_no}")  #first integer in tuple will be unpacked as roll_no
print(f"My name is {name}")  #Then second string will be introduced as string
print(f"student marks: {marks}") #tells the marks

#f is used for formatting 

