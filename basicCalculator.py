def calculator_conv():
    """
    This program prompts the user to enter two number and an operator and displays the result
    """
    print("""BASIC PREMIUM CALCULATOR
    This Calculator can Add, Subtract, Multiply, Divide, and Modulus
    Instruction: Use A for addition, S for subtraction, M for Multiplication, D for Divide, R for Modulus
    """)

    try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        opertn = input('Enter operation: ').upper()

        # operations
        operatn1 =  'Add' or 'A'
        operatn2 = 'Subtraction' or 'S'
        operatn3 = 'Multiply' or 'M'
        operatn4 = 'Divide' or 'D'
        operatn5 =  'R'
        
        if opertn == 'A' in operatn1 or opertn == 'S' in operatn2 or opertn == 'M' in operatn3 or opertn == 'D' in operatn4 or opertn == 'R' in operatn5:
            print('Note the order of inputing Values matter.')

            # calculate
            if opertn == 'A':
                calAdd = num1 + num2
                print(f'{num1} + {num2} = {calAdd}')

            elif opertn == 'S':
                calSub = num1 - num2
                print(f'{num1} - {num2} = {calSub}')

            elif opertn == 'M':
                calMul = num1 * num2
                print(f'{num1} * {num2} = {calMul}')

            elif opertn == 'D':
                calDiv = num1 / num2
                print(f'{num1} / {num2} = {calDiv}')

            elif opertn == 'R':
                calMol = num1 % num2
                print(f'{num1} mod {num2} = {calMol}')

            else:
                print('Wrong Operation')

        else:
            print('Invalid operation input')
            
    except:
        print('Oops! Enter a valid number')
    # run program
calculator_conv()