import matplotlib.pyplot as plt
import numpy as np
import polynomial

class VisualizePoly(polynomial.Polynomial):
    def __init__(self, coeffs):
        super().__init__(coeffs)
    def evaluate(self, x) -> float:
        y = 0.0
        for i, coeff in enumerate(self.coeffs):
            y += coeff * (x ** i)
        return y

    def plot(self, x_range=(-10, 10), num_points=1000, title="Polynomial Plot", xlabel="x", ylabel="f(x)"):
        x_values = np.linspace(x_range[0], x_range[1], num_points)
        y_values = self.evaluate(x_values)

        plt.plot(x_values, y_values, label=str(self))
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.axhline(0, color='black', linewidth=0.5)  # Add x-axis
        plt.axvline(0, color='black', linewidth=0.5)  # Add y-axis
        plt.grid(True)
        plt.legend()
        plt.show()
