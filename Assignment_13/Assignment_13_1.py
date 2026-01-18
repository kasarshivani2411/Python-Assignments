# A program which accepts length and width of a rectangle and prints area

def Area(Len, Wid):
    return Len * Wid

def main():
    Length = int(input("Enter the length of a rectangle : "))

    Width = int(input("Enter the width of a rectangle : "))

    Ret = Area(Length, Width)

    print("Area of a rectangle is :", Ret)

if __name__ == "__main__":
    main()