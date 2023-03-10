"=============================Comprehensions============================="
# генератор с помощью которого можно создавать последовательность 
# использяу цикл for

list1 = []
for i in range(1, 11):
    list1.append(i)
# list1 = = [1,2,3,4,5,6,7,8,9,10]

list1 = [i for i in range(1,11)]
# print(list1)[1,2,3,4,5,6,7,8,9,10]

# результат for элемент in последовательность 
# результат for элемент in последовательность if фильтр

comprehension = (i for i in  range(1,11))
# print(comprehension)
# < generator object <genexpr> at 0x7f6dfd94e490>
# генератор - итерируемый обьект который не хранит в себе 
# полностью все элементы последовательности а генерирует их когда требуется

print(next(comprehension)) # 1
print(next(comprehension)) # 2
print(next(comprehension)) # 3
# print(next(comprehension)) # StopIteration

# next -  функция которая принимает в себя генератор 
# запрашивает следующий элемент у генератора и возврощает его

comprehension = (i for i in  range(1,4))
print(list(comprehension)) # [1,2,3]
print(list(comprehension)) # [] 

"==============================Синтаксический сахар=============================="
# list comprehension
list_compr = [i for i in 'hello']
# print(list_compr)
# ['h', 'e', 'l', 'l', 'o']

# dict comprehensions
dict_compr = {i: str(i) for i in range(1,11)}
print(dict_compr)
# {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

# фильтр
string = 'HelLo WorlD'
res = [i for i in string if i.islower()]
print(res)
# ['e', 'l', 'o', 'o', 'r', 'l']
res = []
for i in string:
    if i.islower():
        res.append(i)
# ['e', 'l', 'o', 'o', 'r', 'l']


# создать список состоящий из четных чисел от 1 до 10

res[]
for i in range(1,11):
    if i % 2 == 0:
        res.append(i)
print(res)

res = [i for i in range(1,11) if i % 2 == 0]
print(res)

res + [i for i in range(2,11,2)]
print(res)


list1 = (list(range(1,11)))
res = []
for i in list1:
    res.append(i*100)
print(res) # [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

res = [i * 100 for i in range(1,11)]
print(res) # [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

res = ['hello' for i in range(5)]
print(res) # ['hello', 'hello', 'hello', 'hello', 'hello']

users = ['test1', 'test2', 'test3']
res = ['Hello' + name for name in users]
print(res) # ['Hellotest1', 'Hellotest2', 'Hellotest3']

res = [[x for x in range(1, i+1)] for i in range(1, 6)]
print(res) # [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]

res = []
for i in range(1,6):
    inner_list = []
    for x in range(1, i+1):
        inner_list.append(x)
    res.append(inner_list)
print(res) # [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]

list1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
res = [1,2,3,4,5,6,7,8,9,10,11,12]

res = [i for inner_list in list1 for i in inner_list]
# res = []
# for inner_list in list1:
#     for i in inner_list:
#         res.append(i)
print(res)

list1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
res = [i for inner_list in list1 for i in inner_list]
print(res) #[1,2,3,4,5,6,7,8,9,10,11,12]

# [1,2,3,4]
# ['не четное', 'четное', 'не четное', 'четное']

dict1 = {'a':1, 'b':2, 'c':3}
# {1:'a', 2:'b', 3:'c'}
res = {value:key for key,value in dict1.items()}
res = {}
for k,v in dict1.items():
    res.update({v:k})
    # res[v] = k


res = ['четное' if i % 2 == 0 else 'не четное' for i in range(1,7)]
print(res) # ['не четное', 'четное', 'не четное', 'четное', 'не четное', 'четное']

res = {i:[x for x in range(1, i+1)] for i in range(1, 6)}
print(res) # {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}


# set comprehension
set_comp = {x for x in range(10)}
print(set_comp) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

set_comprehension = {x for x in range(10)}
print({1, True, 'hello', 10, 1})
# {1, 'hello', 10}
# 1 == True
# 0 == False