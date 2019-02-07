_author_ = 'dev'
age = 24
print("My age is " + str(age) + " years")

# The following format {0} is usefull with multiple parameters and alot of data.
# And the .format(age)) goes into the {0} replacement field of zero.
print("My age is {0}  years".format(age))

# Here is a demo of The REPLACEMENT FIELD SYNTAX. Using the {0} template.
# Much more efficient than the str(0) template
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31, "January", "March", "May", "July", "August", "October", "December"))

# Use of """Triple Quotes""" to deal with data on multiple lines. And multiple reuse of a replacement field {0}
print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

# The String Formating Operator. (has been depricated in Python 3. But used in Py2).
# The %d was replaced by integer
print("My age is %d years"% age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

#Use of "The For Loop"
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

#Specify the precision of a number by
print("Pi is approximately %12f" % (22 / 7))

#And by adding a decimal palce will result in even greater precsion/detail 12.50f vs just 12f
#The 12.50f assigns 50 decimal points
print("Pi is approximately {0:12.50f}".format(22 / 7))

# New Replacement Fields Syntax Cont’d
#for i in range(1, 12):
#print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
# colon 2 {0:2} allocates width of 2, colon 4 {1:4} allocates width of 4 and so on..

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print('using less-than < to align nubers on the left {1:<4}')

for i in range(1, 12):
        print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))











