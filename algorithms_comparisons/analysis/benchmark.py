import sys
import abc
from algorithms_comparisons.utility.timer import timed

class Benchmark(abc.ABC):
    @abc.abstractmethod
    def measure_time_of_execution(self,timed_functions, parameters):
        pass
    
    @abc.abstractmethod
    def build_output(self, functions, time_results, parameters):
        pass

    
    def run(self, functions, parameters):
        timed_functions = self.decorate_functions_with_timer(functions)
        time_results = self.measure_time_of_execution(timed_functions, parameters)
        output = self.build_output(functions, time_results, parameters)
        return output

    def decorate_functions_with_timer(self, functions):
        timed_functions = []
        for function in functions:
            timed_functions.append(timed(function))
        return timed_functions

class OverallPerformanceBenchmark(Benchmark):

    def measure_time_of_execution(self, timed_functions, parameters):
        time_results = [0] * len(timed_functions)
        for index, timed_function in enumerate(timed_functions):
            time_result = 0
            for parameter in parameters:
                _, time = timed_function(parameter)
                time_result += time
            time_results[index] = time_result
        return time_results

    def build_output(self, functions, time_results, parameters):
        function_names = [function.__name__ for function in functions]
        return (function_names, time_results)

class ProblemSizePerformanceBenchmark(Benchmark):
    def measure_time_of_execution(self, timed_functions, parameters):
        num_trials = 20
        time_results = [[0 for x in range(len(parameters))] for fun in range(len(timed_functions))]
        for trial in range(num_trials):
            for findex, timed_function in enumerate(timed_functions):
                for pindex, param in enumerate(parameters):
                    _, time = timed_function(param)
                    time_results[findex][pindex] += time/num_trials
        return time_results

    def build_output(self, functions, time_results, parameters):
        function_names = [function.__name__ for function in functions]
        return (function_names, parameters, time_results)

