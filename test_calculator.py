# https://github.com/Jtorresuribe/Lab11-JT-U-RR.git
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self): # 3 assertions
        self.assertEqual(self.add(2,3),5)
        self.assertEqual(self.add(5,3),8)
        self.assertEqual(self.add(4,3),7)





    def test_subtract(self): # 3 assertions
        self.assertEqual(self.sub(2,3),5)
        self.assertEqual(self.add(5,3),8)
        self.assertEqual(self.add(4,3),7)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul())

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div())
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            self.div(0, 5)

    def test_logarithm(self):
        # 3 assertions
        self.assertEqual(self.log(8,2),3)
        self.assertEqual(self.log(4,2),2)
        self.assertEqual(self.log(16,2),4)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            self.log(2,0)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            log(0, 5)

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