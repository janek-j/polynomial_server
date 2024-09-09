import numpy as np

class Polynomial:
    def __init__(self, coeffs: list):
        self.coeffs = coeffs
        self.n = len(coeffs)

    def get_n(self):
        return self.n

    def __str__(self):
        this_n = self.get_n()
        result_str = "Polynomial: \n"
        for i in range(this_n):
            result_str += f"{self.coeffs[i]}*x^{i} "
            if i < this_n - 1:
                result_str += "+ "
        return result_str

    def __add__(self, other_poly):
        this_size = self.get_n()
        other_size = other_poly.get_n()
        max_n = max(this_size, other_size)
        min_n = min(this_size, other_size)
        result_coeffs = []
        for i in range(min_n):
            result_coeffs.append(self.coeffs[i] + other_poly.coeffs[i])

        if this_size > other_size:
            result_coeffs.extend(self.coeffs[min_n:this_size])
        else:
            result_coeffs.extend(other_poly.coeffs[min_n:other_size])
        return Polynomial(result_coeffs)

    def __sub__(self, other_poly):
        this_size = self.get_n()
        other_size = other_poly.get_n()
        max_n = max(this_size, other_size)
        min_n = min(this_size, other_size)
        result_coeffs = []
        for i in range(min_n):
            result_coeffs.append(self.coeffs[i] - other_poly.coeffs[i])

        if this_size > other_size:
            result_coeffs.extend(self.coeffs[min_n:this_size])
        else:
            for i in range(min_n, other_size):
                result_coeffs.append( (-1)*other_poly.coeffs[i])

        return Polynomial(result_coeffs)

    def __mul__(self, other_poly):
        this_size = self.get_n()
        other_size = other_poly.get_n()

        coeffs = [0] * (this_size + other_size - 1)
        for i in range(this_size):
            for j in range(other_size):
                coeffs[i+j] += self.coeffs[i] * other_poly.coeffs[j]

        return Polynomial(coeffs)