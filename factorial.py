"Testing Factorial"
import unittest
import math


def factorial_func(x):
    'Factorial Function Validation'
    if not x:
        raise TypeError("Invalid Input")
    if x < 0:
        raise ValueError('Only Non Negative')
    return math.factorial(x)


class TestMathFactorial(unittest.TestCase):
    "Class Testing Factorial"

    def test_right_parameter(self):
        "Right Parameter Test"
        input_r = 5
        desired = 120

        self.assertEqual(math.factorial(input_r), desired)
        self.assertEqual(factorial_func(input_r), desired)


    def test_empty_parameter(self):
        "Empty Parameter Test"
        with self.assertRaises(TypeError):
            self.assertEqual(factorial_func(), True)
        with self.assertRaises(TypeError):
            self.assertEqual(factorial_func(''), True)

    def test_negative_parameter(self):
        with self.assertRaises(ValueError) as err:
            factorial_func(-5)


    def test_invalid_parameter(self):
        "Invalid Parameter Test"
        with self.assertRaises(TypeError) as err:
            factorial_func()



if __name__ == '__main__':
    unittest.main()