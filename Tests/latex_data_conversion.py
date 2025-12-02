import numpy as np

data = np.loadtxt('EXPORT_fitted_full_data.csv', delimiter=',')
with open('data_xyz.csv', 'w') as f:
    f.write('x,y,z\n')
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            f.write(f'{j},{i},{data[i,j]}\n')
        f.write('\n')  # blank line between rows (required by pgfplots)