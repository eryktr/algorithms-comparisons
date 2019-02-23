from algorithms_comparisons.analysis.compare import BarChartComparator, PerformanceChartComparator
from algorithms_comparisons.fibonacci import fibonacci

def compare_fibonacci_barchart():
    comparator = BarChartComparator()
    functions = [fibonacci.dynamic_fibonacci, fibonacci.matrix_fibonacci, fibonacci.recursive_fibonacci]
    params = [i for i in range(1, 20)]
    comparator.compare(functions, params)

def compare_fibonacci_performancechart():
    comparator = PerformanceChartComparator()
    functions = [fibonacci.dynamic_fibonacci, fibonacci.matrix_fibonacci]
    parameters = [i for i in range(2000)]
    comparator.compare(functions, parameters)

if __name__ == "__main__":
    compare_fibonacci_barchart()
    compare_fibonacci_performancechart()