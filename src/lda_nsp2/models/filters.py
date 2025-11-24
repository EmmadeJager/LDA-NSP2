# code voor het definieren van low- en highpassfilters, voor het filteren van de histogramdata.

import numpy as np

# definieer highpassfilter
def highpass(f, fc, k):
    exponent = - (f - fc) / k
    sigmoid = 1 / (1 + np.exp(exponent))
    return sigmoid

# definieer lowpassfilter
def lowpass(f, fc, k):
    exponent = (f - fc) / k
    sigmoid = 1 / (1 + np.exp(exponent))
    return sigmoid