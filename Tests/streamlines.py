import numpy as np

def generate_high_res_vortex_field(x0, y0, Gamma, rc, 
                                   x_range=(0, 10), y_range=(0, 10), 
                                   resolution=50):
    """
    Generate high-resolution velocity field from fitted parameters
    
    Parameters:
    -----------
    x0, y0, Gamma, rc : fitted vortex parameters
    model_func : which vortex model to use
    x_range, y_range : (min, max) tuples for plot extent
    resolution : number of points in each direction
    
    Returns:
    --------
    X, Y : meshgrid coordinates
    Vx, Vy : velocity components
    V_mag : velocity magnitude
    """
    # Create fine grid
    x = np.linspace(x_range[0], x_range[1], resolution)
    y = np.linspace(y_range[0], y_range[1], resolution)
    X, Y = np.meshgrid(x, y)
    
    # Calculate full velocity field (not LDA projection!)
    dx = X - x0
    dy = Y - y0
    r = np.sqrt(dx**2 + dy**2)
    r = np.maximum(r, 1e-6)
    
    # Get tangential velocity magnitude from your model
    # (You need to modify your model functions to return v_tangential)
    theta = np.arctan2(dy, dx)
    
    # For Lamb-Oseen:
    v_tangential = (Gamma / (2 * np.pi * r)) * (1 - np.exp(-r**2 / rc**2))
    
    # Convert to Cartesian components
    # Tangential direction is perpendicular to radial
    Vx = -v_tangential * np.sin(theta)  # x-component
    Vy = v_tangential * np.cos(theta)   # y-component
    
    V_mag = np.sqrt(Vx**2 + Vy**2)
    
    return X, Y, Vx, Vy, V_mag


def lamb_oseen_tangential(r, Gamma, rc):
    """Returns tangential velocity magnitude (not LDA projection)"""
    r = np.maximum(r, 1e-6)
    return (Gamma / (2 * np.pi * r)) * (1 - np.exp(-r**2 / rc**2))

def get_velocity_field(X, Y, x0, y0, Gamma, rc, model='lamb_oseen'):
    """
    Calculate full 2D velocity field
    
    Returns Vx, Vy components
    """
    dx = X - x0
    dy = Y - y0
    r = np.sqrt(dx**2 + dy**2)
    theta = np.arctan2(dy, dx)
    
    # Choose model
    if model == 'lamb_oseen':
        v_tang = lamb_oseen_tangential(r, Gamma, rc)

    
    # Convert to Cartesian
    Vx = -v_tang * np.sin(theta)
    Vy = v_tang * np.cos(theta)
    
    return Vx, Vy


import matplotlib.pyplot as plt

x0_fit = 5
y0_fit = 5
Gamma_fit = -79.69
rc_fit = 2

X, Y, Vx, Vy, V_mag = generate_high_res_vortex_field(
    x0_fit, y0_fit, Gamma_fit, rc_fit, 
    resolution=50
)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Vector plot (quiver)
ax1 = axes[0]
ax1.quiver(X[::3, ::3], Y[::3, ::3], 
           Vx[::3, ::3], Vy[::3, ::3],
           V_mag[::3, ::3],  # Color by magnitude
           cmap='viridis',
           scale=50)  # Adjust for arrow length
ax1.plot(x0_fit, y0_fit, 'r+', markersize=20, markeredgewidth=3)
ax1.set_aspect('equal')
ax1.set_title('Vector Field')

# Streamlines
ax2 = axes[1]
ax2.streamplot(X, Y, Vx, Vy, 
               color=V_mag, 
               cmap='viridis',
               density=2,
               linewidth=1)
ax2.plot(x0_fit, y0_fit, 'r+', markersize=20, markeredgewidth=3)
ax2.set_aspect('equal')
ax2.set_title('Streamlines')

plt.tight_layout()
plt.show()