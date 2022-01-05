"Testing Absolute"
import unittest
import math

def fab(n):
    if not n:
        raise TypeError("Invalid input")
    if not isinstance(n, int):
        raise TypeError("Integer Only")
    return math.fabs(n)


class TestMathFunc(unittest.TestCase):

    def test_right_parameter(self):
        "Right Parameter Testing"
        input_r = -2.22
        desired = 2.22
        self.assertEqual(math.fabs(input_r), desired)


    def test_positive_parameter(self):
        "Positive Number Testing"
        input_r = 2.2
        desired = 2.2
        self.assertEqual(math.fabs(input_r), desired)


    
    def test_wrong_param(self):
        "Wrong Parameter Testing"
        with self.assertRaises(TypeError):
            fab({})
        with self.assertRaises(TypeError):
            fab([])
        with self.assertRaises(TypeError):
            fab("Invalid")




    def test_empty_parameter(self):
        "Empty Parameter Testing"
        with self.assertRaises(TypeError):
            self.assertEqual(fab(), True)
        with self.assertRaises(TypeError):
            self.assertEqual(fab(''), True)




if __name__ == '__main__':
    unittest.main()



