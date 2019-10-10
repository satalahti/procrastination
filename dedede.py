

a = [2, 3, 4, 5, 6, 7, 8, 9, 10]

def isPrime(num):
    #check each number between 2 and num -1
    for divCan in list(range(2, num)):
        #chekc if it divides num?
        if (num % divCan == 0):
            return False
    return True



for num1 in a:
    if isPrime(num1):
        print(str(num1) + " is not a prime")
    else:
        print(str(num1) + " is a prime")


print(isPrime(27))
