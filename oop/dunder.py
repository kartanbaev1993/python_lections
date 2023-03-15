# dunder (double underscore) - metody u kotoryx 2 _ v nachale i konce
# magiya v tom chto my ix ne vyzyvaem napryamuyu

class A:
    def __new__(cls):
        print("__NEW__")
        return super().__new__(cls)
    
    def __init__(self):
        print("__INIT__")
        pass


A()
# __NEW__
# __INIT__

# __new__, __init__ - vyzyvayutsya pri sozdanii ob'ekta



# __eq__ ==
# __ge__ >=
# __gt__ >
# __le__ <=
# __lt__ <
# __ne__ !=
# __add__ +
# __sub__ -
# __floordiv__ /
# __truediv__ //


class A:
    pass
# __str__ str, print
print(A()) # <__main__.A object at 0x7f91a0357d00>

class A:
    def __str__(self) -> str:
        return "Hello"

print(A()) # Hello


class A:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number == other.number

obj1 = A(5)
obj2 = A(5)

print(obj1 == obj2)
print(obj1.__eq__(obj2))

          