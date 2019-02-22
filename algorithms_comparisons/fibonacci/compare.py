from algorithms_comparisons.analysis.compare import BarChartComparator
from algorithms_comparisons.fibonacci import fibonacci

def compare_fibonacci():
    comparator = BarChartComparator()
    functions = [fibonacci.dynamic_fibonacci, fibonacci.matrix_fibonacci, fibonacci.recursive_fibonacci]
    params = [i for i in range(1, 20)]
    comparator.compare(functions, params)

if __name__ == "__main__":
    compare_fibonacci()