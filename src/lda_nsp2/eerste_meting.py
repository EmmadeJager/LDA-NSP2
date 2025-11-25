# Eerste code voor het bereken van een stroomprofiel in een cilindrische buis met water.

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

from src.lda_nsp2.data_ingestion import Ingest_Data

def bereken_v(x, y, z, f, delta_x, delta_y, delta_z, delta_f):
    """Functie om v te berekenen bij bepaalde frequentie en afstanden.

    Args:
        x (float): Afstand van lens tot bekerglas.
        y (float): Afstand van laser 1 tot laser 2 in lens.
        z (float): Afstand van laser 1 tot laser 2 op bekerglas.
        f (float): Frequentie interferentiepatroon.
        delta_x (float): Fout op x
        delta_y (float): Fout op y
        delta_z (float): Fout op z
        delta_f (float): Fout op f
    """
    theta = np.arctan((0.5 * y - 0.5 * z) / x)
    lamda = 632.8 * (10**-9)
    v = f * (lamda / (2 * np.sin(theta)))

    # bereken fout op theta
    u = (0.5 * y - 0.5 * z) / x
    dy = (0.5 * delta_y) / x
    dz = (0.5 * delta_z) / x
    dx = (0.5 * (y - z) * delta_x) / x**2
    delta_theta = (1 / (1 + u**2)) * np.sqrt(dx**2 + dy**2 + dz**2)

    # bereken fout op v
    delta_lamda = 0.1
    df = (lamda * delta_f) / 2 * np.sin(theta)
    dlamda = (f * delta_lamda) / 2 * np.sin(theta)
    dtheta = (f * lamda * np.cos(theta) * delta_theta) / (2 * (np.sin(theta)) ** 2)
    delta_v = np.sqrt(df**2 + dlamda**2 + dtheta**2)

    return theta, delta_theta, v, delta_v

# print(bereken_v(97, 17, 2.5, 2836))
# print(bereken_v(97, 17, 2.5, 2712))
# print(bereken_v(97, 17, 2.5, 2133))

# stop gemeten data in testcode
ingestion = Ingest_Data("first measurement!!!!!")
data = ingestion.returndata()

# fit data met gauss fit
def Gauss(x, A, B, slide):
    return A * np.exp(-B * (x - slide) ** 2)

estimated_sigma = 100
B_guess = 1 / (2 * estimated_sigma**2)

# definieer (fit)parameters
parameters, _ = curve_fit(
    Gauss,
    data[0],
    data[1],
    p0=[
        max(data[1]),
        B_guess,
        data[0][data[1].index(max(data[1]))]
    ],
)

# doe fit
fit_A, fit_B, fit_C= parameters
print(f"A = {fit_A}")
print(f"B = {fit_B}")
print(f"C = {fit_C}")
fit_y = Gauss(data[0], fit_A, fit_B, fit_C)
print(f"Sigma = {1 / (fit_A * np.sqrt(2 * np.pi))}")

# plot fit
plt.plot(data[0], data[1], ".", label="Data")
plt.plot(data[0], fit_y, '-', label='Fit')
plt.legend()
plt.grid()
plt.show()
