import abc
from .benchmark import OverallPerformanceBenchmark
from .plot import plot

class Comparator(abc.ABC):
    def __init__(self):
        self.benchmark = None

    def compare(self, functions, params):
        res = self.benchmark.run(functions, params)
        plot(res)


class BarChartComparator(Comparator):
    def __init__(self):
        self.benchmark = OverallPerformanceBenchmark()
        