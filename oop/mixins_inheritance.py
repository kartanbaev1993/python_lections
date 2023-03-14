"""
1 Миксины - классы, которые будут использоваться для наследования.
Но от миксинов не создаются объекты
2 Миксины - классы-примеси, которые служат для
расширения функционала класса
"""
# От миксинов нельзя создавать объекты,
# поскольку миксины - несамостоятельные классы

# При наследовании миксины должны идти в первую очередь

class WalkMixin:
    def walk(self):
        print('я могу ходить')

class SwimMixin:
    def swim(self):
        print('я могу плыть')

class FlyMixin:
    def fly(self):
        print('я могу летать')

class Human(WalkMixin, SwimMixin):
    name = 'человек'

    def talk(self):
        print('я могу говорить')

class Fish(SwimMixin):
    name = 'рыба'

class Exocoetidae(SwimMixin, FlyMixin):
    name = 'летучая рыба'

class Duck(WalkMixin, SwimMixin, FlyMixin):
    name = 'утка'


obj = Human()
setattr(obj, 'new_attribute', 'hello world')
# print(dir(obj))
print(obj.name)
print(obj.new_attribute)

# objects = [Human(), Fish(), Exocoetidae(), Duck()]

# for obj in objects:
#     # print(obj.name)

#     attrs = ['fly', 'swim', 'walk', 'talk']
#     for attr in attrs:
#         if hasattr(obj, attr):
#             method = getattr(obj, attr)
#             method()

# print(hasattr(obj, 'fly')) -> True
# method = getattr(obj, 'walk')
# method()


# obj.fly()
# obj.swim()
# obj.walk()

# hasattr - funkciya kotoraya prinimaet ob'ekt i nazvanie attributa.
# Vozvrashaet True, esli u ob'ekta est' takoi attribut (metod)

# getattr - funkciya kotoraya prinimaet ob'ekt i nazvanie attributa.
# Vozvrashaet znachenie attributa

# setattr - funkciya kotoraya prinimaet ob'ekt, nazvanie attributa 
# i znachenie attributa. Dobavlyaet v ob'ekt navyi attribut 
# ili perezapishet odnoimennyi attribut