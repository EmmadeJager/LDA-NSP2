# Test-code voor de heatmap

import sys

from colour import Color
import numpy as np
from pgcolorbar.colorlegend import ColorLegendItem
from PySide6 import QtWidgets
import pyqtgraph as pg

# Sample array
data = np.random.normal(size=(200, 200))
data[40:80, 40:120] += 4
data = pg.gaussianFilter(data, (15, 15))
data += np.random.normal(size=(200, 200)) * 0.1

app = QtWidgets.QApplication(sys.argv)

window = pg.GraphicsLayoutWidget()

blue, red = Color("blue"), Color("red")
colors = blue.range_to(red, 256)
colors_array = np.array([np.array(color.get_rgb()) * 255 for color in colors])
look_up_table = colors_array.astype(np.uint8)

image = pg.ImageItem()
image.setOpts(axisOrder="row-major")  # 2021/01/19 Add
image.setLookupTable(look_up_table)
image.setImage(data)

view_box = pg.ViewBox()
view_box.setAspectLocked(lock=True)
view_box.addItem(image)

plot = pg.PlotItem(viewBox=view_box)

color_bar = ColorLegendItem(
    imageItem=image, showHistogram=True, label="sample"
)  # 2021/01/20 add label
color_bar.setImageItem(image)

window.addItem(plot)
window.addItem(color_bar)

window.show()

sys.exit(app.exec_())
