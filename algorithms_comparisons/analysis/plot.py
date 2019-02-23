import abc
import numpy as np
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
        plt.xticks(np.arange(0, int(len(parameters)), len(parameters)/10))
        plt.xlabel("Problem size")
        plt.ylabel("Time taken (s)")
        for index, label in enumerate(labels):
            plt.plot(parameters, time_results[index], colors[index], label=label)
        plt.legend()
        plt.show()