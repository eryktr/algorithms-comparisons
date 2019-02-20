from .benchmark import benchmark
from .plot import plot

def compare(functions, params):
    res = benchmark(functions, params)
    plot(res)
