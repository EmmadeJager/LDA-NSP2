import sys
from colour import Color
from pgcolorbar.colorlegend import ColorLegendItem

import pyqtgraph as pg
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QListWidgetItem, QDialog
from rich import print
import numpy as np
from lda_nsp2.data_ingestion import Ingest_Data, Ingest_Data_1D
from lda_nsp2.models.fitting import gaussfit, parabfit
from lda_nsp2.models.velocitycalculation import bereken_v
from lda_nsp2.views.lda_designer_gui import Ui_MainWindow
from lda_nsp2.views.lda_vortex_histogram_edit_dialog import Ui_Dialog
from lda_nsp2.models.filters import lowpass, highpass

pg.setConfigOption("background", 0.2)
pg.setConfigOption("foreground", 0.5)


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = None
        self.fit_C = None

        self.parabola_list_velo = []
        self.parabola_list_velo_uncertainty = []

        self.parabola_list_depth = []

        self.current_velocity_result = None
        self.current_velocity_uncertainty = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.import_button.clicked.connect(self.ingest_data_to_gui)
        self.ui.fit_button.clicked.connect(self.do_fit)

        self.ui.calculate_velocity_button.clicked.connect(self.calc_velocity)

        self.ui.param1_fit_output_label.setEnabled(False)
        self.ui.param2_fit_output_label.setEnabled(False)
        self.ui.param3_fit_output_label.setEnabled(False)

        self.ui.refraction_correction_checkbox.stateChanged.connect(
            self.check_refraction_checkbox
        )

        self.ui.add_to_table_button.clicked.connect(self.add_to_table)
        self.ui.parabola_fit_button.clicked.connect(self.parabola_fit)
        self.ui.graphicsView.showGrid(x=True, y=True, alpha=0.9)
        self.ui.graphicsView_2.showGrid(x=True, y=True, alpha=0.9)
        # self.ui.graphicsView_3.showGrid(x=True, y=True, alpha=0.9)

        # Initialise a hashtable for 200 different vortex measurements
        self.vortex_master_data = []
        for i in range(200):
            self.vortex_master_data.append(None)

        self.currently_selected_vortex_histogram = None

        # Vortex Button Bindings
        self.ui.ImportSingleButton.clicked.connect(self.ingest_vortex_histogram)
        self.ui.ImportMultipleButton.clicked.connect(
            self.ingest_multiple_vortex_histograms
        )
        self.ui.DeleteSelectedHistogramButton.clicked.connect(
            self.delete_vortex_histogram
        )
        self.ui.EditSelectedHistogramButton.clicked.connect(self.edit_vortex_histogram)

        self.ui.LowPassFilterCheckBox.stateChanged.connect(self.applylowpassfilter)
        self.ui.LowPassFilterK_value_Spinbox.valueChanged.connect(
            self.applylowpassfilter
        )
        self.ui.LowPassFilterSpinbox.valueChanged.connect(self.applylowpassfilter)

        self.ui.HighPassFilterCheckBox.stateChanged.connect(self.applyHighpassfilter)
        self.ui.HighPassFilterK_value_Spinbox.valueChanged.connect(
            self.applyHighpassfilter
        )
        self.ui.HighPassFilterSpinbox.valueChanged.connect(self.applyHighpassfilter)

        self.ui.SaveHistogramButton.clicked.connect(self.saveCurrentHistogram)

        self.ui.listWidget.currentItemChanged.connect(self.redraw_vortex_histogram)

        self.ui.Fit_All_Histograms_Button.clicked.connect(self.fitAllHistograms)

        self.ui.comboBox.currentTextChanged.connect(self.plotHeatMap)

    @Slot()
    def ingest_data_to_gui(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, ("Import data"), "")
        print(fileName)

        experiment = Ingest_Data(fileName[0])
        self.data = experiment.returndata()

        self.ui.graphicsView.clear()
        self.ui.graphicsView.plot(self.data[0], self.data[1], pen=None, symbol="o")

        self.ui.param1_guess_spinbox.setValue(max(self.data[1]))
        self.ui.param2_guess_spinbox.setValue(1 / (2 * 100**2))
        self.ui.param3_guess_spinbox.setValue(
            self.data[0][self.data[1].index(max(self.data[1]))]
        )

    @Slot()
    def do_fit(self):
        if not self.data:
            self.error_modal("Please import data before fitting.")
            return

        A_guess = self.ui.param1_guess_spinbox.value()
        B_guess = self.ui.param2_guess_spinbox.value()
        C_guess = self.ui.param3_guess_spinbox.value()

        fit_data = gaussfit(self.data[0], self.data[1], A_guess, B_guess, C_guess)

        self.fit_A = fit_data[0]
        self.fit_B = fit_data[1]
        self.fit_C = fit_data[2]

        self.ui.param1_fit_output_label.setEnabled(True)
        self.ui.param2_fit_output_label.setEnabled(True)
        self.ui.param3_fit_output_label.setEnabled(True)

        self.ui.param1_fit_output_label.setText(str(self.fit_A)[0:10])
        self.ui.param2_fit_output_label.setText(str(self.fit_B)[0:10])
        self.ui.param3_fit_output_label.setText(str(self.fit_C)[0:10])

        self.ui.graphicsView.plot(self.data[0], fit_data[3])

    @Slot()
    def calc_velocity(self):
        if not self.fit_C:
            self.error_modal("Please fit before calculating the velocity.")
            return

        x = self.ui.x_measurement_spinbox.value()
        y = self.ui.y_measurement_spinbox.value()
        z = self.ui.z_measurement_spinbox.value()
        f = self.fit_C

        x_err = self.ui.x_uncertainty_spinbox.value()
        y_err = self.ui.y_uncertainty_spinbox.value()
        z_err = self.ui.z_uncertainty_spinbox.value()
        f_err = 100

        results = bereken_v(x, y, z, f, x_err, y_err, z_err, f_err)

        self.ui.velocity_lcd.display(results[2])
        self.ui.velocity_lcd_uncertainty.display(results[3])

        self.current_velocity_result = results[2]
        self.current_velocity_uncertainty = results[3]

    def error_modal(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(text)
        msg.setWindowTitle("Error")
        msg.exec_()

    @Slot()
    def check_refraction_checkbox(self):
        self.ui.refraction_coefficient_spinbox.setEnabled(
            self.ui.refraction_correction_checkbox.isChecked()
        )
        self.ui.refraction_coefficient_spinbox.setEnabled(
            self.ui.refraction_correction_checkbox.isChecked()
        )

    @Slot()
    def add_to_table(self):
        if not self.current_velocity_result:
            self.error_modal("Please calculate measurement before adding to table.")
            return
        # for i in range(0, 10):
        #     if self.ui.tableWidget.item

        # self.ui.tableWidget.setItem()
        self.parabola_list_velo.append(self.current_velocity_result)
        self.parabola_list_velo_uncertainty.append(self.current_velocity_uncertainty)

        self.parabola_list_depth.append(self.ui.measurement_depth_spinbox.value())

        self.ui.graphicsView_2.clear()
        self.ui.graphicsView_2.plot(
            self.parabola_list_depth, self.parabola_list_velo, pen=None, symbol="o"
        )

    @Slot()
    def parabola_fit(self):
        results = parabfit(
            self.parabola_list_depth, self.parabola_list_velo, -1, -2, 10
        )
        parab_fit_A, parab_fit_B, parab_fit_C, parab_fit_Y, parab_fit_X = results

        self.ui.graphicsView_2.plot(parab_fit_X, parab_fit_Y)

        print(parab_fit_A, parab_fit_B, parab_fit_C)

    @Slot()
    def ingest_vortex_histogram(self):
        # Open file-choosing modal
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, ("Import data"), "")
        print(fileName)

        # Ingest data and make it a histogram
        vals = Ingest_Data_1D(fileName)
        hist_data = vals.returndata()
        y, x = np.histogram(hist_data, bins=32)

        self.current_histogram_x = x
        self.current_histogram_y = y

        self.plothistogram(x, y)

        # Name of file without preceding path
        fileNameWOPath = fileName.split("/")[-1]

        # Add Name of file to list widget
        QListWidgetItem((fileNameWOPath), self.ui.listWidget)

        fileCoords = fileNameWOPath.split(" ")[0]
        fileCoords = list(fileCoords)[1:-1]
        fileCoordsNumbers = ""
        for i in fileCoords:
            fileCoordsNumbers += i

        fileCoords = [int(i) for i in fileCoordsNumbers.split(",")]

        x_value = 50 + 22 + 8.5 * fileCoords[1]
        y_value = 18.5
        if fileCoords[1] == 0:
            z = 6.5
        elif fileCoords[1] == 1:
            z = 5.5
        elif fileCoords[1] == 2:
            z = 4
        elif fileCoords[1] == 3:
            z = 2.5
        elif fileCoords[1] == 4:
            z = 1.5

        fileCoords.append(x_value)
        fileCoords.append(y_value)
        fileCoords.append(z)

        # save histogram to memory
        hashTableAddress = int(list(fileNameWOPath)[-2] + list(fileNameWOPath)[-1])
        self.vortex_master_data[hashTableAddress] = [[x, y], fileCoords]

    @Slot()
    def ingest_multiple_vortex_histograms(self):
        # Open file-choosing modal
        fileNames = QtWidgets.QFileDialog.getOpenFileNames(self, ("Import data"), "")

        for fileName in fileNames[0]:
            # Ingest data and make it a histogram
            vals = Ingest_Data_1D(fileName)
            hist_data = vals.returndata()
            y, x = np.histogram(hist_data, bins=32)

            self.current_histogram_x = x
            self.current_histogram_y = y

            self.plothistogram(x, y)

            # Name of file without preceding path
            fileNameWOPath = fileName.split("/")[-1]

            # Add Name of file to list widget
            QListWidgetItem((fileNameWOPath), self.ui.listWidget)

            fileCoords = fileNameWOPath.split(" ")[0]
            fileCoords = list(fileCoords)[1:-1]
            fileCoordsNumbers = ""
            for i in fileCoords:
                fileCoordsNumbers += i

            fileCoords = [int(i) for i in fileCoordsNumbers.split(",")]

            x_value = 50 + 22 + 8.5 * fileCoords[1]
            y_value = 18.5
            if fileCoords[1] == 0:
                z = 6.5
            elif fileCoords[1] == 1:
                z = 5.5
            elif fileCoords[1] == 2:
                z = 4
            elif fileCoords[1] == 3:
                z = 2.5
            elif fileCoords[1] == 4:
                z = 1.5

            fileCoords.append(x_value)
            fileCoords.append(y_value)
            fileCoords.append(z)

            print(fileCoords)
            # save histogram to memory
            hashTableAddress = int(list(fileNameWOPath)[-2] + list(fileNameWOPath)[-1])
            self.vortex_master_data[hashTableAddress] = [[x, y], fileCoords]
            self.currently_selected_vortex_histogram = hashTableAddress

    @Slot()
    def redraw_vortex_histogram(self, reset_filters=True):
        datasetName = self.ui.listWidget.currentItem().text()

        datasetIndex = int(list(datasetName)[-2] + list(datasetName)[-1])
        self.currently_selected_vortex_histogram = datasetIndex

        HistogramList = self.vortex_master_data[datasetIndex]
        x = HistogramList[0][0]
        y = HistogramList[0][1]

        self.current_histogram_x = x
        self.current_histogram_y = y

        self.plothistogram(x, y, reset_filters)

    @Slot()
    def delete_vortex_histogram(self):
        self.vortex_master_data[self.currently_selected_vortex_histogram] = None

        currentRow = self.ui.listWidget.currentRow()
        self.ui.listWidget.takeItem(currentRow)

    def edit_vortex_histogram(self):
        dlg = HistogramEditDialog(self)
        dlg.exec()

    def plothistogram(self, x, y, reset_filters=True):
        # set plot limits
        self.ui.HistoStartRangeSpinbox.setValue(x[0])
        self.ui.HistoEndRangeSpinbox.setValue(x[-1])

        if reset_filters:
            # set filter frequencies
            self.ui.HighPassFilterSpinbox.setValue(x[0])
            self.ui.LowPassFilterSpinbox.setValue(x[-1])
            self.ui.HighPassFilterCheckBox.setChecked(False)
            self.ui.LowPassFilterCheckBox.setChecked(False)

        # Graph selected Histogram
        self.ui.graphicsView_3.clear()
        self.ui.graphicsView_3.setXRange(x[0], x[-1], padding=0.05)
        bgi = pg.BarGraphItem(
            x0=x[:-1], x1=x[1:], height=y, pen="w", brush=(16, 3, 0, 255)
        )
        self.ui.graphicsView_3.addItem(bgi)

    def applylowpassfilter(self):
        if self.ui.LowPassFilterCheckBox.isChecked():
            x = self.current_histogram_x
            y = self.current_histogram_y

            # filter histogram according to high and lowpass filter
            filtered_y = []
            for i, j in zip(x, y):
                # apply lowpass
                filtered_y_value = j * lowpass(
                    i,
                    self.ui.LowPassFilterSpinbox.value(),
                    self.ui.LowPassFilterK_value_Spinbox.value(),
                )

                # apply highpass if enabled
                if self.ui.HighPassFilterCheckBox.isChecked():
                    filtered_y_value = filtered_y_value * highpass(
                        i,
                        self.ui.HighPassFilterSpinbox.value(),
                        self.ui.HighPassFilterK_value_Spinbox.value(),
                    )
                filtered_y.append(filtered_y_value)

            # generate plot of lowpass function
            filterplot_range = np.arange(x[0], x[-1], 1)
            filterplot_y = []
            for i in filterplot_range:
                filterplot_y.append(
                    lowpass(
                        i,
                        self.ui.LowPassFilterSpinbox.value(),
                        self.ui.LowPassFilterK_value_Spinbox.value(),
                    )
                    * max(y)
                )

            # plot histogram and lowpass function
            self.plothistogram(x, filtered_y, False)
            self.current_histogram_filtered_y = filtered_y
            self.ui.graphicsView_3.plot(filterplot_range, filterplot_y, pen="r")

            # if highpass is enabled also plot that function
            if self.ui.HighPassFilterCheckBox.isChecked():
                filterplot_y_highpass = []
                for i in filterplot_range:
                    filterplot_y_highpass.append(
                        highpass(
                            i,
                            self.ui.HighPassFilterSpinbox.value(),
                            self.ui.HighPassFilterK_value_Spinbox.value(),
                        )
                        * max(y)
                    )

                self.ui.graphicsView_3.plot(
                    filterplot_range, filterplot_y_highpass, pen="g"
                )
        else:
            # if lowpass is disabled but highpass is enabled redraw that highpass function
            self.redraw_vortex_histogram(False)
            if self.ui.HighPassFilterCheckBox.isChecked():
                filterplot_y_highpass = []
                for i in filterplot_range:
                    filterplot_y_highpass.append(
                        highpass(
                            i,
                            self.ui.HighPassFilterSpinbox.value(),
                            self.ui.HighPassFilterK_value_Spinbox.value(),
                        )
                        * max(y)
                    )

                self.ui.graphicsView_3.plot(
                    filterplot_range, filterplot_y_highpass, pen="g"
                )

    def applyHighpassfilter(self):
        if self.ui.HighPassFilterCheckBox.isChecked():
            x = self.current_histogram_x
            y = self.current_histogram_y

            # filter histogram according to high and lowpass filter
            filtered_y = []
            for i, j in zip(x, y):
                # apply highpass filter
                filtered_y_value = j * highpass(
                    i,
                    self.ui.HighPassFilterSpinbox.value(),
                    self.ui.HighPassFilterK_value_Spinbox.value(),
                )

                # apply lowpass if enabled
                if self.ui.LowPassFilterCheckBox.isChecked():
                    filtered_y_value = filtered_y_value * lowpass(
                        i,
                        self.ui.LowPassFilterSpinbox.value(),
                        self.ui.LowPassFilterK_value_Spinbox.value(),
                    )
                filtered_y.append(filtered_y_value)

            # generate plot of highpass function
            filterplot_range = np.arange(x[0], x[-1], 1)
            filterplot_y = []
            for i in filterplot_range:
                filterplot_y.append(
                    highpass(
                        i,
                        self.ui.HighPassFilterSpinbox.value(),
                        self.ui.HighPassFilterK_value_Spinbox.value(),
                    )
                    * max(y)
                )

            # plot histogram and highpass function
            self.plothistogram(x, filtered_y, False)
            self.current_histogram_filtered_y = filtered_y
            self.ui.graphicsView_3.plot(filterplot_range, filterplot_y, pen="g")

            # if lowpass is enabled also plot that function
            if self.ui.LowPassFilterCheckBox.isChecked():
                filterplot_y_lowpass = []
                for i in filterplot_range:
                    filterplot_y_lowpass.append(
                        lowpass(
                            i,
                            self.ui.LowPassFilterSpinbox.value(),
                            self.ui.LowPassFilterK_value_Spinbox.value(),
                        )
                        * max(y)
                    )

                self.ui.graphicsView_3.plot(
                    filterplot_range, filterplot_y_lowpass, pen="r"
                )
        else:
            # if highpass is disabled but lowpass is enabled redraw that lowpass function
            self.redraw_vortex_histogram(False)
            if self.ui.LowPassFilterCheckBox.isChecked():
                filterplot_y_lowpass = []
                for i in filterplot_range:
                    filterplot_y_lowpass.append(
                        lowpass(
                            i,
                            self.ui.LowPassFilterSpinbox.value(),
                            self.ui.LowPassFilterK_value_Spinbox.value(),
                        )
                        * max(y)
                    )

                self.ui.graphicsView_3.plot(
                    filterplot_range, filterplot_y_lowpass, pen="r"
                )

    @Slot()
    def saveCurrentHistogram(self):
        index = self.currently_selected_vortex_histogram

        self.current_histogram_y = self.current_histogram_filtered_y
        self.vortex_master_data[index][0][1] = self.current_histogram_filtered_y

    @Slot()
    def fitAllHistograms(self):
        self.velocitylist = []
        for i in range(200):
            velocity_grid = []
            for i in range(10):
                velocity_line = []
                for j in range(10):
                    velocity_line.append(None)
                velocity_grid.append(velocity_line)
            self.velocitylist.append(velocity_grid)

        self.velocity_err_list = self.velocitylist

        available_heights = []

        for histogram in self.vortex_master_data:
            if histogram is not None:
                x = list(histogram[0][0])
                x.pop(-1)

                y = list(histogram[0][1])

                # print(f"{x} len = {len(x)}")
                # print(f"{y} len = {len(y)}")
                metadata = histogram[1]
                D = metadata[0]
                R = metadata[1]
                H = metadata[2]

                if H not in available_heights:
                    available_heights.append(H)
                    available_heights.sort()

                x_meas = metadata[3]
                y_meas = metadata[4]
                z_meas = metadata[5]

                A_Guess = max(y)
                B_Guess = 0.0005
                C_Guess = x[y.index(max(y))]

                fit_data = gaussfit(
                    x, y, A_guess=A_Guess, B_guess=B_Guess, C_guess=C_Guess
                )

                fit_A = fit_data[0]
                fit_C = fit_data[2]

                x_err = 0.1
                y_err = 0.1
                z_err = 0.1

                f_err = 1 / (fit_A * np.sqrt(2 * np.pi))

                velocity_data = bereken_v(
                    x=x_meas,
                    y=y_meas,
                    z=z_meas,
                    f=fit_C,
                    delta_x=x_err,
                    delta_y=y_err,
                    delta_z=z_err,
                    delta_f=f_err,
                )

                self.velocitylist[H][D][R] = velocity_data[2]
                self.velocity_err_list[H][D][R] = velocity_data[3]

        for i in range(len(available_heights)):
            available_heights[i] = str(available_heights[i]) + "mm"

        self.ui.comboBox.addItems(available_heights)

    @Slot()
    def plotHeatMap(self):
        currentDepth = int(self.ui.comboBox.currentText()[:-2])
        data = self.velocitylist[currentDepth]

        # mask_r = (data != None).any(axis=1)
        # mask_c = (data != None).any(axis=0)

        # data = data[mask_r][:, mask_c]

        # data = list(data)

        for row in range(len(data)):
            for column in range(len(data[row])):
                if data[row][column] is None:
                    data[row][column] = 0.0
                else:
                    data[row][column] = float(data[row][column])

        data = np.array(data)
        print(data)

        blue, red = Color("blue"), Color("red")
        colors = blue.range_to(red, 256)
        colors_array = np.array([np.array(color.get_rgb()) * 255 for color in colors])
        look_up_table = colors_array.astype(np.uint8)

        image = pg.ImageItem()
        image.setOpts(axisOrder="row-major")
        image.setLookupTable(look_up_table)
        image.setImage(data)

        view_box = pg.ViewBox()
        view_box.setAspectLocked(lock=True)
        view_box.addItem(image)

        plot = pg.PlotItem(viewBox=view_box)

        color_bar = ColorLegendItem(
            imageItem=image, showHistogram=True, label="sample"
        ) 
        color_bar.setImageItem(image)

        self.ui.heatMapView.addItem(plot)
        self.ui.heatMapView.addItem(color_bar)

        self.ui.heatMapView.show()


class HistogramEditDialog(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    # def add_values(self, x_value, y_value, z_value, x_list, y_list):
    #     self.s =


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
