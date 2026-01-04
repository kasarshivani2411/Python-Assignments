# nested functions definitions

def Phoenix():
    print("Inside Phoenix mall")

    def zara():
        print("Inside Zara shop")

    zara()

def main():
    Phoenix()
    
if __name__ == "__main__" :
    main()