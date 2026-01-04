# Disfferenec between print() and return

def Display():
    print("Inside Display Function")
    return 11

result = Display()
print(result)              


# print()  is used to print/display the message/output on the screen (default return value is None)
# return will return/give the expected result/value back to the caller (return value based on the result)