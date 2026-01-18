# A program which accepts one number and checks whether it is palindrome or not

def ChkPalindrome(Value):
    Digit = 0
    ReverseNo = 0
    Temp = Value

    while(Value != 0):
        Digit = Value % 10
        ReverseNo = ReverseNo * 10 + Digit
        Value = Value//10   
            
    return Temp == ReverseNo
        

def main():
    No = int(input("Enter number : "))

    Ret = ChkPalindrome(No)
    if(Ret == True):
        print("Palindrome")
    else:
        print("Not a Palindrome")

if __name__ == "__main__":
    main()