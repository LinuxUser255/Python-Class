#!/usr/bin/env python3
#
import time

# FOR LOOP
for i in range(21):
    time.sleep(0.02)
    print("i incremented by 1 is now {}".format(i))
    
var = 20

# WHILE LOOP
while var > 0:
    time.sleep(0.05)
    print("i add 1 is now {}".format(i))
    var = var -1
    if var == 10:
        break

# FUNCTIONS
def me():
    print("yyyyyyy")

me()

# FUNCTIONS
def pro_lang(language):
    print(f"we learning {language.title()}.")

pro_lang('python functions')


print('''
        ''')

# VARIABLES AND USER INPUT
age = int(input("age: "))

if age < 16:
    print("not allowed to drive")
else:
    if age in range(16, 90):
        print("Yes, you may drive.")
if age >= 90:
    print("Yes, though some restrictions may apply.")
