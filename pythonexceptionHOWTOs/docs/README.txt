Exception Handling

An exception is an error that happens during the execution of a program. 
Exceptions are known to non-programmers as instances that do not conform to a general rule. 
The name "exception" in computer science has this meaning as well: 
	It implies that the problem (the exception) doesn't occur frequently, 
	i.e. the exception is the "exception to the rule". 
Exception handling is a construct in some programming languages to handle or deal 
with errors automatically. Many programming languages like C++, Objective-C, PHP, Java, Ruby, Python, 
and many others have built-in support for exception handling.

Error handling is generally resolved by saving the state of execution at the moment the error 
occurred and interrupting the normal flow of the program to execute a special function or piece of code, 
which is known as the exception handler. Depending on the kind of error ("division by zero", 
"file open error" and so on) which had occurred, the error handler can "fix" 
the problem and the program can be continued afterwards with the previously saved data.

Exceptions handling in Python is very similar to Java. The code, which harbours the risk of an exception, 
is embedded in a try block. But whereas in Java exceptions are caught by catch clauses, 
we have statements introduced by an "except" keyword in Python. It's possible to "create custom-made" exceptions: 
With the raise statement it's possible to force a specified exception to occur.