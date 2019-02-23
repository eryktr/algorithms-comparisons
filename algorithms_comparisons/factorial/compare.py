from algorithms_comparisons.analysis.compare import BarChartComparator, PerformanceChartComparator
import algorithms_comparisons.factorial.factorial as f

def compare_factorials_barchart():
    comparator = BarChartComparator()
    functions = [f.accumulated_factorial, f.dynamic_factorial, f.naive_factorial, f.recursive_factorial]
    parameters = [i for i in range(100)]
    comparator.compare(functions, parameters)
    
def compare_factorials_performancechart():
    comparator = PerformanceChartComparator()
    functions = [f.accumulated_factorial, f.dynamic_factorial, f.naive_factorial, f.recursive_factorial]
    parameters = [i for i in range(300)]
    comparator.compare(functions, parameters)

if __name__ == "__main__":
    compare_factorials_barchart()
    compare_factorials_performancechart()