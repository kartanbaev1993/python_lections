class A:
    def method(self):
        print("Metod v klasse A")

obj_a = A()
obj_a.method()
# Metod v klasse A

class B(A):
    pass

obj_b = B()
obj_b.method()
# Metod v klasse A

class C(A):
    def method(self):
        print("Metod v klasse C")

obj_c = C()
obj_c.method()
# Metod v klasse C


class A:
    def method(self):
        print("Metod v klasse A")
        return "AAA"
    
class B(A):
    def method (self):
        print("Metod v klasse B")
        return_from_super = super().method()
        print("super().method() vernul", return_from_super)
        return "BBB"

obj_a = A()
res_a = obj_a.method()
print("A.method vernul", res_a)

obj_b = B()
res_b = obj_b.method()
print("B.method vernul", res_b)


class Range:
    def create(self, n):
        """Prinimaet chislo i vozvrashaet spisok chisel ot 0 do dannogo 
        chisla vklyuchitel'no"""
        return list(range(n+1))

class Range10(Range):
    def create(self):
        """Vozvrashaet spisok chisel ot 0 do 10 vklyuchitel'no"""
        return super().create(10)
    
range_obj = Range()
res = range_obj.create(5)
print(res)
# [0, 1, 2, 3, 4, 5]

range10_obj = Range10()
res = range10_obj.create()
print(res)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class A:
    attr1 = 'a'

    def method(self):
        print("Metod v klasse A")

class B:
    attr2 = 'b'

    def method(self):
        print("Metod v klasse B")

class C(A,B):
    pass

obj_c = C()

print(obj_c.attr1) # 'a'
print(obj_c.attr2) # 'b'
obj_c.method() # Metod v klasse A


print(C.mro())
# [<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>]


# perekrestnoe nasledovanie
class A:
    pass

class B:
    pass

class C(A,B):
    pass

class D(B,A):
    pass

class E(C,D):
    pass
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B