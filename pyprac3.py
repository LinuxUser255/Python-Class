#!/usr/bin/env python3

#Continue, Break and Else within the For Loop
#The variable in the following code is: what_i_like
#Python variables are case-sensetive

print("------------------------------------------------------------")

hot_cars = ["a ferrari", "a lambo", "an astonmartin", "a bently", "a beamer"]
for item in hot_cars:
    if item == 'ferrari':
         continue

    print("I want to drive " + item)

print("____________________________________")

hot_cars = ["ferrari", "lambo", "astonmartin", "bently", "beamer"]

what_i_like = ''
for item in hot_cars:
    if item == 'lambo':
        what_i_like = item
        break
else:
    print("I'd like to try the aston")

if what_i_like == 'beamer':
    print("Lets's take it to VIR")


