# -*- coding: utf-8 -*-
from dataclasses import dataclass

@dataclass(eq=True)
class Address:
    street: str
    city: str
    zipcode: str
    
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

    def __str__(self):
        return f"{self.street}, {self.zipcode} {self.city}"