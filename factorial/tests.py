import unittest
import factorial as f
from timer import timed

class TestFactorial(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.data = [0, 1, 2, 3, 4, 5, 6]
        cls.results = [1, 1, 2, 6, 24, 120, 720]

    def test_all_functions_work(self):
        functions = [f.accumulated_factorial, f.recursive_factorial, f.naive_factorial, f.dynamic_factorial]
        
        for function in functions:
            for index, value in enumerate(self.data):
                self.assertEqual(function(value), self.results[index])

class TestTimedAttribute(unittest.TestCase):
  
    
    def test_timed_attribute(self):
        
        def func():
            for i in range(1000):
               pass
            return 7

        seven, time = timed(func())()
        self.assertEqual(seven, 7)
    
    
