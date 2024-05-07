# libraries
import matplotlib.pyplot as plt
import numpy as np


# plotting
def plot_function():
    function = input("Enter the function (use x as the variable): ")
    x_range = input("Enter the range of x-values (e.g., -10,10): ").split(',')
    x_min = float(x_range[0])
    x_max = float(x_range[1])

    x = np.linspace(x_min, x_max, 100)
    y = eval(function.replace('^', '**'))

    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Graph of {function}")
    plt.grid(True)
    plt.show()


# main loop
while True:
    plot_function()
    choice = input("Do you want to plot another function? (y/n): ").lower()
    if choice != 'y':
        break
