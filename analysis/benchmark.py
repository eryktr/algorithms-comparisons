from utility.timer import timed
def benchmark(functions, parameters):
    
    def decorate_functions_with_timer(functions):
        timed_functions = []
        for function in functions:
            timed_functions.append(timed(function))
        return timed_functions

    def measure_time_of_execution(timed_functions, parameters):
        time_results = [0] * len(timed_functions)
        for index, timed_function in enumerate(timed_functions):
            time_result = 0
            for parameter in parameters:
                _, time = timed_function(parameter)
                time_result += time
            time_results[index] = time_result
        return time_results

    def build_output(functions, time_results):
        results = {}
        for function in functions:
            for result in time_results:
                results[function.__name__] = result
        return results
    
    timed_functions = decorate_functions_with_timer(functions)
    time_results = measure_time_of_execution(timed_functions, parameters)
    output = build_output(functions, time_results)
    return output

