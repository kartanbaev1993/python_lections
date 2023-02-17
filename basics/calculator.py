from decimal import Decimal
try:
    num1 = Decimal(input('Введите первое число: '))
    num2 = Decimal(input('Введите второе число: '))
except:
    print('Вы ввели не число')
else:
    znak = input('Выберите операцию из следующих (+ - * / %  //)  : ')
    if znak == '+':
        a = num1 + num2
        print(f'Ответ: {a}')
    elif znak == '-':
        a = num1 - num2
        print(f'Ответ: {a}')
    elif znak == '*':
        a = num1 * num2
        print(f'Ответ: {a}')
    elif znak == '/':
        try:
            a = num1 / num2
            print(f'Ответ: {a}')
        except ZeroDivisionError:
            print("Нельзя делить на 0")
    elif znak == '//':
        try:
            a = num1 // num2
            print(f'Ответ: {a}')
        except ZeroDivisionError:
            print("Нельзя делить на 0")
    elif znak == '%':
        a = num1 % num2
        print(f'Ответ: {a}')
    elif znak == '':
        a = num1 ** num2
        print(f'Ответ: {a}')
    else:
        print('Ответ: Данной операции нет в системе')