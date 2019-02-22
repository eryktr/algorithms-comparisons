from algorithms_comparisons.analysis.compare import BarChartComparator
import algorithms_comparisons.factorial.factorial as f

def compare_factorials():
    comparator = BarChartComparator()
    functions = [f.accumulated_factorial, f.dynamic_factorial, f.naive_factorial, f.recursive_factorial]
    parameters = [i for i in range(100)]
    comparator.compare(functions, parameters)
    
if __name__ == "__main__":
    compare_factorials()