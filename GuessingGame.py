#!/usr/bin/env python3

#While Loop
#Continue looping so long as a condition is true, then stop when it becomes false.

avail_exits = ["east", "north east", "south"]

chosen_exit = ""
while chosen_exit not in avail_exits:
    chosen_exit = input("choose a direction: ")
    if chosen_exit == "quit":
        print("game over")
    break

else:
    print("glad you got out huh?")

print("============================================")

#!/usr/bin/env python3

tries =["A"]
#max number of attempts
max_tries = 5
counter = 1
increment = 1

while len(tries) <= max_tries:
    tries.append("A"*counter)
    counter=counter+increment


import random

highest = 10
answer = random.randint(1, highest)
print("guess a number between 1 & {}: ".format(highest))

guess = 0 #initialize number outside of valid range
while guess != answer:
    guess = int(input())
    if guess < answer:
        print("guess higher")
    elif guess > answer: #guess must be greater than number
        print("guess lower")
    else:
        print("congrats")
    



