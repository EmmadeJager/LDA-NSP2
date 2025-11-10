from scipy.optimize import curve_fit
import numpy as np


def Gauss(x, A, B, slide):
    return A * np.exp(-B * (x - slide) ** 2)


def gaussfit(xvals, yvals, A_guess, B_guess, C_guess):
    data = [xvals, yvals]

    parameters, _ = curve_fit(
        Gauss,
        data[0],
        data[1],
        p0=[
            A_guess,
            B_guess,
            C_guess
        ],
    )

    fit_A, fit_B, fit_C= parameters
    fit_y = Gauss(data[0], fit_A, fit_B, fit_C)

    return fit_A, fit_B, fit_C, fit_y
