class NumberBase:
    input_number = input("Enter Number: ")
    #assert input_number in "0123456789abcdefABCDEF",    "Not accepted"
    def __init__(self):
        pass
        
    def __repr__(self):
        return "Number Base Calculator and Converter"
        
    def validate_input(self):
        num = self.input_number
        
        legal_char = '0123456789ABCDEFabcdef'
        for number in num:
            if number not in legal_char:
                print("You have inputed an incorrect number...")
                return False
        print("Your number is ", num)
        return True
        
    def validate_bin(self):
        num = self.input_number
        check_list = [int(item) for item in (sorted(set(list(str(num)))))]
        print(check_list)

        for number in check_list:
            print (f'checking {number} - {type(number)}')
            if number not in [0,1]:
                print (f'invalid binary number')
                return False
            return True
            
            
    def validator(self):
        num = self.input_number
        input_base = input("Enter the base you are convertinng FROM: ")
        output_base = input("Enter the base you are convertinng TO: ")
        if self.validate_input() and input_base.isdigit() and output_base.isdigit():

            if int(input_base) == 2:
                if not self.validate_bin():
                    print ('ERROR: Invalid Binary Number. Must contain 0s or 1s')
                    return False

            if num.isdigit() and num.isalpha():
                if int(input_base) != 16:
                    print ('ERROR: Hexadesimal numbers requires base FROM to be 16')
                    return False

            if int(input_base) == 1 or int(output_base) == 1:
                print (f'can not convert to or from Base-1')
                return False
            return True
            
            
    def convert_number_system(input_number, input_base, output_base):
        '''
        function that calculates numbers from one base to the other
    returns: int, converted number
    '''

        #list that holds the numbers to output in the end
        self.validator()
        remainder_list = []

        #start value for sum_base_10. All calculations go thorugh base-10.
        sum_base_10 = 0

        #validate_input

        if output_base == 2:
            binary_repr = bin(input_number)
            return (binary_repr[2:])

        # we coulc use python's built in hex(), but it is more fun not to...
        #if output_base == 16:
            #hex_repr = hex(input_number)
            #return hex_repr[2:]

        # we want to convert to base-10 before the actual calculation:
        elif input_base != 10:

            # reverse the string to start calculating from the least significant number
            reversed_input_number = input_number[::-1]

            #check if user typed in letter outside HEX range.
            hex_helper_dict = {'a' : 10 , 'b' : 11 , 'c' : 12 , 'd' : 13 , 'e' : 14 , 'f' : 15}


            for index, number in enumerate(reversed_input_number):
                for key,value in hex_helper_dict.items():
                    if str(number).lower() == key:
                        number = value

                sum_base_10 += (int(number)*(int(input_base)**index))

        # if the number is already in Base-10, we can start the convertion
        elif input_base == 10:
            sum_base_10 = int(input_number)


        # we loop through until we hit 0. When we hit 0, we have our number.
        while sum_base_10 > 0:

            #find number to pass further down the loop
            divided = sum_base_10// int(output_base)

            #find remainder to keep
            remainder_list.append(str(sum_base_10 % int(output_base)))

            # the new value to send to the next iteration
            sum_base_10 = divided


        #fix the list and send a number:
        return_number = ''

        # if the user asked for a Hexadesimal output, we need to convert
        # any number from 10 and up.
        if output_base == 16:
            hex_dict = {10 : 'a' , 11 : 'b' , 12 : 'c' , 13 : 'd' , 14 : 'e' , 15 : 'f'}

            #loop through remainder_list and convert 10+ to letters.
            for index, each in enumerate(remainder_list):
                for key, value in hex_dict.items():
                    if each == str(key):
                        remainder_list[index] = value

        #return the number:
        else:
            for each in remainder_list[::-1]:
                return_number += each

            return (return_number)
        #else:
            #return ('invalid input... Please Try Again')
    
n1 = NumberBase()
n1.validate_input()
try:
    n1.validate_bin()
except:
    print(n1.input_number, "Is not a binary number!!!")
#n1.validator()