# Инкапсуляция
> принцип ООП, у которого есть 2 трактовки
1. Все, что нужно для работы класса - лежит в классе
2. Сокрытие данных (ограничение доступа к аттрибутам)

## Виды доступа
1. public (публичный)
2. protected (защищенный) - один underscore в начале
3. private (приватный) - два underscore в начале

> Нужно для разработчиков чтобы не поломали код

> В python инкапсуляция реализовано на уровне соглашения

```py
class A:
    attr1 = 'public'
    _attr2 = 'protected'
    __attr3 = 'private'

print(A.attr1)
print(A._attr2)
# print(A.__attr3)   Такого названия уже не существует
print(A._A__attr3)

# Getters / Setters
> Методы, с помощью которых мы указываем каким образом мы можем получать и изменять какие-то аттрибуты

py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    # Не трогайте, но можно через set_age:

    def set_age(self, new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else:
            raise Exception('Invalid age')

obj = Person('Nastya', 12)
print(obj.name)
print(obj.get_age())
obj.set_age(45)
print(obj.get_age())
obj.set_age(-123)   # Exception: Invalid age

## Property
> декоратор, который превращает метод в аттрибут с декоратором getter, setter, deleter

> setter будет вызываться, когда мы записываем в аттрибут значение
> deleter будет вызываться, когда мы удаляем аттрибут через del

py
class A:
    @property
    def Hello(self):
        return 5

    # После @property функция становится аттриб-ом, у которого появ-ся setter, getter, deleter

    # property.setter работает когда мы пишем obj.attr = ...
    @Hello.setter
    def Hello(self, new_value):
        print('setter')

    # property.deleter работает когда мы пишем del obj.attr
    @Hello.deleter
    def Hello(self):
        print('deleter')

obj = A()
print(obj.Hello)  # 5
obj.Hello = 'new value' # setter
del obj.Hello # deleter

py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else:
            raise Exception('Invalid age')
    
    @age.deleter
    def age(self):
        if self.__age < 100:
            raise Exception('Cannot delete age')
        del self.__age

obj = Person('Nastya', 12)
print(obj.age)
obj.age = 34
print(obj.age) # 34
obj.age = -100 # Exeption: Invalid age
del obj.age # Exeption: Cannot delete age
obj.age = 115
del obj.age

```