#!/usr/bin/env python3

# This script includes print statements of the source code that is..
# to be printed to the screen along with the output. 
# This is to aide the user to see how and why the code works.
# ----------------------------------------------------------------------------------------------
# How the {} {} double brackets hold the variables 
# The f" " formats the string, 
# place an f before the " " to insert a vars value into a string
#------------------------------------------------------------------------------------------------
print(60*"-")
#------------------------------------------------------------------------------------------------
print('''Using {} {} to contain pre selected values of variables
        to print out a consolidated function
        
first_name = "peter"
last_name = "gibbons"

full_name = f"{first_name} {last_name}"
print(full_name)
''')

first_name = "peter"
last_name = "gibbons"

full_name = f"{first_name} {last_name}"
print(full_name)

#----------------------------------------------------------------------------------------------
print(60*"-")
#----------------------------------------------------------------------------------------------

print("Lists are repped using [] square brackets the 1st item in a list is 0")   

names = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly']
message = f"The funniest character is {names[0].title()}."

names = print(names[1])
print(message)

#-------------------------------------------------------------------------------------------------
print(61*"-")
#-------------------------------------------------------------------------------------------------
print('''
names = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly']
print(names[0]) #Michael Scott
print(names[2]) #Jim Halpert
print(names[3]) #Pam Beasley
print(names[1]) #Dwight

 ''')        

names = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly']
print(names[0]) #Michael Scott
print(names[2]) #Jim Halpert
print(names[3]) #Pam Beasley
print(names[1]) #Dwight

#---------------------------------------------------------------------------------------------
print(60*"-")
#---------------------------------------------------------------------------------------------
print('''Function example code:

def get_the_office(first, last):
    
    full = f"{first} {last}"
    return full.title()

while True:
    print("\nWho is your favourite character on The Office?")
    f_first = input("First name: ")
    l_last = input("Last name: ")

    formatted_name = get_the_office(f_first, l_last)
    print(f"\nYour favourite character is {formatted_name}.") 
    
    ''')
#-----------------------------------------------------------------------------------------------
print(60*"-")
#-----------------------------------------------------------------------------------------------
def get_the_office(first, last):
    
    full = f"{first} {last}"
    return full.title()

while True:
    print("\nWho is your favourite character on The Office?")
    f_first = input("First name: ")
    l_last = input("Last name: ")

    formatted_name = get_the_office(f_first, l_last)
    print(f"\nYour fav character is {formatted_name}.")
    break

#---------------------------------------------------------------------------------------------
print(60*"-")
#---------------------------------------------------------------------------------------------
names = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly']

print(names[0:3])
#---------------------------------------------------------------------------------------------

for name in names[:2]:
    print(name.title())
    
#---------------------------------------------------------------------------------------------
print(60*"-")
#---------------------------------------------------------------------------------------------
print('''Basic while loop with break:

import time

i = 1

while i > 0
    time.sleep(0.1)
    i += 1
    print(i)
    if == 20:
        break

        ''')
import time

# While Loop
i = 1

while i > 0:
    time.sleep(0.1)
    i += 1
    print(i)
    if i == 20:
        break

("loop break")
#----------------------------------------------------------------------------------------------
print(60*"-")
#----------------------------------------------------------------------------------------------
print(''' i becomes each variable. Four examples.
#This loop retrieves the values of 0 through 26.
#The last value is not included and thus ends on 25.

for i in range(0, 26):    
    time.sleep(0.05)
    print(i)

# Iterate through a range
for i in [1,2,3,4,5,'a','b','c']:
    time.sleep(0.05)
    print(i)

for c in 'password':
    time.sleep(0.05)
    print(c)
#
#Use of the replacement field {}. to format and print i. 
for i in range(1, 25):
    time.sleep(0.05)
    print("i is now {}".format(i))
''')
#-------------------------------------------------------------------------------------------
print(60*"-")
#-------------------------------------------------------------------------------------------
for i in range(0, 26):    
    time.sleep(0.05)
    print(i)

# Iterate through a range
for i in [1,2,3,4,5,'a','b','c']:
    time.sleep(0.05)
    print(i)
for c in 'password':
    time.sleep(0.05)
    print(c)
#
#Use of the replacement field {}. to format and print i. 
for i in range(1, 25):
    time.sleep(0.05)
    print("i is now {}".format(i))

#---------------------------------------------------------------------------------------------
print(60*"-")
#---------------------------------------------------------------------------------------------

# The For Loop
import time
#----------------------------------------------------------------------------------------------
print(60*"-")
#----------------------------------------------------------------------------------------------
print('''This is an example of a try-except-else block when tring to open a file: 
        it will attempt to open a text doccument, read it, and print the contents to the screen''')
print(60*"-")
#----------------------------------------------------------------------------------------------
print('''
try:
    f = open('officespace_cast.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Execution complete closing resources.")
---------------------------------------------------------------------------------------------------''')
#----------------------------------------------------------------------------------------------------- 
names = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly']
message = f"The funniest character is {names[0].title()}."


try:
    f = open('officespace_cast.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Execution complete closing resources.")
                                                    
#---------------------------------------------------------------------------------------------
print(60*"-")
#----------------------------------------------------------------------------------------------
