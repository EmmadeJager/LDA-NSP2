import numpy as np

# functie om v te berekenen bij bepaalde frequentie en afstanden
def bereken_v(x, y, z, f, delta_x, delta_y, delta_z, FMWH):
    theta = np.arctan((0.5*y - 0.5*z) / x)
    lamda = 632.8 * (10 ** -9)
    v = f * (lamda / (2 * np.sin(theta)))
    
    # bereken fout op theta
    u = ((0.5 * y) - (0.5 * z)) / x
    dy = (0.5 * delta_y) / x
    dz = (0.5 * delta_z) / x
    dx = (0.5 * (y - z) * delta_x) / (x**2)
    delta_theta = (1 / (1 + u**2)) * np.sqrt(dx**2 + dy**2 + dz**2)

    # bereken fout op frequentie
    delta_f = FMWH / (2 * np.sqrt(2*np.log(2)))

    # bereken fout op v
    delta_lamda = 0.1
    df = (lamda * delta_f) / (2 * np.sin(theta))
    dlamda = (f * delta_lamda) / (2* np.sin(theta))
    dtheta = (f * lamda * np.cos(theta) * delta_theta) / (2 * (np.sin(theta))**2)
    delta_v = np.sqrt(df**2 + dlamda**2 + dtheta**2)

    print(f"v ={v}")
    print(f"error_v ={delta_v}")

    return theta, delta_theta, v, delta_v

print(bereken_v(0.097, 0.021, 0.0025, 2345.60, 0.001, 0.001, 0.001, 754.62))