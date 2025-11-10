import numpy as np

# functie om v te berekenen bij bepaalde frequentie
def bereken_v(x, y, z, f, delta_x, delta_y, delta_z):
    theta = np.arctan((0.5*y - 0.5*z) / x)
    lamda = 632.8 * (10 ** -9)
    v = f * (lamda / (2 * np.sin(theta)))

    u = (0.5 * y - 0.5 * z) / x
    dy = (0.5 * delta_y) / x
    dz = (0.5 * delta_z) / x
    dx = (0.5 * (y - z) * delta_x) / x**2
    delta_theta = (1 / (1 + u**2)) * np.sqrt(dx**2 + dy**2 + dz**2)

    return theta, v, delta_theta

print(bereken_v(97, 17, 2.5, 2836))
print(bereken_v(97, 17, 2.5, 2712))
print(bereken_v(97, 17, 2.5, 2133))