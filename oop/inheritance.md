# Nasledovanie
> Princip OOP, gde my mojem unasledovat', pereopredelyat' i ispol'zovat' vse 
attributy i metody roditel'skogo klassa

```py
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
```

> klass A - roditel'skii
> klass B - dochernii

## Pereopredelenie
> kogda my sozdaem metod ili attribut s takim je nazvaniem kak i v 
roditel'skih klassah

```py
class C(A):
    def method(self):
        print("Metod v klasse C")

obj_c = C()
obj_c.method()
# Metod v klasse C
```

## Vidy nasledovaniya
* **odinochnoe** (kogda odin roditel')
* **mnojestvennoe** (kogda neskol'ko roditelei)
* mnogourovnevoe (kogda u roditelya est' roditel')
* ierarhicheskoe (kogda u kajdogo est' tol'ko odin roditel', no 
u roditelya mojet byt' mnogo detei)
* gibridnoe (sovmeshenie raznyh vidov nasledovaniya)


## Problemy mnojestvennogo nasledovaniya
1. Problema romba (resheniya s pomosh'yu MRO (s versii 2.3))
> MRO - method resolution order (prostraivaet poryadok dlya poiska attributov)

```py
class A:
    pass
class B:
    pass
class C(A,B):
    pass

# do MRO
[C, A, object, C, B, object]

# posle MRO
[C, A, B, object]
```

2. Problema perekrestnogo nasledovaniya (ne reshennaya, voznikaet kogda 
ne vozmojno prostroit' prioritet roditelei)

```py
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
```









