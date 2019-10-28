#8.39

class Animal(object):
    def speak(self):
        print("not all animals can speak you know...")
        
class Mammal(Animal):
    def speak(self):
        print('grrrrr')
        
class Cat(Mammal):
    def speak(self):
        print('Meeow')
        
class Dog(Mammal):
    def speak(self):
        print('wooof')
        
class Primate(Mammal):
    def speak(self):
        print('hoo hoo haa haa')
            
class Hacker(Primate):
    def speak(self):
        print('Hello World!')