import time
input_number = input("Enter number: ")
def validate_input(input_number):
    start = time.time()
    
    '''
    function that checks if the input consists of legal characters.
    Binary numbers can only be 0 or 1, so we need to validate this
    before doing any math on it.
    returns: True/False
    '''
    legal_char = '0123456789ABCDEFabcdef'
    for number in input_number:
        if number not in legal_char:
            print("You have inputed an incorrect number...")
            end = time.time()
            print(end - start)
            return False
    print("Your number is ", input_number)
    end = time.time()
    print(end - start)
    return True
print(validate_input(input_number))