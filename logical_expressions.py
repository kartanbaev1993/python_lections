"===============Логические выражения================"

"равенство"
# print(5 == 5) -> True
# print(4 == 5) -> False

"не равенство"
# print(4 != 5) -> True
# print(5 != 5) -> False

"больше"
# print(5 > 4) -> True
# print(5 > 5) -> False

"меньше"
# print(5 < 10) -> True
# print(5 < 4) -> False
# print(5 < 5) -> False

"больше или равно"
# print(5 >= 10) -> False
# print(10 >= 5) -> True

"меньше или равно"
# print(10 <= 5) -> False
# print(5 <= 10) -> True
# print(5 <= 5) -> True

# print('5' == 5) -> False
# print('Hello' == 'hello') -> False
# print('hello' == 'hello') -> True

"========= AND и OR и NOT =========="
# and - и
# or - или
# not - не

# a = 5
# b = 6

# print(a == 5 and b == 6) -> True
# print(a == 4 and b == 6) -> False

# print(a == 5 or b == 4) -> True
# print(a == 3 or b == 4) -> False

# print(not a == 5) -> False
# print(not b == 4) -> True

# print(not b == 4 and a == 5) -> True
# print(not b == 4 and not a == 5) -> False
# print(not b == 4 or not a == 5) -> True


"=========Boolean Type========="
# bool -> 1)True 2)False

# print(bool(1)) -> True
# print(bool(-1)) -> True
# print(bool(0)) -> False

# print(bool('hello')) -> True
# print(bool(' ')) -> True
# print(bool('')) -> False

# print(bool([])) -> False
# print(bool([[]])) -> True

"===============None Type=============="
# print(bool(None)) -> False
# print(bool('None')) -> True


"========Условные операторы========="

if условие1:
    тело1
    # тело1 будет выполняться только если условие1 верное

if условие1:
    тело1
    # тело1 будет выполняться только если условие1 верное
else:
    тело2
    # тело2 будет выполняться во всех других случаях

if условие1:
    тело1
    # тело1 будет выполняться только если условие1 верное
elif условие2:
    тело2
    # тело2 будет выполняться только если условие1 не верное и если условие2 верное

if условие1:
    тело1
    # тело1 будет выполняться только если условие1 верное
elif условие2:
    тело2
    # тело2 будет выполняться только если условие1 не верное и если условие2 верное
else:
    тело3
    # тело3 будет выполняться только если все вышеуказанные условия не верные


# в одной конструкции мы можем использовать только один if
# в одной конструкции мы можем использовать неограниченное количество elif или не использовать вообще
# в одной конструкции мы можем использовать только один else или не использовать вообще


# value = int(input('Enter your score '))

# if value > 90:
#     print('Good job!')
# elif value < 90 and value > 70:
#     print('OK, good!')
# elif value < 70 and value >= 50:
#     print('Not bad but not good')
# else:
#     print('Looser')

# примите число от пользователя
# выведите Fizz, если число кратно 3
# выведите Buzz, если число кратно 5
# выведите FizzBuzz, если число кратно и 3, и 5
# выведите число во всех остальных случаях

# x = int(input('Enter the number '))

# if x % 3 == 0 and x % 5 == 0:
#     print('FizzBuzz')
# elif x % 5 == 0:
#     print('Buzz')
# elif x % 3 == 0:
#     print('Fizz')
# else:
#     print(x)