# https://github.com/Jtorresuribe/Lab11-JT-U-RR.git
# Partner 1 Joaquin Torres-Uribe
# Partner 2 Reyhan Rahman
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(5,3),8)
        self.assertEqual(add(4,3),7)





    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2,3),5)
        self.assertEqual(add(5,3),8)
        self.assertEqual(add(4,3),7)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul())

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(8, 2), 4)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            self.div(5, 0)

    def test_logarithm(self):
        # 3 assertions
        self.assertEqual(logarithm(8,2),3)
        self.assertEqual(logarithm(4,2),2)
        self.assertEqual(logarithm(16,2),4)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(2,0)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            logarithm(5, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse())

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
           square_root(4)
        self.assertEqual(square_root())

    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()