import numpy as np
from scipy.optimize import curve_fit


def Gauss(x, A, B, slide):
    return A * np.exp(-B * (x - slide) ** 2)


def gaussfit(xvals, yvals, A_guess, B_guess, C_guess):
    data = [xvals, yvals]

    parameters, _ = curve_fit(
        Gauss,
        data[0],
        data[1],
        p0=[A_guess, B_guess, C_guess],
    )

    fit_A, fit_B, fit_C = parameters
    fit_y = Gauss(data[0], fit_A, fit_B, fit_C)

    return fit_A, fit_B, fit_C, fit_y


def parabola(x, a, b, c):
    return a * x**2 + b * x + c


def parabfit(xvals, yvals, A_guess, B_guess, C_guess):
    data = [xvals, yvals]

    parameters, _ = curve_fit(
        parabola,
        data[0],
        data[1],
        p0=[A_guess, B_guess, C_guess],
    )

    fit_x = np.linspace(min(xvals), max(xvals), 100)

    fit_A, fit_B, fit_C = parameters
    fit_y = parabola(fit_x, fit_A, fit_B, fit_C)

    return fit_A, fit_B, fit_C, fit_y, fit_x
