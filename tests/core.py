# -*- coding: utf-8 -*-
from context import module
import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def test_absolute_truth_and_meaning(self):
        assert True

    """Test adress comparison"""
    def test_adress_comparison(self):
        address_1 = module.person.Address("street", "city", "zipcode")
        address_2 = module.person.Address("street", "city", "zipcode")
        self.assertEqual(address_1, address_2)

    """Test person comparison"""
    def test_person_comparison(self):
        person_1 = module.person.Person("John", 30)
        person_2 = module.person.Person("John", 30)
        self.assertNotEqual(person_1, person_2)

    """Test static method"""
    def test_static_method(self):
        self.assertTrue(module.person.Person.static_method_true())


if __name__ == '__main__':
    unittest.main()