class Animal:
    def sound(self):
        return "I make sounds"

class Giraffe(Animal):
    def sound(self):
        return "Giiiiiiiiiiraffffffffffeeeeeeee"

a = Animal()
print(a.sound())

g = Giraffe()
print(g.sound())

