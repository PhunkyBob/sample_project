# -*- coding: utf-8 -*-
from .address import Address

THIS_IS_A_CONSTANT = "This is a constant"

class Person: 
    name: str
    age: int
    address: Address

    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"{self.name} ({self.age}) : {self.address}"

    @staticmethod
    def static_method_true():
        return True

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")