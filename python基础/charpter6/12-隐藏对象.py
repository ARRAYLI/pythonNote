#!/usr/bin/env python
# coding=utf-8

class Dog:
    
    def set_age(self,age):
        if age >0 and age <= 100:
            self.age = age
        else:
            self.age = 0
    
    def get_age(self):
        return self.age

dog = Dog()

dog.set_age(-10)
age = dog.get_age()
print(dog.age)


#dog.get_age()
#dog.get_name()
