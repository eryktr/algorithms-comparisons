import unittest
import algorithms_comparisons.fibonacci.fibonacci as f
class FibonacciTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.args = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        cls.results = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    def test_if_all_algorithms_work(self):
        functions = [f.recursive_fibonacci, f.dynamic_fibonacci]
        for function in functions:
            for index, arg in enumerate(self.args):
                self.assertEqual(function(arg), self.results[index])
    