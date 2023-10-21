import unittest
from exceptions.basics import safe_divide, list_element_retrieval, validate_age, InvalidAgeError

class TestBasicExceptions(unittest.TestCase):
    
    def test_safe_divide(self):
        self.assertEqual(safe_divide(10, 2), 5)
        self.assertEqual(safe_divide(10, 0), "Cannot divide by zero!")
        
    def test_list_element_retrieval(self):
        lst = [1, 2, 3]
        self.assertEqual(list_element_retrieval(lst, 1), 2)
        self.assertEqual(list_element_retrieval(lst, 5), "Index out of range!")


class TestCustomExceptions(unittest.TestCase):
    
    def test_validate_age(self):
        # Test a valid age
        age = 20
        result = None
        try:
            validate_age(age)
        except InvalidAgeError:
            result = "Exception raised"
        self.assertIsNone(result)
        
        # Test an invalid age
        age = 150
        with self.assertRaises(InvalidAgeError):
            validate_age(age)
