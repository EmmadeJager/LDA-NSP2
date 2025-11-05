import numpy as np

# functie om v te berekenen bij bepaalde frequentie
def bereken_v(x, y, z, f):
    theta = np.arctan((0.5*y - 0.5*z) / x)
    lamda = 632.8 * (10 ** -9)
    v = f * (lamda / (2 * np.sin(theta)))

    return theta, v

print(bereken_v(97, 17, 2.5, 2836))
print(bereken_v(97, 17, 2.5, 2712))
print(bereken_v(97, 17, 2.5, 2133))