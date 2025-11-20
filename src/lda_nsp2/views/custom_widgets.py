from colour import Color
import numpy as np
from PySide6 import QtWidgets
import pyqtgraph as pg
from pgcolorbar.colorlegend import ColorLegendItem


class HeatMapWidget(QtWidgets.QGraphicsWidget):
    def __init__(self, title="", bar_label=""):
        super(HeatMapWidget, self).__init__()

        self.layout = QtWidgets.QGraphicsGridLayout()

        blue, red = Color("blue"), Color("red")
        colors = blue.range_to(red, 256)
        colors_array = np.array([np.array(color.get_rgb()) * 255 for color in colors])
        look_up_table = colors_array.astype(np.uint8)

        self.image = pg.ImageItem()
        self.image.setOpts(axisOrder="row-major")
        self.image.setLookupTable(look_up_table)

        view_box = pg.ViewBox()
        view_box.setAspectLocked(lock=True)
        view_box.addItem(self.image)

        self.plot = pg.PlotItem(viewBox=view_box)

        color_bar = ColorLegendItem(
            imageItem=self.image, showHistogram=True, label="sample"
        )
        color_bar.setImageItem(self.image)

        self.layout.setContentsMargins(1, 1, 1, 1)
        self.layout.setSpacing(0)
        self.layout.addItem(self.plot, 0, 0)
        self.layout.addItem(color_bar, 0, 1)

        self.setLayout(self.layout)

    def set_image(self, image):
        self.image.setImage(image)
