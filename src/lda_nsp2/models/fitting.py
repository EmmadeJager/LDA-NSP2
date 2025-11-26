# code voor het fitten van histrogram-frequentie data uit LabView aan een Gaussfit. Met verschillende
# fit functies voor het fitten van een vortexmodel.

import numpy as np
from scipy.optimize import curve_fit


# definieer Gauss-functie
def Gauss(x, A, B, slide):
    return A * np.exp(-B * (x - slide) ** 2)


# definieer Gaussfit
def gaussfit(xvals, yvals, A_guess, B_guess, C_guess):
    data = [xvals, yvals]

    # neem parameters (met guess)
    parameters, _ = curve_fit(
        Gauss,
        data[0],
        data[1],
        p0=[A_guess, B_guess, C_guess],
    )

    fit_A, fit_B, fit_C = parameters
    fit_y = Gauss(data[0], fit_A, fit_B, fit_C)

    return fit_A, fit_B, fit_C, fit_y


# definieer parabool-functie
def parabola(x, a, b, c):
    return a * x**2 + b * x + c


# definieer parabool-fit
def parabfit(xvals, yvals, A_guess, B_guess, C_guess):
    data = [xvals, yvals]

    # neem parameters
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


def lamb_oseen_model(xy, x0, y0, Gamma, rc):
    """Lamb-Oseen vortex fit-functie"""
    x, y = xy

    dx = x - x0
    dy = y - y0
    r = np.sqrt(dx**2 + dy**2)
    r = np.maximum(r, 1e-6)

    v_tangential = (Gamma / (2 * np.pi * r)) * (1 - np.exp(-(r**2) / rc**2))
    theta = np.arctan2(dy, dx)
    v_measured = -v_tangential * np.sin(theta)

    return np.abs(v_measured)


def rankine_model(xy, x0, y0, Gamma, rc):
    """Rankine (samengesteld) vortex fitfunctie.
    Laminente rotatie in het middel en potentiele ruis daarbuiten.
    """
    x, y = xy

    dx = x - x0
    dy = y - y0
    r = np.sqrt(dx**2 + dy**2)
    r = np.maximum(r, 1e-6)

    # Rankine vortex
    v_tangential = np.where(
        r <= rc,
        # Binnen: laminente rotatie
        (Gamma * r) / (2 * np.pi * rc**2),
        # Buiten: potentiele ruis
        Gamma / (2 * np.pi * r),
    )

    theta = np.arctan2(dy, dx)
    v_measured = -v_tangential * np.sin(theta)

    return np.abs(v_measured)


def kaufmann_model(xy, x0, y0, Gamma, rc):
    """Kaufmann vortex fitfunctie.
    Gladde transitie door de middenregio.
    """
    x, y = xy

    dx = x - x0
    dy = y - y0
    r = np.sqrt(dx**2 + dy**2)
    r = np.maximum(r, 1e-6)

    # Kaufmann vortex
    v_tangential = (Gamma / (2 * np.pi)) * (r / (r**2 + rc**2))

    theta = np.arctan2(dy, dx)
    v_measured = -v_tangential * np.sin(theta)

    return np.abs(v_measured)


def vatistas_model(xy, x0, y0, Gamma, rc, n=1.0):
    """Vatistas vortex - gegeneraliseerd model met vorm-parameter n

    n=1: Scully/Kaufmann vortex
    n=2: Lamb-Oseen
    n→∞: Rankine vortex

    Te gebruiken voor het vinden van de "beste" vortexvorm voor data.
    """
    x, y = xy

    dx = x - x0
    dy = y - y0
    r = np.sqrt(dx**2 + dy**2)
    r = np.maximum(r, 1e-6)

    # Vatistas formule
    v_tangential = (Gamma / (2 * np.pi * r)) * (r**n / (r**n + rc**n)) ** (1 / n)

    theta = np.arctan2(dy, dx)
    v_measured = -v_tangential * np.sin(theta)

    return np.abs(v_measured)


def burgers_model(xy, x0, y0, Gamma, rc):
    """Burgers vortex - inclusief axesincludes axiale rekeffecten
    Werkt voor: gerekte vortexen. Lijkt op lamb-oseen maar anders exponentieel.
    """
    x, y = xy

    dx = x - x0
    dy = y - y0
    r = np.sqrt(dx**2 + dy**2)
    r = np.maximum(r, 1e-6)

    # Burgers vortex
    alpha = 1.25643  # Burgers parameter
    v_tangential = (Gamma / (2 * np.pi * r)) * (1 - np.exp(-alpha * r**2 / rc**2))

    theta = np.arctan2(dy, dx)
    v_measured = -v_tangential * np.sin(theta)

    return np.abs(v_measured)


def sullivan_model(xy, x0, y0, Gamma, rc):
    """Sullivan vortex - gladde Rankine variant.
    Goede compromie tussen Rankine en Lamb-Oseen.
    """
    x, y = xy

    dx = x - x0
    dy = y - y0
    r = np.sqrt(dx**2 + dy**2)
    r = np.maximum(r, 1e-6)

    # Sullivan formule
    v_tangential = (Gamma / (2 * np.pi * r)) * np.tanh(r / rc)

    theta = np.arctan2(dy, dx)
    v_measured = -v_tangential * np.sin(theta)

    return np.abs(v_measured)


def batchelor_model(xy, x0, y0, Gamma, rc, q=2.0):
    """Batchelor (q-vortex) model

    q=2: Standaar Gaussisch profiel
    q>2: Geconcentreerd middelpunt
    q<2: Meer diffuus middelpunt
    """
    x, y = xy

    dx = x - x0
    dy = y - y0
    r = np.sqrt(dx**2 + dy**2)
    r = np.maximum(r, 1e-6)

    # Batchelor vortex
    v_tangential = (Gamma / (2 * np.pi * r)) * (1 - np.exp(-(r**q) / rc**q))

    theta = np.arctan2(dy, dx)
    v_measured = -v_tangential * np.sin(theta)

    return np.abs(v_measured)


def modified_rankine_model(xy, x0, y0, Gamma, rc, delta=0.1):
    """Modified Rankine - gladde transitie regio

    delta: transitie weidte (fractie van rc)
    delta→0: dichtbij scherpe rankine
    """
    x, y = xy

    dx = x - x0
    dy = y - y0
    r = np.sqrt(dx**2 + dy**2)
    r = np.maximum(r, 1e-6)

    # gladde transitie met tanh
    transition = 0.5 * (1 + np.tanh((r - rc) / (delta * rc)))

    # transitie tussen binnen en buiten
    v_inner = (Gamma * r) / (2 * np.pi * rc**2)
    v_outer = Gamma / (2 * np.pi * r)
    v_tangential = v_inner * (1 - transition) + v_outer * transition

    theta = np.arctan2(dy, dx)
    v_measured = -v_tangential * np.sin(theta)

    return np.abs(v_measured)


def two_cell_model(xy, x0, y0, Gamma, rc, beta=0.2):
    """2-cel vortex - omgedraaide roterende middelpunt

    beta: strekte van roterend middelpunt (typisch 0.1-0.3)
    Goed voor: tornado-achtige vortexen
    """
    x, y = xy

    dx = x - x0
    dy = y - y0
    r = np.sqrt(dx**2 + dy**2)
    r = np.maximum(r, 1e-6)

    # 2-cel structuur
    v_tangential = (Gamma / (2 * np.pi * r)) * (
        (1 + beta) * (1 - np.exp(-(r**2) / rc**2))
        - beta * (1 - np.exp(-4 * r**2 / rc**2))
    )

    theta = np.arctan2(dy, dx)
    v_measured = -v_tangential * np.sin(theta)

    return np.abs(v_measured)
