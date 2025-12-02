import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

from lda_nsp2.models.fitting import gaussfit, Gauss
from lda_nsp2.data_ingestion import Ingest_Data_1D

raw_data = np.loadtxt("EXPORT_original_data.csv", delimiter=",")
fitted_data = np.loadtxt("EXPORT_fitted_full_data.csv", delimiter=",")
sigma_data = np.loadtxt("EXPORT_uncertainty_data.csv", delimiter=",")


# Initial fit successful

# Refining with weighted curve_fit
# Refinement failed: too many values to unpack (expected 2)
# Using differential evolution result

# ==============================
# FITTED PARAMETERS (with uncertainties):
# ==============================
#   Vortex center X: 1.4221 ± 0.0000
#   Vortex center Y: 3.4077 ± 0.0000
#   Circulation Γ:   -50.000000 ± 0.000000
#   Core radius rc:  0.628978 ± 0.000000

# FIT QUALITY:
#   RMSE: 1.852193
#   Weighted RMSE: 0.553288
#   χ²: 7.0409
#   Reduced χ² (χ²/dof): 0.3706
#   → Good fit! (reduced χ² close to 1)


x0_fit = 1.4221
y0_fit = 3.4077


plt.figure(figsize=(8, 8))
fontdict = {"family": "serif", "size": 12}
plt.imshow(
    raw_data.T[:10, :10],
    cmap="twilight_shifted",
    origin="lower",
    norm=colors.LogNorm(vmin=0.1, vmax=raw_data.max()),
)
plt.plot(x0_fit, y0_fit, "k+", markersize=20, markeredgewidth=3)
plt.xlabel("X position", fontdict=fontdict)
plt.ylabel("Y position", fontdict=fontdict)
plt.tick_params(axis="both", labelsize=10)
plt.title("Original LDA Measurements", fontdict=fontdict)

plt.colorbar(label="Velocity (m/s)", shrink=1.0, aspect=20)
plt.savefig("original_heatmap.pdf", bbox_inches="tight")


plt.figure(figsize=(8, 8))
fontdict = {"family": "serif", "size": 12}
plt.imshow(
    fitted_data.T[:30, :30],
    cmap="twilight_shifted",
    origin="lower",
    norm=colors.LogNorm(vmin=0.1, vmax=fitted_data.max()),
)
plt.colorbar(label="Velocity (m/s)")
# get coordinates where mask is non-zero
y_idx, x_idx = np.where(raw_data.T != 0)
plt.scatter(x_idx, y_idx, c="gray", s=50, alpha=0.5, marker="x")

plt.plot(x0_fit, y0_fit, "k+", markersize=20, markeredgewidth=3)
plt.xlabel("X position", fontdict=fontdict)
plt.ylabel("Y position", fontdict=fontdict)
plt.tick_params(axis="both", labelsize=10)
plt.title("Fitted Lamb-Oseen", fontdict=fontdict)


plt.savefig("fitted_heatmap.pdf", bbox_inches="tight")


plt.figure(figsize=(8, 8))
fontdict = {"family": "serif", "size": 12}
plt.imshow(
    sigma_data.T[:10, :10],
    cmap="afmhot_r",
    origin="lower",
    norm=colors.LogNorm(vmin=0.1, vmax=sigma_data.max()),
)
plt.plot(x0_fit, y0_fit, "k+", markersize=20, markeredgewidth=3)
plt.xlabel("X position", fontdict=fontdict)
plt.ylabel("Y position", fontdict=fontdict)
plt.tick_params(axis="both", labelsize=10)
plt.title("Measurement Uncertainties", fontdict=fontdict)

plt.colorbar(label="Velocity (m/s)")
plt.savefig("sigma_heatmap.pdf", bbox_inches="tight")


histogram = Ingest_Data_1D("Tests\(0,4,154) Vortex #05")
hist_data = histogram.returndata()
y, x = np.histogram(hist_data, bins=32)

x = list(x)
y = list(y)

x.pop(-1)

A_Guess = max(y)
B_Guess = 0.0005
C_Guess = x[y.index(max(y))]

fit_data = gaussfit(x, y, A_guess=A_Guess, B_guess=B_Guess, C_guess=C_Guess)

x_space = np.linspace(x[0], x[-1], 500)
y_fit = []

for i in x_space:
    y_fit.append(Gauss(i, fit_data[0], fit_data[1], fit_data[2]))

plt.figure(figsize=(8, 8))
plt.grid()

plt.hist(hist_data, bins=32)
plt.plot(x_space, y_fit)

mu = x_space[y_fit.index(max(y_fit))]  # your fitted mean
sigma = 1/(fit_data[0] * np.sqrt(2 * np.pi))  # your fitted sigma
print(sigma)
print(fit_data[0])

# vertical line at mean
plt.axvline(mu, color="red", linestyle="--", linewidth=1.5, label=f"$\mu = {mu:.1f}$")

# vertical lines at ±sigma
plt.axvline(
    mu - sigma,
    color="gray",
    linestyle=":",
    linewidth=1.5,
    label=f"$\sigma = {sigma:.1f}$",
)
plt.axvline(mu + sigma, color="gray", linestyle=":", linewidth=1.5)

# annotate
plt.annotate(f'$\mu = {mu:.1f}$', xy=(mu, 90), xytext=(mu + 50, 95),
             arrowprops=dict(arrowstyle='->', color='red'), fontsize=11)

plt.legend()

plt.show()
