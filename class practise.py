#class practise
'''
class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"hi {self.name} welcome to python")
ayyappan = Person("ayyappan")
ayyappan.talk()

suresh = Person("suresh")
suresh.talk()
'''


#inheritance
'''
class Mammal:
    def myfunc(self):
        print("belongs to mammal")
    def walk(self):
        print('love both dog and cat')


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass
dog =Dog()
dog.myfunc()

cat=Cat()
cat.walk()

'''

class String():

    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = String()

str1.get_String()
