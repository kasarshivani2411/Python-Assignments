# program to display Value, Type, Memory address for a variable using appropriate built in functions

print("----------------------Numeric------------------------")
# int
print("--------int-------")
value = 11
print(value)
print(type(value))
print(id(value))

# float
print("--------float-------")
marks = 98.12
print(marks)
print(type(marks))
print(id(marks))

# complex number
print("--------complex number-------")
number = 2+3j
print(number)
print(type(number))
print(id(number))

print("----------------------Text------------------------")
# str
print("--------str-------")
name = "Shivani"
print(name)
print(type(name))
print(id(name))

print("----------------------Boolean------------------------")
# bool
print("--------bool-------")
isFine = True
print(isFine)
print(type(isFine))
print(id(isFine))

print("----------------------Sequence------------------------")
# List
print("--------List-------")
Value1 = [10,20,30,40,10]   
print(Value1[0])
Value1[2] = 35
print(Value1[2])
print(type(Value1))
print(id(Value1))

# Tuple
print("--------Tuple-------")
Value2 = (10,20,30,40,10)
print(Value2[0])
#alue2[2] = 35  
print(Value1[2])
print(type(Value2))
print(id(Value2))

print("----------------------Set------------------------")
# Set
print("--------set-------")
Value3 = {10,20,30,40}
print(type(Value3))
print(id(Value3))

print("----------------------Mapping------------------------")
# Dict
print("--------dict-------")
Data = {"Name": "Rahul", "Age": 25, "City": "Pune", "Marks": 89.90}
print(Data)
print(type(Data))
print(Data["City"])
Data["Age"] = 26
print(Data)
print(type(Data))
print(id(Data))

print("----------------------None Type------------------------")
# None
print("--------None-------")
Info = None
print(Info)
print(type(Info))
print(type(Info))
print(id(Info))

print("----------------------Binary------------------------")
# bytes
print("--------bytes-------")
# Indexed, Ordered, Immutable
Data1 = bytes([65, 97, 98])
print(Data1)
print(type(Data1))
print(Data1[0])
# Data1[0] = 66      # Error
print(type(Data1))
print(id(Data1))

# bytearray
print("--------bytearray-------")
# Indexed, Ordered, Mutable
Data2 = bytearray([65, 97, 98])
print(Data2)
print(type(Data2))
print(Data2[0])
Data2[0] = 66 
print(Data2[0])
print(type(Data2))
print(id(Data2))