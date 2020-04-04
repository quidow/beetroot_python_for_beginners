class Animal:

    def talk(self):
        pass


class Dog(Animal):

    def talk(self):
        return "woof woof"


class Cat(Animal):

    def talk(self):
        return "meow"


def animal_talk(a):
    if not isinstance(a, (Dog, Cat)):
        raise TypeError
    print(a.talk())
