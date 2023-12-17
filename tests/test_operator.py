import sys
from os.path import dirname, realpath

parent_dir = dirname(dirname(realpath(__file__)))
sys.path.append(parent_dir)

from operatorasm import Operator
from exceptions import NotIntegerException
import unittest

class TestAdd(unittest.TestCase):
    """
    Test the add function from the operatorasm library
    """


    # Validation Testing
    def test_add_integers(self):
        self.assertEqual(Operator.add(1, 2), 3)
        self.assertNotEqual(Operator.add(4, 5), 6)

    # Defect Testing
    def test_add_floats(self):
        self.assertRaises(NotIntegerException, Operator.add, 10.5, 2)

    # Defect Testing
    def test_add_strings(self):
        self.assertRaises(NotIntegerException, Operator.add, 'abc', 'def')

class TestSub(unittest.TestCase):
    """
    Test the sub function from the operatorasm library
    """

    # Validation Testing
    def test_sub_integers(self):
        self.assertEqual(Operator.sub(3, 2), 1)
        self.assertNotEqual(Operator.sub(19, 5), 10)

    # Defect Testing
    def test_sub_floats(self):
        self.assertRaises(NotIntegerException, Operator.sub, 10.5, 2)
    
    # Defect Testing
    def test_sub_strings(self):
        self.assertRaises(NotIntegerException, Operator.sub, 'abc', 'def')

class TestMul(unittest.TestCase):
    """
    Test the mul function from the operatorasm library
    """

    # Validation Testing
    def test_mul_integers(self):
        self.assertEqual(Operator.mul(3, 2), 6)
        self.assertNotEqual(Operator.add(4, 5), 6)

    # Defect Testing
    def test_mul_floats(self):
        self.assertRaises(NotIntegerException, Operator.mul, 10.5, 2)
    
    # Defect Testing
    def test_mul_strings(self):
        self.assertRaises(NotIntegerException, Operator.mul, 'abc', 'def')
            
if __name__ == '__main__':
    unittest.main()