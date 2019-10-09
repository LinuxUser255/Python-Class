#!/usr/bin/env python3

#python scripting practice
#STRING FORMATING

print("________________________________________________")
print("STRING FORMATTING - DISPLAYING NUMBERS & STRINGS")
print("________________________________________________")


age = 24
print("my age is " + str(age) + " years")

#same as above but with a replacement field of {}. Use case is with multiple variables.
print("my age is {0} years".format(age))

#CURLY BRACKET REPLACEMENT FIELD. A USE-CASE EXAMPLE TO DEAL WITH MULTIPLE PARAMETERS AND DATA/VARS
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31, "Janurary", "March", "May",
      "July", "August", "october", "December"))

#USE OF TRIPLE QUOTES TO DEAL WITH MULTIPLE LINES
print("""Janurary:{2}
feburary: {0}
march: {2}
april: {1}
may:   {2}
june:  {1}
july:  {2}
aug:   {2}
sep:   {1}
oct:   {2}
nov:   {1}
dec:   {2}""".format(28,30,31))

#FORMATTING OPERATOR,(DEPRECATED PYTHON 2 EXAMPLES) % is a modulo operator yielding the remainder from the division of the first argument by the second
print("my age is %d years" % age)
print("my age is %d %s, %d %s" % (age, "years", 6, "months"))

#USE OF A FOR-LOOP,(double astrics indicate raising a number to the power of another). Also, including a number following..
#the % improves formating. In this example %d is for an integer. %s was for a string.
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

#SPECIFY THE PRECISION OF A NUMBER USING A WHOLE NUMBER ONLY, OR A PERCENT, (DECIMAL) FOR ADDED ELABORATION.
#example
print("Pi is approximately %12f" % ( 22 / 7))
#versus
print("Pi is approximately %12.50f" % ( 22 / 7 ))

#USING THE NEW REPLACEMENT FIELD SYNTAX
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

#COLON 2 MEANS AN ALLOCATED WIDTH OF 2, etc..
#When encountering the old format %12f can be replaced by the replacement field format of {0:12.50}".format( 22 / 7))

print("___________________________________")

print("IF PROGRAM FLOW / IF ELSE & ELIF")

print("____________________________________")

#FORMAT CAN BE APPLIED TO ANY STRING
#VARIABLE created: NAME
#ACCEPT THE NAME ENTERED BY THE USER & insert it into the variable "NAME"
#USING A REPLACEMENT FIELD {0} , to FORMAT AND PRINT THE NAME ENTERED
name = input("enter name: ")
age = int(input("how old are you, {0}? ".format(name)))
print(age)

#If Else. Make the computer decide how many years a juvinile must wait until voting elidgeability.
#Accomplish this by using a replacement field $ dot format {0}.format
#If the condition is true, then no response, else the person mus wait X no. of Yrs.
if age >= 18:
    print("you are old enough to vote")
else:
    print("Return in {0} years".format(18 - age))

#if age >= 18:
#   print("you are old enough to vote")

print("_________________________________")

print(" Guessing Game with IF, ELSE, ELIF")
print(" == means equal to. & != meand not equal to")
print("________________________________")

print("Guess a number between 1 and 100: ")
guess = int(input())

if guess < 100:
    print("Guess higher")
    guess = int(input())
    if guess == 100:
        print("congrats!")
    else:
        print("try again")
elif guess > 100:
    print("Guess lower")
    guess = int(input())
    if guess == 100:
        print("congrats! that is correct.")
    else:
        print("try again")
else:
     print("first try correct")

#if age >= 18:
#    print("you are old enough to vote")

print("__________________________________")

print("CONDITIONALS - Itermediate")


print("_________________________________")

#int(input() converts variable to a number
age = int(input("your age? "))

#The ( ) ( ) parenthesis and or [] [] Brackets in conditionals are not necessaary for functionality, but,
#makes the code more reader friendly and obvious of the developer's intentions.
#When writing conditionals if "and" is used between ( ) and  ( ) both statements must be true to satisfy the condition.
#However, when using "or" ( ) or ( ) then only one of the two statements must be true, and must be follwed with an else:

if (age < 16) or (age > 65):
    print("enjoy it while it lasts") 
else:
    print("have a good day at work")

#Python does not have boolean data type, but it does have tow constants: TRUE and FALSE
#Example: using x as a string. In Python, True is 1 and False is 0.
#But in a condition, any non-zero or non empty values will evaluate to true. 
x = "false"
if x:
    print("x is true")
print("""False: {0} 
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple (): {5}
empty string ' ': {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False,bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(' '), bool(""), bool({})))

#NOT TRUE = FALSE & FALSE = NOT TRUE
print(not False)
print(not True)

print("_________________________________________")

print("ForLoops")

print("________________________________________")

#ForLoops
#A for loop takes a range of values and asssigns them one-by-one to a variable.
#It then executes a block of code once for each value.
#The following for loop retrieves the values of one through 20.
#The last value in is not included
for i in range(1,20):
     print("i is now {}".format(i))

#number = 

