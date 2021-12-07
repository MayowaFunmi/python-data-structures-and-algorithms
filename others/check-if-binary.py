check_number = input("Enter Number: ")
def validate_bin(check_number):
    '''
    function that checks if the input consists of either 0 or 1.
    Binary numbers can only be 0 or 1, so we need to validate this
    before doing any math on it.
    returns: True/False
    '''
    check_list = [int(item) for item in (sorted(set(list(str(check_number)))))]
    print(check_list)
    for number in check_list:
        print (f'checking {number} - {type(number)}')
        if number not in [0,1]:
            print (f'invalid binary number')
            return False
    return True
    
print(validate_bin(check_number))
    