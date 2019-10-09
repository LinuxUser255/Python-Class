#!/usr/bin/env python3

print("###################")
print("For Loops")
print("###################")

#For Loops
#Take range of values and assigns them one by one to a variable.
#It then executes a block of code once for each value
#the loop below retrieves the values of 1 through 20.

for i in range(1,20):
    print("i is now {}".format(i))

number = "9,223,372,036,854,775,807"
for i in range(0, len(number)):
    print(number[i])

#Print ONLY the numbers. Exclude punctiation etc.
#Convert from a string and build up a number in the string..
#then convert the string back to an integer.

number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
       cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)

print("The number is {} ".format(newNumber)) 
       

print("########################################")
print("Extending For Loops")
print("#########################################")

#For loop with a step of 5
for i in range(0, 100, 5):
    print("i is {} ".format(i))

#Nested for loop    
for i in range(1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i, j, i*j))
    print("=================")




