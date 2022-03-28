"""
This is sample file to test though the parser.
Sample documentation string () test() Class(Object)
"""
import os
from random import randint
from .file1 import add as addition, sub
from sample_code.package.sub_package.sub_package2.file1 import add as addition, sub
from sample_code.package.sub_package.sub_package2 import file1
from sample_code.package.sub_package.sub_package_file import Parent, View

KEYWORDS = ["tes", "test2"]


class Person(Parent, View):
    """
        Class Person: Doc String
    """
    # init method definition
    def __init__(self, name):
        temp = 'a'
        self.name = name

    # Sample Method
    def say_hi(self):
        print("Hello, my name is ", self.name)

    # Another samlple method
    def say_bye(self):
        print("Hey there! See you! Bye Bye!")

class Person1():
    # init method definition
    """
        Class Person1: Doc String
    """
    def __init__(self, name):
        temp = 'a'
        self.name = name

    # Sample Method
    def say_hi(self):
        print("Hello, my name is ", self.name)

    # Another samlple method
    def say_bye(self):
        print("Hey there! See you! Bye Bye!")

def a():
    num = addition(randint(1, 10), 6)
    print(num)
    pass

def b():
    # a()
    num = addition(5, 6)
    print(num)
    num2 = addition(5, 6)
    print(num2)
    obj = Person('Lokesh')  # init method is called
    obj2 = Person('Lokesh')  # init method is called
    pass


if __name__ == "__main__":
    b()
    obj = Person('Lokesh')   # init method is called
    obj2 = Person('Lokesh')  # init method is called
    p1 = Parent()
    obj.say_hi()             # say_hi() method is called.
    obj.say_bye()            # say_bye() method is called.
    obj.say_hi()             # say_hi() method is called.
    num = addition(5, 6)
    print(num)

