from abc import ABC, abstractmethod

class AstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(AstractAnimal):
    pass

# obj = Dog()
# TypeError: Can't instantiate abstract class Dog with abstract method speak

class Dog(AstractAnimal):
    def speak(self):
        print("gav-gav")
    
obj = Dog()
obj.speak()
