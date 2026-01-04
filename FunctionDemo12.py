# nested functions definitions
# error

def Phoenix():
    print("Inside Phoenix mall")

    def zara():
        print("Inside Zara shop")

def main():
    Phoenix.zara()
    
if __name__ == "__main__" :
    main()