class A:
    def instance_method(self):
        print("metod ob'ekta")
        print("self", self)

obj = A()
obj.instance_method()
# metod ob'ekta
#self <__main__.A object at 0x7fbf10b5baf0>
# kogda my vyzyvem metod u ob'ekta to nam ne nujno peredavat' ego v self,
# on peredaetsya avtomaticheskii

A.instance_method(obj)
# metod ob'ekta
#self <__main__.A object at 0x7fbf10b5baf0>
# kogda my vyzyvaaem metod u klassa to nam nujno peredavat' ob'ekt


class A:
    @classmethod
    def class_method(cls):
        print("metod klassa")
        print("cls", cls)

A.class_method()
# metod klassa
# cls <class '__main__.A'>

obj = A()
obj.class_method()
# metod klassa
# cls <class '__main__.A'>

# vse ravno ot kuda vy budete vyzyvat' classmethod (ot ob'ekta ili klassa)
# pervym argumentom budet prihodit' class


# primery
class C:
    counter = 0
    def __init__(self):
        # ob'ekt sozdaetsya
        # C.counter += 1
        self._inc_counter()
    
    def __del__(self):
        # ob'ekt udalyaetsya
        # C.counter -= 1
        self._dec_counter()

    @classmethod
    def _inc_counter(cls):
        # cls - class C
        # uvelichivaem attribut klassa counter na odin
        cls.counter += 1

    @classmethod
    def _dec_counter(cls):
        cls.counter -= 1


obj1 = C()
obj2 = C()
obj3 = C()
obj4 = C()
print(C.counter) # 4
del obj1
print(C.counter)


class Pizza:
    def __init__(self, radius, *ingredients):
        self.r = radius
        self.ingredients = ingredients

    def cook(self):
        print(f"Pizza razmerom {self.r * 2}")
        print(f"Ingredienty: {self.ingredients}")

    @classmethod
    def four_cheeze(cls, radius):
        pizza = cls(radius, "1 syr", "2 syr", "3 syr", "4 syr")
        # pizza = Pizza(15, "1 syr", "2 syr", "3 syr", "4 syr")
        return pizza

pizza1 = Pizza(15, "Syr", "Kolbasa", "Cherry")
pizza1.cook()

pizza2 = Pizza(10, "1 syr", "2 syr", "3 syr", "4 syr")
pizza2.cook()

pizza3 = Pizza(15, "1 syr", "2 syr", "3 syr", "4 syr")
pizza3.cook()

pizza4 = Pizza.four_cheeze(10)
pizza4.cook()

pizza5 = Pizza.four_cheeze(15)
pizza5.cook()



class A:
    @staticmethod
    def static_method():
        print("statik metod")

obj = A()
obj.static_method()


class Cylinder:
    def __init__(self, diameter, height):
        self.di = diameter
        self.h = height
        self.area = self.get_area(diameter, height)
    
    @staticmethod
    def get_area(di, h):
        from math import pi
        circle_area = pi * di**2 / 4
        side_area = pi * di * h
        return circle_area*2 + side_area
    
cylinder1 = Cylinder(4, 10)
print(cylinder1.area) # 150.79644737231007

print(Cylinder.get_area(4, 10)) # 150.79644737231007
# my ne sozdali ob'ekt, no poluchili nyjnye nam raschety


def get_area_cylinder(di, h):
        from math import pi
        circle_area = pi * di**2 / 4
        side_area = pi * di * h
        return circle_area*2 + side_area

print(get_area_cylinder(4, 10)) # 150.79644737231007
