# Program to display data type, memory address and size in bytes of a variable entered by the user

from sys import getsizeof

print("Enter the number/message")
variable = input()

print(variable)
print(type(variable))           # <class 'str'>
print(id(variable))
print(getsizeof(variable))