def validator(input_number,input_base,output_base):
    if validate_input(input_number) and input_base.isdigit() and output_base.isdigit():

        if int(input_base) == 2:
            if not validate_bin(input_number):
                print ('ERROR: Invalid Binary Number. Must contain 0s or 1s')
                return False

        if input_number.isdigit() and input_number.isalpha():
            if int(input_base) != 16:
                print ('ERROR: Hexadesimal numbers requires base FROM to be 16')
                return False

        if int(input_base) == 1 or int(output_base) == 1:
            print (f'can not convert to or from Base-1')
            return False
        return True