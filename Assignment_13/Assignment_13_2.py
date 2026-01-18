# A program which accepts radius of a circle and prints area of a circle

def Area(Rad):
    return 3.14 * Rad * Rad

def main():
    Radius = int(input("Enter the radius of a circle : "))

    Ret = Area(Radius)

    print("Area of a Circle is :", Ret)

if __name__ == "__main__":
    main()