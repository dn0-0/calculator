def calculate():

    num1 = int(input('first number'))
    operator = input('+,-,/,*')
    num2 = int(input('second number'))

    result = 0

    try:
        match operator:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '/':
                result = num1 / num2
            case '*':
                result = num1 * num2
    except:
        print('something is wrong')
    
    return result

print(calculate())