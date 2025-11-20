import sys

import numpy as np
from PySide6 import QtWidgets
import pyqtgraph as pg

#Sample array
data = np.random.normal(size=(5, 5))
data[40:80, 40:120] += 4
data = pg.gaussianFilter(data, (15, 15))
data += np.random.normal(size=(5, 5)) * 0.1
print(data)

#GUI control object
app = QtWidgets.QApplication(sys.argv)
#Window creation
window = pg.GraphicsLayoutWidget()
#Image object creation&Set image
image = pg.ImageItem()
image.setImage(data)
#Create a box to store images&Set image object
view_box = pg.ViewBox()
view_box.addItem(image)
#Plot object creation&View created above_set box
plot = pg.PlotItem(viewBox=view_box)
#Add plot to window
window.addItem(plot)
#Window display
window.show()
#The end of the program
sys.exit(app.exec_())