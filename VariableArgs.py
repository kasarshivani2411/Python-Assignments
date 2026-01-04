def Addition(*No):
    print(No)               
    print(type(No))             # tuple
    print(len(No))       

def main():
    Addition(11, 21, 51, 101, 11)

if __name__ == "__main__":
    main()