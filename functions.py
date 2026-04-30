#Recursive
import time


def factorial(n):
    if n == 1:
        result = 1
    else:
        result = n * factorial(n-1)

    return result
#-----------------------------------------------------------------------
#Decorator
def logtime(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        time_needed = (end - start)
        print (time_needed)
        return result
    return wrapper

@logtime
def hello():
    print("Hello World!")
hello()
#-----------------------------------------------------------------------
#Annotations
def increment(n: int) -> int:   # accepts int and returns int
    return n + 1

count: int = 0
#-----------------------------------------------------------------------
#Exceptions
try:
    result = 2/0
except ZeroDivisionError:
    print("Division by zero not possible")
finally:
    result = 1
print(result)
#-----------------------------------------------------------------------
#Installing Packages (pip)
# How to install and uninstall a package through console
#-----------------------------------------------------------------------
#List Compressions
numbers = [1,2,3,4,5]
numbers_power_2 = [i ** 2 for i in numbers]
print(numbers_power_2)
#-----------------------------------------------------------------------
#Polymorphism
class Dog:
    def eat(self):
        print("Dog is eating")

class Cat:
    def eat(self):
        print("Cat is eating")

animal1 = Dog()
animal2= Cat()

animal1.eat()
animal2.eat()
#-----------------------------------------------------------------------
#Operator Overloading
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

roger = Dog("Roger", 18)
sydney = Dog("Sydney", 16)

print(roger > sydney)