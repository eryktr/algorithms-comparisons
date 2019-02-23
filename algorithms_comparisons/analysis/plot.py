import abc
import matplotlib.pyplot as plt


class Plotter(abc.ABC):
    @abc.abstractmethod
    def plot(self, results):
        pass
        

class BarChartPlotter(Plotter):
    def plot(self, results):
        labels = results[0]
        values = results[1]
        plt.bar(labels, values)
        plt.show()

class PerformanceChartPlotter(Plotter):
    def plot(self, results):
        labels = results[0]
        parameters = results[1]
        time_results = results[2]
        colors =['b','r','g','y']
        for index, time_result in enumerate(time_results):
            plt.plot(parameters, time_result, colors[index], label=labels[index])
            plt.legend()
        plt.show()