from base_converter import to_base_10, from_base_10

def convert_to_10():
    x = input("Enter number in base other than 10: ")
    x_base = input("Enter the base of x: ")
    x_con = to_base_10(x, x_base)
    return x_con


def convert_from_10():
    x = input("Enter number in base 10: ")
    x_base = input("Enter the base you want to convert to: ")
    x_con = from_base_10(int(x), int(x_base))
    return x_con


def add_base():
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    x_base = input("Enter the base of first number: ")
    y_base = input("Enter the base of second number: ")
    z_base = input("Enter base you want to get the sum in: ")
    x_con = to_base_10(x, x_base)
    y_con = to_base_10(y, y_base)
    
    sum = x_con + y_con
    sum_con = from_base_10(int(sum), int(z_base))
    
    
def subtract_base():
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    x_base = input("Enter the base of first number: ")
    y_base = input("Enter the base of second number: ")
    z_base = input("Enter base you want to get the difference in: ")
    x_con = to_base_10(x, x_base)
    y_con = to_base_10(y, y_base)
    
    if y_con > x_con:
        print("First number ",x, "is less than second number ", y)
    else:
        sub = x_con - y_con
        sub_con = from_base_10(int(sub), int(z_base))
        
        
def multiply_base():
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    x_base = input("Enter the base of first number: ")
    y_base = input("Enter the base of second number: ")
    z_base = input("Enter base you want to get the product in: ")
    x_con = to_base_10(x, x_base)
    y_con = to_base_10(y, y_base)
    
    product = x_con * y_con
    product_con = from_base_10(int(product), int(z_base))
    
    
def divide_base():
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    x_base = input("Enter the base of first number: ")
    y_base = input("Enter the base of second number: ")
    z_base = input("Enter base you want to get the division in: ")
    x_con = to_base_10(x, x_base)
    y_con = to_base_10(y, y_base)
    
    div = x_con / y_con
    div_con = from_base_10(int(div), int(z_base))
    quo = x_con // y_con
    rem = x_con % y_con
    quo_con = from_base_10(int(quo), int(z_base))
    rem_con = from_base_10(int(rem), int(z_base))
    #print("quotient = ", x_con // y_con)
    #print("remainder = ",x_con % y_con)
    print("quotient = ", quo_con)
    print("remainder = ", rem_con)

#add_base()
#subtract_base()
#multiply_base()
#divide_base()
#print(convert_to_10())
print(convert_from_10())