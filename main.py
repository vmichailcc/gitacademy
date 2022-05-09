# list_a = [0,1,2]
# list_b = ['zero', 'one', 'two']
# list_c = ['cero', 'uno', 'dos']
# list_all = list(zip(list_a, list_b, list_c))
# print(list_all)
# for a,b,c in list_all:
#     print(f'{a} is {b} in English and {c} in Spanish.')


class Cat:
    # Class attribute
    cute = "Cat is so cute"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Cat name - {self.name}. It's - {self.age} year. {Cat.cute}")

class MyClass:
    def method(self):
        return 'instance method called', self
    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    @staticmethod
    def staticmethod():
        return 'static method called'


milo = Cat("Milo", 2)
print(milo)
print(Cat.cute)
print(milo.cute)