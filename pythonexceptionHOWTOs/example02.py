'''
Created on Jun 30, 2017

@author: jwang02
'''
'''
So far the try statement had always been paired with except clauses. 
But there is another way to use it as well. The try statement can be followed by a finally clause. 
Finally clauses are called clean-up or termination clauses, 
because they must be executed under all circumstances, i.e. a "finally" clause is always executed regardless 
if an exception occurred in a try block or not. 
A simple example to demonstrate the finally clause:
'''
try:
    x = float(raw_input("Your number: "))
    inverse = 1.0 / x
finally:
    print("There may or may not have been an exception.")
print "The inverse: ", inverse

try:
    x = float(raw_input("Your number: "))
    inverse = 1.0 / x
except ValueError:
    print "You should have given either an int or a float"
except ZeroDivisionError:
    print "Infinity"
finally:
    print("There may or may not have been an exception.")
