'''
Created on Jun 30, 2017

@author: jwang02
'''


# n = int(raw_input("Please enter a number: "))
# print n

while True:
    try:
        n = raw_input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print "Great, you successfully entered an integer!"