class Whale:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swim(self):
        return 'I am swimming'

    def description(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}'.format(self.name, sound)

a = Whale('adrian', 29)
print(a.description())