# A program which accepts marks and display grade

def DisplayGrades(Value):
    if(Value >= 75):
        print("Distinction")
    elif(Value >= 60):
        print("First Class")
    elif(Value >= 50):
        print("Second Class")
    elif(Value < 50):
        print("Fail")

def main():
    Marks = int(input("Enter Marks : "))
    
    DisplayGrades(Marks)

if __name__ == "__main__":
    main()