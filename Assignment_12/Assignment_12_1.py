# A program which accepts one character and checks whether it is vowel or consonant

def ChkVowel(Value):
    if(Value == 'a' or Value == 'e' or Value == 'i' or Value == 'o' or Value == 'u' or Value == 'A' or Value == 'E' or Value == 'I' or Value == 'O' or Value == 'U'):
        return True
    else:
        return False

    # return Value.lower() in ['a', 'e', 'i', 'o', 'u']

    # return Value.lower() in "aeiou"
        

def main():
    Data = input("Enter the character/letter : ")
    
    Ret = ChkVowel(Data)

    if(Ret == True):
        print("Vowel")
    else:
        print("Consonant")

if __name__ == "__main__":
    main()