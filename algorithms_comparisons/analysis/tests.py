import unittest
from .benchmark import benchmark

class BenchmarkTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        def fun1(x):
            return x*x
        def fun2(x):
            return x*x*x
        def fun3(x):
            return x*x*x*x
        cls.functions = [fun1,fun2,fun3]
        cls.arguments = [i for i in range(200)]
    
    def test_benchmark_works(self):
        res = benchmark(self.functions, self.arguments)
        self.assertEqual(len(res), 3)
        for key in res:
            self.assertGreater(res[key], 0)