import numpy as np

def highpass(f, fc, k):
    exponent = - (f - fc) / k
    sigmoid = 1 / (1 + np.exp(exponent))
    return sigmoid

def lowpass(f, fc, k):
    exponent = (f - fc) / k
    sigmoid = 1 / (1 + np.exp(exponent))
    return sigmoid