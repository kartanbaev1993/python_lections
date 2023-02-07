# создайте список от 1 до 10
# выведите список с числами в обратном порядке
list1 = [1,2,3,4,5,6,7,8,9,10]
list1 = list(range(1,11))
print(list1[::-1])
list1.reverse()
print(list(reversed(list1)))
