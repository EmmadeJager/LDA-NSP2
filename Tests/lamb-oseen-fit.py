import numpy as np
from scipy.optimize import curve_fit, differential_evolution
import matplotlib.pyplot as plt

# Your data
data = [
    [0.0, 1.55190864, 1.73089824, 17.66877074, 2.31217222, 0.0, 0.0, 0.0, 0.0, 0.0],
    [
        1.30491845,
        4.57097047,
        1.33108394,
        1.54017677,
        1.21102433,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ],
    [
        2.04938629,
        4.84838525,
        2.83959439,
        1.21933811,
        0.67835976,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
]

# Parse data
data_array = np.array(data)
n_x, n_y = data_array.shape

# Create coordinate grids
x_coords = np.arange(n_x)
y_coords = np.arange(n_y)
X, Y = np.meshgrid(x_coords, y_coords, indexing="ij")

V = data_array
mask = V != 0.0

# Extract valid data
x_valid = X[mask]
y_valid = Y[mask]
v_valid = V[mask]

print(f"Valid measurements: {len(v_valid)} out of {n_x * n_y}")
print(f"Velocity range: [{v_valid.min():.2f}, {v_valid.max():.2f}]")

# First, visualize the raw data to understand it better
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

ax1 = axes[0]
im1 = ax1.pcolormesh(X, Y, np.where(mask, V, np.nan), shading="auto", cmap="RdBu_r")
ax1.scatter(x_valid, y_valid, c=v_valid, s=100, edgecolors="black", cmap="RdBu_r")
ax1.set_xlabel("X position")
ax1.set_ylabel("Y position")
ax1.set_title("Raw LDA Data")
ax1.axis("equal")
plt.colorbar(im1, ax=ax1, label="Velocity (m/s)")

# Scatter plot to see pattern
ax2 = axes[1]
scatter = ax2.scatter(x_valid, y_valid, c=v_valid, s=200, cmap="RdBu_r")
for i, (x, y, v) in enumerate(zip(x_valid, y_valid, v_valid)):
    ax2.text(x, y, f"{v:.1f}", ha="center", va="center", fontsize=8)
ax2.set_xlabel("X position")
ax2.set_ylabel("Y position")
ax2.set_title("Valid Measurements with Values")
ax2.axis("equal")
ax2.grid(True, alpha=0.3)
plt.colorbar(scatter, ax=ax2, label="Velocity (m/s)")
plt.tight_layout()
plt.show()


# Lamb-Oseen model
def lamb_oseen_horizontal_lda(xy, x0, y0, Gamma, rc):
    """Lamb-Oseen vortex with horizontal LDA measurement"""
    x, y = xy

    dx = x - x0
    dy = y - y0
    r = np.sqrt(dx**2 + dy**2)
    r = np.maximum(r, 1e-6)  # Avoid singularity

    # Lamb-Oseen tangential velocity
    v_tangential = (Gamma / (2 * np.pi * r)) * (1 - np.exp(-(r**2) / rc**2))

    # Angle from vortex center
    theta = np.arctan2(dy, dx)

    # Horizontal component: v_x = -v_tang * sin(θ)
    v_measured = -v_tangential * np.sin(theta)

    return v_measured


# Better initial guess: vortex center where velocities transition
# Look for sign changes or velocity magnitude patterns
x0_guess = 0.5  # Near the measured region
y0_guess = 2.0  # Somewhere in middle of measurements

# Estimate circulation from peak velocity
# For Lamb-Oseen: v_max ≈ Γ/(2πrc) * 0.715 (at r ≈ 1.12*rc)
v_max = np.max(np.abs(v_valid))
rc_guess = 0.5
Gamma_guess = v_max * 2 * np.pi * rc_guess / 0.715

print(f"\nInitial guesses:")
print(f"  Center: ({x0_guess:.2f}, {y0_guess:.2f})")
print(f"  Γ: {Gamma_guess:.4f}")
print(f"  rc: {rc_guess:.4f}")

# Try differential evolution for global optimization (more robust)
print("\nAttempting fit with differential evolution...")


def objective(params):
    """Objective function for optimization"""
    try:
        v_pred = lamb_oseen_horizontal_lda((x_valid, y_valid), *params)
        return np.sum((v_valid - v_pred) ** 2)
    except:
        return 1e10


# Define bounds
bounds = [
    (-2, 5),  # x0: vortex center x
    (-2, 8),  # y0: vortex center y
    (-50, 50),  # Gamma: circulation (allow negative for opposite rotation)
    (0.1, 5),  # rc: core radius
]

result = differential_evolution(
    objective, bounds, maxiter=1000, popsize=15, tol=1e-7, seed=42, disp=True
)

if result.success:
    popt = result.x
    x0_fit, y0_fit, Gamma_fit, rc_fit = popt

    print(f"\n{'=' * 50}")
    print(f"FITTED PARAMETERS:")
    print(f"{'=' * 50}")
    print(f"  Vortex center: ({x0_fit:.4f}, {y0_fit:.4f})")
    print(f"  Circulation Γ: {Gamma_fit:.6f}")
    print(f"  Core radius rc: {rc_fit:.6f}")

    # Now refine with curve_fit
    print("\nRefining with curve_fit...")
    try:
        popt_refined, pcov = curve_fit(
            lamb_oseen_horizontal_lda,
            (x_valid, y_valid),
            v_valid,
            p0=popt,
            maxfev=10000,
        )

        perr = np.sqrt(np.diag(pcov))
        x0_fit, y0_fit, Gamma_fit, rc_fit = popt_refined

        print(f"\nREFINED PARAMETERS:")
        print(
            f"  Vortex center: ({x0_fit:.4f} ± {perr[0]:.4f}, {y0_fit:.4f} ± {perr[1]:.4f})"
        )
        print(f"  Circulation Γ: {Gamma_fit:.6f} ± {perr[2]:.6f}")
        print(f"  Core radius rc: {rc_fit:.6f} ± {perr[3]:.6f}")

        popt = popt_refined
    except:
        print("Refinement failed, using differential evolution result")

    # Calculate fitted values and residuals
    v_fitted_valid = lamb_oseen_horizontal_lda((x_valid, y_valid), *popt)
    residuals = v_valid - v_fitted_valid
    rmse = np.sqrt(np.mean(residuals**2))
    r_squared = 1 - np.sum(residuals**2) / np.sum((v_valid - np.mean(v_valid)) ** 2)

    print(f"\nFIT QUALITY:")
    print(f"  RMSE: {rmse:.6f}")
    print(f"  R²: {r_squared:.4f}")

    # Create full grid prediction
    v_fitted_full = lamb_oseen_horizontal_lda((X, Y), *popt)

    # Visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    # 1. Original measurements
    ax1 = axes[0, 0]
    im1 = ax1.pcolormesh(X, Y, np.where(mask, V, np.nan), shading="auto", cmap="RdBu_r")
    ax1.plot(
        x0_fit, y0_fit, "k+", markersize=20, markeredgewidth=3, label="Fitted center"
    )
    ax1.set_xlabel("X position")
    ax1.set_ylabel("Y position")
    ax1.set_title("Original LDA Measurements")
    ax1.legend()
    ax1.axis("equal")
    plt.colorbar(im1, ax=ax1, label="Velocity (m/s)")

    # 2. Fitted model (full grid)
    ax2 = axes[0, 1]
    im2 = ax2.pcolormesh(X, Y, v_fitted_full, shading="auto", cmap="RdBu_r")
    ax2.plot(
        x0_fit, y0_fit, "k+", markersize=20, markeredgewidth=3, label="Fitted center"
    )
    circle = plt.Circle(
        (x0_fit, y0_fit),
        rc_fit,
        fill=False,
        color="yellow",
        linewidth=2,
        linestyle="--",
        label=f"Core radius: {rc_fit:.3f}",
    )
    ax2.add_patch(circle)
    ax2.scatter(
        x_valid, y_valid, c="gray", s=50, alpha=0.5, marker="x", label="Measured points"
    )
    ax2.set_xlabel("X position")
    ax2.set_ylabel("Y position")
    ax2.set_title("Fitted Lamb-Oseen Model")
    ax2.legend()
    ax2.axis("equal")
    plt.colorbar(im2, ax=ax2, label="Velocity (m/s)")

    # 3. Measured vs Fitted scatter
    ax3 = axes[1, 0]
    ax3.scatter(v_valid, v_fitted_valid, alpha=0.6, s=100, edgecolors="black")
    min_v = min(v_valid.min(), v_fitted_valid.min())
    max_v = max(v_valid.max(), v_fitted_valid.max())
    ax3.plot([min_v, max_v], [min_v, max_v], "r--", linewidth=2, label="Perfect fit")
    ax3.set_xlabel("Measured velocity (m/s)")
    ax3.set_ylabel("Fitted velocity (m/s)")
    ax3.set_title(f"Fit Quality (RMSE: {rmse:.4f}, R²: {r_squared:.3f})")
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.axis("equal")

    # 4. Residuals
    ax4 = axes[1, 1]
    ax4.scatter(
        x_valid,
        y_valid,
        c=residuals,
        s=200,
        cmap="RdBu_r",
        edgecolors="black",
        vmin=-2,
        vmax=2,
    )
    ax4.plot(x0_fit, y0_fit, "k+", markersize=20, markeredgewidth=3)
    ax4.set_xlabel("X position")
    ax4.set_ylabel("Y position")
    ax4.set_title("Residuals (Measured - Fitted)")
    ax4.axis("equal")
    ax4.grid(True, alpha=0.3)
    plt.colorbar(ax4.collections[0], ax=ax4, label="Residual (m/s)")

    plt.tight_layout()
    plt.show()

    # Print comparison table
    print(f"\n{'=' * 60}")
    print(f"MEASUREMENT COMPARISON:")
    print(f"{'=' * 60}")
    print(f"{'X':>6} {'Y':>6} {'Measured':>12} {'Fitted':>12} {'Residual':>12}")
    print(f"{'-' * 60}")
    for x, y, v_m, v_f in zip(x_valid, y_valid, v_valid, v_fitted_valid):
        print(f"{x:6.2f} {y:6.2f} {v_m:12.6f} {v_f:12.6f} {v_m - v_f:12.6f}")

else:
    print(f"\nOptimization failed: {result.message}")
    print("The data may not be consistent with a Lamb-Oseen vortex model")
    print("Possible issues:")
    print("  - Insufficient data points")
    print("  - Measurement noise")
    print("  - Vortex center outside measured region")
    print("  - Non-Lamb-Oseen vortex structure")
