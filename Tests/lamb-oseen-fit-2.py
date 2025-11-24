# test code voor lamb oseen fit

import numpy as np
from scipy.optimize import curve_fit, differential_evolution
import matplotlib.pyplot as plt

# Your data
data = [
    [3.19418509, 1.55190864, 1.73089824, 17.66877074, 2.31217222, 0.0, 0.0, 0.0, 0.0, 0.0],
    [1.30491845, 4.57097047, 1.33108394, 1.54017677, 1.21102433, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2.04938629, 4.84838525, 2.83959439, 1.21933811, 0.67835976, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
]

# YOUR UNCERTAINTIES - replace with your actual values
# Same structure as data: 10x10 grid
uncertainties = [
    [3.19418509, 1.55190864, 1.73089824, 17.66877074, 2.31217222, 0.0, 0.0, 0.0, 0.0, 0.0],
    [1.30491845, 4.57097047, 1.33108394, 1.54017677, 1.21102433, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2.04938629, 4.84838525, 2.83959439, 1.21933811, 0.67835976, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
]

# Parse data and uncertainties
data_array = np.array(data)
uncertainty_array = np.array(uncertainties)
n_x, n_y = data_array.shape

# Create coordinate grids
x_coords = np.arange(n_x)
y_coords = np.arange(n_y)
X, Y = np.meshgrid(x_coords, y_coords, indexing='ij')

V = data_array
sigma = uncertainty_array
mask = V != 0.0

# Extract valid data with uncertainties
x_valid = X[mask]
y_valid = Y[mask]
v_valid = V[mask]
sigma_valid = sigma[mask]

print(f"Valid measurements: {len(v_valid)} out of {n_x * n_y}")
print(f"Velocity range: [{v_valid.min():.2f}, {v_valid.max():.2f}]")
print(f"Uncertainty range: [{sigma_valid.min():.2f}, {sigma_valid.max():.2f}]")

# Lamb-Oseen model
def lamb_oseen_horizontal_lda(xy, x0, y0, Gamma, rc):
    """Lamb-Oseen vortex with horizontal LDA measurement"""
    x, y = xy
    
    dx = x - x0
    dy = y - y0
    r = np.sqrt(dx**2 + dy**2)
    r = np.maximum(r, 1e-6)
    
    v_tangential = (Gamma / (2 * np.pi * r)) * (1 - np.exp(-r**2 / rc**2))
    theta = np.arctan2(dy, dx)
    v_measured = -v_tangential * np.sin(theta)
    
    return v_measured

# Initial parameter estimation using differential evolution
print("\nFinding initial parameters with differential evolution...")

def objective_weighted(params):
    """Weighted objective function"""
    try:
        v_pred = lamb_oseen_horizontal_lda((x_valid, y_valid), *params)
        weighted_residuals = (v_valid - v_pred) / sigma_valid
        return np.sum(weighted_residuals**2)
    except:
        return 1e10

bounds = [
    (-2, 5),      # x0
    (-2, 8),      # y0  
    (-50, 50),    # Gamma
    (0.1, 5),     # rc
]

result = differential_evolution(
    objective_weighted,
    bounds,
    maxiter=1000,
    popsize=15,
    tol=1e-7,
    seed=42,
    disp=True
)

if result.success:
    popt_initial = result.x
    print(f"Initial fit successful")
    
    # Refine with curve_fit using uncertainties
    print("\nRefining with weighted curve_fit...")
    try:
        popt, pcov = curve_fit(
            lamb_oseen_horizontal_lda,
            (x_valid, y_valid),
            v_valid,
            p0=popt_initial,
            sigma=sigma_valid,        # UNCERTAINTIES HERE!
            absolute_sigma=True,      # Use absolute uncertainties
            maxfev=10000
        )
        
        perr = np.sqrt(np.diag(pcov))
        x0_fit, y0_fit, Gamma_fit, rc_fit = popt
        
        print(f"\n{'='*60}")
        print(f"FITTED PARAMETERS (with uncertainties):")
        print(f"{'='*60}")
        print(f"  Vortex center X: {x0_fit:.4f} ± {perr[0]:.4f}")
        print(f"  Vortex center Y: {y0_fit:.4f} ± {perr[1]:.4f}")
        print(f"  Circulation Γ:   {Gamma_fit:.6f} ± {perr[2]:.6f}")
        print(f"  Core radius rc:  {rc_fit:.6f} ± {perr[3]:.6f}")
        
    except Exception as e:
        print(f"Refinement failed: {e}")
        print("Using differential evolution result")
        popt = popt_initial
        perr = np.array([0, 0, 0, 0])
        x0_fit, y0_fit, Gamma_fit, rc_fit = popt
    
    # Calculate fitted values and residuals
    v_fitted_valid = lamb_oseen_horizontal_lda((x_valid, y_valid), *popt)
    residuals = v_valid - v_fitted_valid
    weighted_residuals = residuals / sigma_valid
    
    # Chi-squared statistic
    chi_squared = np.sum(weighted_residuals**2)
    dof = len(v_valid) - 4  # degrees of freedom
    reduced_chi_squared = chi_squared / dof
    
    rmse = np.sqrt(np.mean(residuals**2))
    weighted_rmse = np.sqrt(np.mean(weighted_residuals**2))
    
    print(f"\nFIT QUALITY:")
    print(f"  RMSE: {rmse:.6f}")
    print(f"  Weighted RMSE: {weighted_rmse:.6f}")
    print(f"  χ²: {chi_squared:.4f}")
    print(f"  Reduced χ² (χ²/dof): {reduced_chi_squared:.4f}")
    if reduced_chi_squared < 1.5:
        print(f"  → Good fit! (reduced χ² close to 1)")
    elif reduced_chi_squared > 3:
        print(f"  → Poor fit or underestimated uncertainties")
    
    # Full grid prediction
    v_fitted_full = lamb_oseen_horizontal_lda((X, Y), *popt)
    


    # ENHANCED VISUALIZATION WITH UNCERTAINTIES
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # 1. Original measurements with error bars
    ax1 = fig.add_subplot(gs[0, 0])
    im1 = ax1.pcolormesh(X, Y, np.where(mask, V, np.nan), 
                         shading='auto', cmap='RdBu_r')
    # ax1.errorbar(x_valid, y_valid, xerr=None, yerr=None, 
    #              fmt='none', ecolor='black', elinewidth=1.5, capsize=3, alpha=0.5)
    ax1.plot(x0_fit, y0_fit, 'k+', markersize=20, markeredgewidth=3)
    
    ax1.set_xlabel('X position')
    ax1.set_ylabel('Y position')
    ax1.set_title('Original LDA Measurements')
    ax1.axis('equal')
    plt.colorbar(im1, ax=ax1, label='Velocity (m/s)')
    
    # 2. Fitted model
    ax2 = fig.add_subplot(gs[0, 1])
    im2 = ax2.pcolormesh(X, Y, v_fitted_full, shading='auto', cmap='RdBu_r')
    ax2.plot(x0_fit, y0_fit, 'k+', markersize=20, markeredgewidth=3)
    circle = plt.Circle((x0_fit, y0_fit), rc_fit, fill=False, 
                        color='yellow', linewidth=2, linestyle='--')
    ax2.add_patch(circle)
    ax2.scatter(x_valid, y_valid, c='gray', s=50, alpha=0.5, marker='x')
    ax2.set_xlabel('X position')
    ax2.set_ylabel('Y position')
    ax2.set_title(f'Fitted Lamb-Oseen (rc={rc_fit:.3f})')
    ax2.axis('equal')
    plt.colorbar(im2, ax=ax2, label='Velocity (m/s)')
    
    # 3. Uncertainties heatmap
    ax3 = fig.add_subplot(gs[0, 2])
    im3 = ax3.pcolormesh(X, Y, np.where(mask, sigma, np.nan), 
                         shading='auto', cmap='YlOrRd')
    ax3.plot(x0_fit, y0_fit, 'k+', markersize=20, markeredgewidth=3)
    ax3.set_xlabel('X position')
    ax3.set_ylabel('Y position')
    ax3.set_title('Measurement Uncertainties')
    ax3.axis('equal')
    plt.colorbar(im3, ax=ax3, label='Uncertainty (m/s)')
    
    # 4. Measured vs Fitted with error bars
    ax4 = fig.add_subplot(gs[1, 0])
    ax4.errorbar(v_valid, v_fitted_valid, xerr=sigma_valid, yerr=None,
                 fmt='o', alpha=0.6, markersize=8, ecolor='gray', 
                 elinewidth=1, capsize=3)
    min_v = min(v_valid.min(), v_fitted_valid.min())
    max_v = max(v_valid.max(), v_fitted_valid.max())
    ax4.plot([min_v, max_v], [min_v, max_v], 'r--', linewidth=2, label='Perfect fit')
    ax4.set_xlabel('Measured velocity (m/s)')
    ax4.set_ylabel('Fitted velocity (m/s)')
    ax4.set_title(f'Fit Quality (χ²/dof={reduced_chi_squared:.2f})')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    ax4.axis('equal')
    
    # 5. Residuals
    ax5 = fig.add_subplot(gs[1, 1])
    sc5 = ax5.scatter(x_valid, y_valid, c=residuals, s=200, 
                      cmap='RdBu_r', edgecolors='black', 
                      vmin=-max(abs(residuals)), vmax=max(abs(residuals)))
    ax5.plot(x0_fit, y0_fit, 'k+', markersize=20, markeredgewidth=3)
    ax5.set_xlabel('X position')
    ax5.set_ylabel('Y position')
    ax5.set_title('Residuals (Measured - Fitted)')
    ax5.axis('equal')
    ax5.grid(True, alpha=0.3)
    plt.colorbar(sc5, ax=ax5, label='Residual (m/s)')
    
    # 6. Weighted residuals (normalized by uncertainty)
    ax6 = fig.add_subplot(gs[1, 2])
    sc6 = ax6.scatter(x_valid, y_valid, c=weighted_residuals, s=200, 
                      cmap='RdBu_r', edgecolors='black', vmin=-3, vmax=3)
    ax6.plot(x0_fit, y0_fit, 'k+', markersize=20, markeredgewidth=3)
    ax6.axhline(0, color='k', linestyle='--', alpha=0.3)
    ax6.set_xlabel('X position')
    ax6.set_ylabel('Y position')
    ax6.set_title('Weighted Residuals (σ units)')
    ax6.axis('equal')
    ax6.grid(True, alpha=0.3)
    plt.colorbar(sc6, ax=ax6, label='(Meas-Fit)/σ')
    
    # 7. Residual distribution
    ax7 = fig.add_subplot(gs[2, 0])
    ax7.hist(weighted_residuals, bins=min(10, len(weighted_residuals)), 
             alpha=0.7, edgecolor='black')
    ax7.axvline(0, color='r', linestyle='--', linewidth=2)
    ax7.set_xlabel('Weighted Residual (σ units)')
    ax7.set_ylabel('Count')
    ax7.set_title('Residual Distribution')
    ax7.grid(True, alpha=0.3)
    
    # 8. Residuals vs fitted values
    ax8 = fig.add_subplot(gs[2, 1])
    ax8.errorbar(v_fitted_valid, residuals, yerr=sigma_valid, 
                 fmt='o', alpha=0.6, markersize=8, ecolor='gray',
                 elinewidth=1, capsize=3)
    ax8.axhline(0, color='r', linestyle='--', linewidth=2)
    ax8.set_xlabel('Fitted velocity (m/s)')
    ax8.set_ylabel('Residual (m/s)')
    ax8.set_title('Residuals vs Fitted Values')
    ax8.grid(True, alpha=0.3)
    
    # 9. Comparison table
    ax9 = fig.add_subplot(gs[2, 2])
    ax9.axis('off')
    table_data = []
    for i, (x, y, vm, vf, sig, res) in enumerate(zip(
            x_valid[:8], y_valid[:8], v_valid[:8], 
            v_fitted_valid[:8], sigma_valid[:8], weighted_residuals[:8])):
        table_data.append([f'{x:.1f}', f'{y:.1f}', 
                          f'{vm:.2f}±{sig:.2f}', 
                          f'{vf:.2f}', f'{res:.2f}'])
    
    table = ax9.table(cellText=table_data,
                     colLabels=['X', 'Y', 'Measured±σ', 'Fitted', 'σ units'],
                     cellLoc='center',
                     loc='center',
                     bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 2)
    ax9.set_title('Data Comparison (first 8 points)', pad=20)
    
    plt.suptitle(f'Lamb-Oseen Vortex Fit with Uncertainties\n' + 
                 f'Γ={Gamma_fit:.4f}±{perr[2]:.4f}, rc={rc_fit:.4f}±{perr[3]:.4f}, ' +
                 f'χ²/dof={reduced_chi_squared:.2f}',
                 fontsize=14, fontweight='bold')
    
    plt.show()
    
    # Print detailed comparison
    print(f"\n{'='*80}")
    print(f"DETAILED MEASUREMENT COMPARISON:")
    print(f"{'='*80}")
    print(f"{'X':>6} {'Y':>6} {'Measured':>12} {'Uncert':>10} {'Fitted':>12} "
          f"{'Residual':>12} {'Weighted':>10}")
    print(f"{'-'*80}")
    for x, y, vm, sig, vf, res, wres in zip(
            x_valid, y_valid, v_valid, sigma_valid, 
            v_fitted_valid, residuals, weighted_residuals):
        print(f"{x:6.2f} {y:6.2f} {vm:12.6f} {sig:10.6f} {vf:12.6f} "
              f"{res:12.6f} {wres:10.2f}")
    
else:
    print("Optimization failed!")