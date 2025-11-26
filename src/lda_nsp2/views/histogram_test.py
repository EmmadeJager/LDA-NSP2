# test voor plotten van histogrammen
import numpy as np
import matplotlib.pyplot as plt

# txt-bestand met één meting per regel
with open("(0,1,161) Vortex #18", "r") as dataFile:
    data = [line.split() for line in dataFile]

    freqs = []

    for line in data:
        line = [i.replace(",", ".") for i in line]
        freqs.append(float(line[0]))

plt.hist(freqs, bins=30)
plt.xlabel("Waarde")
plt.ylabel("Frequentie")
plt.title("Vortex 18")
plt.savefig("Vortex 18")
plt.show()
