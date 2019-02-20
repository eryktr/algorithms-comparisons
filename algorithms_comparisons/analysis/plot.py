import matplotlib.pyplot as plt

def plot(results):
    labels = results[0]
    values = results[1]
    plt.bar(labels, values)
    plt.show()
