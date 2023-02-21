"===========================Встроенные функции==========================="
# enumerate

string = 'hello'
enum = enumerate(string)
print(enum)
# <enumerate object at 0x7ff9e9fe5b40>
print(list(enum))
# [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

string = 'world'
enum = enumerate(string, 5)
print(list(enum))
# [(5, 'w'), (6, 'o'), (7, 'r'), (8, 'l'), (9, 'd')]


# дан список с числами умножьте на 2 все числа под 
# нечетным индексом умножьте на 3 все числа индексом кратным 3
list1 = [1,4,78,3,7,0,4,2,7]
for ind in range(len(list1)):
    element = list1[ind]
    if ind % 2: # ind % 2 != 0
        list1[ind] = element * 2
    if ind % 3 == 0: # not ind % 3
        list1[ind] = element * 3
print(list1) 
# [3, 8, 78, 9, 7, 0, 12, 4, 7]



list1 = [1,4,78,3,7,0,4,2,7]
for ind, element in enumerate(list1):
    if ind % 2:
        list1[ind] = element * 2
    if ind % 3 == 0:
        list1[ind] = element * 3
print(list1)
# [3, 8, 78, 9, 7, 0, 12, 4, 7]


# создайте словарь где ключем будет порядковый номер 
# буквы в алфавите а затем буква
# {1:'a', 2:'b', 3:'c', ...}

string = 'abcdef'
enum = enumerate(string, 1)
print(dict(enum))
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}


# zip
list1 = [1,2,3,4,5]
list2 = 'abcdifg'
list3 = [0.5,0.3,0.6]
print(list(zip(list1,list2,list3)))
# [(1, 'a', 0.5), (2, 'b', 0.3), (3, 'c', 0.6)]



"=========================Функция высшего порядка========================="
# это функция которая:
# принимает в аргументы другую функцию
# возвращает функцию
# создает внутри функцию
# вызывает внутри функцию


# map -  в кпринимает в аргументы функцию и итерируемый обьект. 
# возвращает генератор в котором все элементы - результат 
# принимаемой функции в которую передали элементы последовательности

mapped = map(int, ['1', '2', '3'])
print(mapped)
# <map object at 0x7f90c6703f40>
print(list(mapped))
# [1, 2, 3]


# дан список с числами создайте новый список где 
# элементы - число из списка+1

list1 = [1,2,3,4]
def res1(i):
    return i+1
print(list(map(res1, list1)))
# [2, 3, 4, 5]

print(list(map(lambda i: i+1, list1)))
# [2, 3, 4, 5]



# filter - в кпринимает в аргументы функцию и итерируемый обьект. 
# возвращает генератор в котором элементы из последовательности 
# прошедшие фильтр (функция вернула True)


lsit1 = [-3,7,0,34,-23,435,10]
def is_positive(i):
    return i > 0 # (True False)
    # if i > 0:
    #     return True (плохой код)
    # else:
    #     return False
print(list(filter(is_positive, list1)))
# [7, 34, 435, 10]

print(list(filter(lambda i: i>0, list1)))
# [7, 34, 435, 10]
 

# дан список со строками оставьте только те строки которые 
# начинаются с большой буквы

list1 = ['Hello', 'wORLD', 'MAKERS']
print(list(filter(lambda i: i[0].isupper(), list1)))
# ['Hello', 'MAKERS']

def first_is_upper(word):
    first = word[0]
    return first.isupper()
print(list(filter(first_is_upper, list1)))
# ['Hello', 'MAKERS']


# reduce - функция которая импортируется из модуля functools.
# тоже принимает функцию и итерируемый обьект. 
# возвращает 1 результат 

from functools import reduce
list1 = [2,4,6,3,65,8]
def mul(x,y):
    return x*y
res = reduce(mul, list1)
print(res)
# 74880 = 2*4*6*3*65*8


string = 'hello'
print(reduce(lambda x,y: x+'$'+y, string))
# h$e$l$l$o
# x='h', y='e' -> 'h$e'
# x='h$e', y='l' -> 'h$e$l'
# x='h$e$l', y='l' -> 'h$e$l$l'
# x='h$e$l$l', y='o' -> 'h$e$l$l$o'


# вывести самое длинное слово 

string = ['hello', 'world', 'makers', 'bootcamp', 'aaa']
print(reduce(lambda x,y: x if len(x) > len(y) else y, string))
# bootcamp