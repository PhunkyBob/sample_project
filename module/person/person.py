# -*- coding: utf-8 -*-
# Relative imports.
from .address import Address
from ..tools import tool_function

from typing import Optional

THIS_IS_A_CONSTANT = "This is a constant"


class Person:
    name: str
    age: Optional[int]
    address: Optional[Address]

    def __init__(self, name, age: int = None, address: Address = None):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"{self.name} ({self.age}) : {self.address}"

    @staticmethod
    def static_method_true():
        print("This is a static method")
        tool_function()
        return True

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")
