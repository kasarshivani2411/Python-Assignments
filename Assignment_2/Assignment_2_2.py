# Difference between a = 10, b = 10 and a = [10], b = [10], Explain using id()

a = 10
b = 10

print(a)
print(type(a))      # int
print(id(a))
print(b)
print(type(b))      # int
print(id(b))        # memory address is same because of same value and it is immutable

a = [10]
b = [10]

print(a)
print(type(a))      # list
print(id(a))
print(b)
print(type(b))      # list
print(id(b))