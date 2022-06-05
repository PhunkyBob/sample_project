from context import module

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

"""Test adress comparison"""
def test_adress_comparison():
    address_1 = module.person.Address("street", "city", "zipcode")
    address_2 = module.person.Address("street", "city", "zipcode")
    assert address_1 == address_2

"""Test person comparison"""
def test_person_comparison():
    person_1 = module.person.Person("John", 30)
    person_2 = module.person.Person("John", 30)
    assert person_1 != person_2

"""Test static method"""
def test_static_method():
    assert module.person.Person.static_method_true() == True