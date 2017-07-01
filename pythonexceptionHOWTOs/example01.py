'''
Created on Jun 30, 2017

@author: jwang02
'''
'''
A try statement may have more than one except clause for different exceptions. 
But at most one except clause will be executed.

Our next example shows a try clause, in which we open a file for reading, 
read a line from this file and convert this line into an integer. 
There are at least two possible exceptions:

an IOError
ValueError
Just in case we have an additional unnamed except clause for an unexpected error:

'''
import sys

try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as (errno, strerror):
    print "I/O error({0}): {1}".format(errno, strerror)
except ValueError:
    print "No valid integer in line."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

'''
An except clause may name more than one exception in a tuple of error names, 
as we see in the following example:
'''
try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except (IOError, ValueError):
    print "An I/O error or a ValueError occurred"
except:
    print "An unexpected error occurred"
    raise
