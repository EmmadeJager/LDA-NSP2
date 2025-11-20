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


# Lamb-Oseen model
def lamb_oseen_model(xy, x0, y0, Gamma, rc):
    """Lamb-Oseen vortex fitting function"""
    x, y = xy
    
    dx = x - x0
    dy = y - y0
    r = np.sqrt(dx**2 + dy**2)
    r = np.maximum(r, 1e-6)
    
    v_tangential = (Gamma / (2 * np.pi * r)) * (1 - np.exp(-r**2 / rc**2))
    theta = np.arctan2(dy, dx)
    v_measured = -v_tangential * np.sin(theta)
    
    return v_measured