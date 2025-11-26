# test voor plotten van histogrammen
import numpy as np
import matplotlib.pyplot as plt

# txt-bestand met één meting per regel
with open("(0,1,161) Vortex #18", "r") as dataFile:
    data = [line.split() for line in dataFile]

    one_d = []

    for line in data:
        line = [i.replace(",", ".") for i in line]
        one_d.append(float(line[0]))

plt.hist(one_d, bins=30)
plt.xlabel("Waarde")
plt.ylabel("Frequentie")
plt.title("Vortex 18")
plt.savefig("Vortex 18")
plt.show()
