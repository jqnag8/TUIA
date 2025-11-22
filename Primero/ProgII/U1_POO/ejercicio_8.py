class Animal:
    def talk(self):
        return self.speak()

class Mamifero(Animal):
    def speak(self):
        return "Hola, soy Mamifero"

class Felino(Mamifero):
    def speak(self):
        return "Hola, soy Felino"

class Canido(Mamifero):
    def speak(self):
        return "Hola, soy Canido"

class Primate(Mamifero):
    def speak(self):
        return "Hola, soy Primate"

class Hacker(Primate):
    pass
    # def speak(self):
    #     return "Hola, soy Hacker"
