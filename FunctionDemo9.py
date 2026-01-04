# One function can call another function 

def fun():
    print("Inside fun")

def gun():
    print("Inside gun")

def main():
    fun()
    gun()
    
if __name__ == "__main__" :
    main()