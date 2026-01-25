def IsPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def ListPrime(Values):
    Sum = 0
    for i in Values:
        if IsPrime(i):
            print(i)
            Sum = Sum + i
    return Sum