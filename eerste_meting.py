import numpy as np

# functie om v te berekenen bij bepaalde frequentie en afstanden
def bereken_v(x, y, z, f, delta_x, delta_y, delta_z, delta_f):
    theta = np.arctan((0.5*y - 0.5*z) / x)
    lamda = 632.8 * (10 ** -9)
    v = f * (lamda / (2 * np.sin(theta)))
    
    # bereken fout op theta
    u = (0.5 * y - 0.5 * z) / x
    dy = (0.5 * delta_y) / x
    dz = (0.5 * delta_z) / x
    dx = (0.5 * (y - z) * delta_x) / x**2
    delta_theta = (1 / (1 + u**2)) * np.sqrt(dx**2 + dy**2 + dz**2)

    # bereken fout op v
    delta_lamda = 0.1
    df = (lamda * delta_f) / 2 * np.sin(theta)
    dlamda = (f * delta_lamda) / 2* np.sin(theta)
    dtheta = (f * lamda * np.cos(theta) * delta_theta) / (2 * (np.sin(theta))**2)
    delta_v = np.sqrt(df**2 + dlamda**2 + dtheta**2)

    return theta, delta_theta, v, delta_v

print(bereken_v(97, 17, 2.5, 2836))
print(bereken_v(97, 17, 2.5, 2712))
print(bereken_v(97, 17, 2.5, 2133))