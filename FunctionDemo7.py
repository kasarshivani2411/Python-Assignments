# Accept : Multiple parameters
# Return : one value
def Marvellous1(Value1, Value2):                   
    print("Inside Marvellous1 :", Value1, Value2)
    return 11

def main() :
    Result = None
    Result = Marvellous1("Python", 21)
    print("Returned value is :", Result)

if __name__ == "__main__" :
    main()