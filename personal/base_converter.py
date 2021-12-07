from math import log

#num1 = input("Enter number: ")
#base1 = input("Enter the base of the number: ")

def to_base_10(num1, base1):
    x = int(num1, int(base1))
    print("Value of ", num1, "from base",base1, "to base 10 = ", x)
    return x
    
#to_base_10(num1, base1)


#num = int(input("Enter number: "))
#base = int(input("Enter the base you want to convert to : "))

def from_base_10(num, base):
    numToChar = {i: "0123456789ABCDEF"[i] for i in range(16)}
    
    # set power to largest
    power = int(log(num, base))
    
    # convert numbers
    converted = ""
    for pow in range(power, -1, -1):
        #divide
        converted += numToChar[num // (base ** pow)]
        #remainder
        num %= base ** pow
    print(converted)
    return converted
    
    
#from_base_10(num, base)
    