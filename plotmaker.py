import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

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
