import sys
from os.path import dirname, realpath

parent_dir = dirname(dirname(realpath(__file__)))
sys.path.append(parent_dir)

from operatorasm import Operator
from exceptions import InputException, OutOfRangeException
import unittest

class TestAdd(unittest.TestCase):
    """
    Test the add function from the operatorasm library
    """

    # Validation Testing
    def test_add_integers(self):
        self.assertEqual(Operator.add(1, 2), 3)
        self.assertEqual(Operator.add(4, -5), -1)
        self.assertNotEqual(Operator.add(4, 5), 6)

    # Defect Testing - floats
    def test_add_floats(self):
        self.assertRaises(InputException, Operator.add, 10.5, 2)

    # Defect Testing - strings
    def test_add_strings(self):
        self.assertRaises(InputException, Operator.add, 'abc', 'def')

class TestSub(unittest.TestCase):
    """
    Test the sub function from the operatorasm library
    """

    # Validation Testing
    def test_sub_integers(self):
        self.assertEqual(Operator.sub(3, 2), 1)
        self.assertEqual(Operator.sub(4, -5), 9)
        self.assertNotEqual(Operator.sub(19, 5), 10)

    # Defect Testing - floats
    def test_sub_floats(self):
        self.assertRaises(InputException, Operator.sub, 10.5, 2)
    
    # Defect Testing - strings
    def test_sub_strings(self):
        self.assertRaises(InputException, Operator.sub, 'abc', 'def')

class TestMul(unittest.TestCase):
    """
    Test the mul function from the operatorasm library
    """

    # Validation Testing
    def test_mul_integers(self):
        self.assertEqual(Operator.mul(3, 2), 6)
        self.assertEqual(Operator.mul(4, -5), -20)
        self.assertNotEqual(Operator.mul(4, 5), 6)

    # Defect Testing - floats
    def test_mul_floats(self):
        self.assertRaises(InputException, Operator.mul, 10.5, 2)
    
    # Defect Testing -- strings
    def test_mul_strings(self):
        self.assertRaises(InputException, Operator.mul, 'abc', 'def')

class TestFact(unittest.TestCase):
    """
    Test the factorial function from the operatorasm library
    """

    # Validation Testing
    def test_mul_integer(self):
        self.assertEqual(Operator.factorial(3), 6)
        self.assertEqual(Operator.factorial(0), 1)

    # Defect Testing - negative
    def test_factorial_strings(self):
        self.assertEqual(OutOfRangeException, Operator.factorial, -1)

    # Defect Testing - float
    def test_factorial_floats(self):
        self.assertRaises(InputException, Operator.factorial, 10.5)

    # Defect Testing -- string
    def test_factorial_strings(self):
        self.assertRaises(InputException, Operator.factorial, 'abc')

if __name__ == '__main__':
    unittest.main()