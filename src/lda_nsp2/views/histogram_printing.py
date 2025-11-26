# code om alle data in histogrammen om te zetten en als png op te slaan.
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import re

# Pad naar je data map
folder_path = "./src/lda_nsp2/data"
file_pattern = os.path.join(folder_path, "*")  # pak alle bestanden

# Zoek alle bestanden
files = glob.glob(file_pattern)
print("Bestanden gevonden:", files)

for file_path in files:
    # Bestand inlezen
    with open(file_path, "r") as dataFile:
        data = [line.split() for line in dataFile]

    freqs = []
    for line in data:
        line = [i.replace(",", ".") for i in line]
        try:
            freqs.append(float(line[0]))
        except ValueError:
            continue  # sla lege of foutieve regels over

    # Vortex nummer en coördinaten uit bestandsnaam halen
    base_name = os.path.basename(file_path)
    
    # Coördinaten tussen haakjes
    coords_match = re.search(r"\((.*?)\)", base_name)
    coords = coords_match.group(1) if coords_match else "unknown"

    # Vortex nummer na 'Vortex #'
    vortex_match = re.search(r"Vortex #(\d+)", base_name)
    vortex_number = vortex_match.group(1) if vortex_match else "unknown"

    # Plotten
    plt.hist(freqs, bins=30)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Occurrence")
    plt.title(f"Vortex {vortex_number} ({coords})")

    # Opslaan in dezelfde map
    save_name = os.path.join(folder_path, f"Vortex {vortex_number} ({coords}).png")
    plt.savefig(save_name)
    plt.close()
