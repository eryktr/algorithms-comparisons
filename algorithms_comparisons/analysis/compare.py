import abc
from .benchmark import OverallPerformanceBenchmark, ProblemSizePerformanceBenchmark
from .plot import BarChartPlotter, PerformanceChartPlotter

class Comparator(abc.ABC):
    def __init__(self):
        self.benchmark = None
        self.plotter = None

    def compare(self, functions, params):
        res = self.benchmark.run(functions, params)
        self.plotter.plot(res)

class BarChartComparator(Comparator):
    def __init__(self):
        self.benchmark = OverallPerformanceBenchmark()
        self.plotter = BarChartPlotter()

class PerformanceChartComparator(Comparator):
    def __init__(self):
        self.benchmark = ProblemSizePerformanceBenchmark()
        self.plotter = PerformanceChartPlotter()
        