# test code voor het simuleren van een kloppend stroomprofiel (circulair)

import sys
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets, QtCore
from scipy.interpolate import RegularGridInterpolator

class StreamlinePlot(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Vortex Streamline Plot with Arrows')
        self.resize(1000, 800)
        
        # Layout
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        
        # Graphics layout for plots
        self.graphics_layout = pg.GraphicsLayoutWidget()
        layout.addWidget(self.graphics_layout)
        
        # Create plot
        self.plot = self.graphics_layout.addPlot(title="Lamb-Oseen Vortex Streamlines")
        self.plot.setAspectLocked(True)
        self.plot.setLabel('left', 'Y position')
        self.plot.setLabel('bottom', 'X position')
        
        # Generate and plot vortex
        self.generate_and_plot_vortex()
        
    def generate_vortex_field(self, x0=5, y0=5, Gamma=10, rc=1.0, 
                             x_range=(0, 10), y_range=(0, 10), 
                             resolution=100):
        """Generate high-resolution velocity field"""
        x = np.linspace(x_range[0], x_range[1], resolution)
        y = np.linspace(y_range[0], y_range[1], resolution)
        X, Y = np.meshgrid(x, y)
        
        # Calculate velocity field
        dx = X - x0
        dy = Y - y0
        r = np.sqrt(dx**2 + dy**2)
        r = np.maximum(r, 1e-6)
        
        # Lamb-Oseen tangential velocity
        v_tangential = (Gamma / (2 * np.pi * r)) * (1 - np.exp(-r**2 / rc**2))
        
        # Angle from vortex center
        theta = np.arctan2(dy, dx)
        
        # Convert to Cartesian components
        Vx = -v_tangential * np.sin(theta)
        Vy = v_tangential * np.cos(theta)
        
        V_mag = np.sqrt(Vx**2 + Vy**2)
        
        return x, y, X, Y, Vx, Vy, V_mag, x0, y0, rc
    
    def compute_streamline(self, x_start, y_start, x, y, Vx, Vy, 
                          n_steps=200, step_size=0.05):
        """Compute a single streamline using RK4 integration"""
        # Create interpolators for velocity components
        interp_vx = RegularGridInterpolator((y, x), Vx, 
                                            bounds_error=False, 
                                            fill_value=0)
        interp_vy = RegularGridInterpolator((y, x), Vy, 
                                            bounds_error=False, 
                                            fill_value=0)
        
        # Initialize streamline
        streamline = np.zeros((n_steps, 2))
        streamline[0] = [x_start, y_start]
        
        # RK4 integration
        for i in range(1, n_steps):
            x_curr, y_curr = streamline[i-1]
            
            # RK4 coefficients
            k1_x = interp_vx([y_curr, x_curr])[0]
            k1_y = interp_vy([y_curr, x_curr])[0]
            
            k2_x = interp_vx([y_curr + 0.5*step_size*k1_y, 
                             x_curr + 0.5*step_size*k1_x])[0]
            k2_y = interp_vy([y_curr + 0.5*step_size*k1_y, 
                             x_curr + 0.5*step_size*k1_x])[0]
            
            k3_x = interp_vx([y_curr + 0.5*step_size*k2_y, 
                             x_curr + 0.5*step_size*k2_x])[0]
            k3_y = interp_vy([y_curr + 0.5*step_size*k2_y, 
                             x_curr + 0.5*step_size*k2_x])[0]
            
            k4_x = interp_vx([y_curr + step_size*k3_y, 
                             x_curr + step_size*k3_x])[0]
            k4_y = interp_vy([y_curr + step_size*k3_y, 
                             x_curr + step_size*k3_x])[0]
            
            # Update position
            x_new = x_curr + (step_size/6) * (k1_x + 2*k2_x + 2*k3_x + k4_x)
            y_new = y_curr + (step_size/6) * (k1_y + 2*k2_y + 2*k3_y + k4_y)
            
            # Check if out of bounds
            if (x_new < x[0] or x_new > x[-1] or 
                y_new < y[0] or y_new > y[-1]):
                streamline = streamline[:i]
                break
            
            streamline[i] = [x_new, y_new]
        
        return streamline
    
    def add_arrows_to_streamline(self, streamline, n_arrows=3, 
                                 arrow_size=15, arrow_color='w'):
        """
        Add arrows along a streamline to show direction
        
        Parameters:
        -----------
        streamline : array of (x, y) coordinates
        n_arrows : number of arrows to place
        arrow_size : size of arrow heads
        arrow_color : color of arrows
        """
        if len(streamline) < 2:
            return
        
        # Select evenly spaced points along streamline for arrows
        indices = np.linspace(10, len(streamline)-10, n_arrows, dtype=int)
        
        for idx in indices:
            if idx >= len(streamline) - 1:
                continue
                
            # Get position
            x_pos, y_pos = streamline[idx]
            
            # Calculate direction (use next point)
            dx = streamline[idx+1, 0] - streamline[idx, 0]
            dy = streamline[idx+1, 1] - streamline[idx, 1]
            
            # Calculate angle in degrees
            angle = np.degrees(np.arctan2(dy, dx))
            
            # Create arrow
            arrow = pg.ArrowItem(
                angle=angle,
                pos=(x_pos, y_pos),
                headLen=arrow_size,
                headWidth=arrow_size * 0.8,
                tipAngle=40,
                baseAngle=20,
                brush=arrow_color,
                pen=pg.mkPen(arrow_color, width=1.5)
            )
            
            self.plot.addItem(arrow)
    
    def generate_and_plot_vortex(self):
        """Generate vortex field and plot streamlines with arrows"""
        
        # Generate velocity field
        x, y, X, Y, Vx, Vy, V_mag, x0, y0, rc = self.generate_vortex_field(
            x0=5, y0=5, Gamma=10, rc=1.5,
            resolution=150
        )
        
        # Add background heatmap of velocity magnitude
        img = pg.ImageItem()
        img.setImage(V_mag.T, levels=[0, np.nanmax(V_mag)])
        img.setRect(QtCore.QRectF(x[0], y[0], x[-1]-x[0], y[-1]-y[0]))
        
        # Use a nice colormap
        colormap = pg.colormap.get('viridis')
        img.setLookupTable(colormap.getLookupTable())
        
        self.plot.addItem(img)
        
        # Generate starting points for streamlines
        n_angles = 12
        radii = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
        
        print("Computing streamlines...")
        streamline_count = 0
        
        for radius in radii:
            angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
            for angle in angles:
                x_start = x0 + radius * np.cos(angle)
                y_start = y0 + radius * np.sin(angle)
                
                # Compute streamline
                streamline = self.compute_streamline(
                    x_start, y_start, x, y, Vx, Vy,
                    n_steps=300, step_size=0.04
                )
                
                if len(streamline) > 2:
                    # Plot streamline
                    self.plot.plot(
                        streamline[:, 0], 
                        streamline[:, 1],
                        pen=pg.mkPen('w', width=1.5, alpha=180)
                    )
                    
                    # Add arrows to streamline
                    self.add_arrows_to_streamline(
                        streamline, 
                        n_arrows=2,  # Number of arrows per streamline
                        arrow_size=12,
                        arrow_color='yellow'
                    )
                    
                    streamline_count += 1
        
        print(f"Plotted {streamline_count} streamlines")
        
        # Mark vortex center
        self.plot.plot(
            [x0], [y0], 
            symbol='+', 
            symbolSize=25, 
            symbolPen=pg.mkPen('r', width=3),
            symbolBrush=None
        )
        
        # Draw core radius circle
        circle = QtWidgets.QGraphicsEllipseItem(
            x0 - rc, y0 - rc,
            2*rc, 2*rc
        )
        circle.setPen(pg.mkPen('y', width=2, style=QtCore.Qt.DashLine))
        self.plot.addItem(circle)
        
        # Add colorbar
        colorbar = pg.ColorBarItem(
            values=(0, np.nanmax(V_mag)),
            colorMap=colormap,
            label='Velocity magnitude'
        )
        colorbar.setImageItem(img)
        self.graphics_layout.addItem(colorbar, row=0, col=1)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = StreamlinePlot()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()