# Predict the output

def fun():
    x = 10
    print(x)


fun()
print(x)            # Error will appear here due to the scope of the variable, as x is the local variable of function fun()