# Polimorfizm
> princip OOP, v kotorom metody v raznyx klassah nazyvayutsya 
odinakovo. (odin interfeis - raznaya realizaciya)

```py
class Dog:
    def speak(self):
        print("gav-gav")

class Cat:
    def speak(self):
        print("meow-meow")


class Frog:
    def speak(self):
        print("kva-kva")

animals = [Cat(), Frog(), Dog(), Cat(), Dog(), Frog()]
for animal in animals:
    animal.speak()
```