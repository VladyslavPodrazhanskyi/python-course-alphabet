import unittest
import calc


class CalcTest(unittest.TestCase):
    """Calc tests"""

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print('setUpClass')
        print('==========')

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print('tearDownClass')
        print('==========')

    def setUp(self):
        """Set up for test"""
        print(f"Set up for [{self.shortDescription()}]")

    def tearDown(self):
        """Tear down for test"""
        print("Tear down ")

    def test_add(self):
        """test_add"""
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        """test_sub"""
        self.assertEqual(calc.sub(4, 2), 2)

    def test_mul(self):
        """test_mul"""
        self.assertEqual(calc.mul(5, 2), 10)

    def test_div(self):
        """test_div"""
        self.assertEqual(calc.div(8, 4), 2)


if __name__ == '__main__':
    unittest.main()