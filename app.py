num1 = int(input('first number'))
operator = int(input('+,-,/,*'))
num2 = int(input('second number'))

result = 0

try:
    match operator:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 + num2
        case '/':
            result = num1 + num2
        case '*':
            result = num1 + num2
        case _:
            raise Exception
except:
    print('something is wrong')

