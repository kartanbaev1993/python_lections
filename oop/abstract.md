# Abstrakciya
> princip OOP, v kotorom sozdaetsya klass-pustyshka, v kotorom 
ukazyvayutsya nazvaniya metodov, kotorye obyazatel'no nujno realizovat'
pri sozdanii dochernego klassa

> Chtoby realizovat' abstrakciyu, nujno importirovat' abc i naledovat'
ot klassa ABC, a nujnye metody dekoriruem abstractmethod

```py
from abc import ABC, abstractmethod

class AstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass
```