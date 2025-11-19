import sys

import pyqtgraph as pg
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QListWidgetItem, QDialog

import numpy as np
from lda_nsp2.data_ingestion import Ingest_Data, Ingest_Data_1D
from lda_nsp2.models.fitting import gaussfit, parabfit
from lda_nsp2.models.velocitycalculation import bereken_v
from lda_nsp2.views.lda_designer_gui import Ui_MainWindow
from lda_nsp2.views.lda_vortex_histogram_edit_dialog import Ui_Dialog

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
        self.ui.ImportMultipleButton.clicked.connect(self.ingest_multiple_vortex_histograms)
        self.ui.DeleteSelectedHistogramButton.clicked.connect(self.delete_vortex_histogram)
        self.ui.EditSelectedHistogramButton.clicked.connect(self.edit_vortex_histogram)

        self.ui.listWidget.currentItemChanged.connect(self.redraw_vortex_histogram)



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
        results = parabfit(self.parabola_list_depth, self.parabola_list_velo, -1, -2, 10)
        parab_fit_A, parab_fit_B, parab_fit_C, parab_fit_Y, parab_fit_X = results



        self.ui.graphicsView_2.plot(
            parab_fit_X, parab_fit_Y
        )

        print(parab_fit_A, parab_fit_B, parab_fit_C)

    @Slot()
    def ingest_vortex_histogram(self):
        # Open file-choosing modal
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, ("Import data"), "")
        print(fileName)

        # Ingest data and make it a histogram
        vals = Ingest_Data_1D(fileName)
        hist_data = vals.returndata()
        y,x = np.histogram(hist_data, bins=32)

        # Graph newly imported Histogram
        self.ui.graphicsView_3.clear()
        bgi = pg.BarGraphItem(x0=x[:-1], x1=x[1:], height=y, pen='w', brush=(16,3,0,255))
        self.ui.graphicsView_3.addItem(bgi)

        # Name of file without preceding path
        fileNameWOPath = fileName.split("/")[-1]

        # Add Name of file to list widget
        QListWidgetItem((fileNameWOPath), self.ui.listWidget)

        # save histogram to memory
        hashTableAddress = int(list(fileNameWOPath)[-2] + list(fileNameWOPath)[-1])
        self.vortex_master_data[hashTableAddress] = [x, y]

    @Slot()
    def ingest_multiple_vortex_histograms(self):
        # Open file-choosing modal
        fileNames = QtWidgets.QFileDialog.getOpenFileNames(self, ("Import data"), "")
        
        for fileName in fileNames[0]:

            # Ingest data and make it a histogram
            vals = Ingest_Data_1D(fileName)
            hist_data = vals.returndata()
            y,x = np.histogram(hist_data, bins=32)

            # Graph newly imported Histogram
            self.ui.graphicsView_3.clear()
            bgi = pg.BarGraphItem(x0=x[:-1], x1=x[1:], height=y, pen='w', brush=(16,3,0,255))
            self.ui.graphicsView_3.addItem(bgi)

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

            x = 50 + 22 + 8.5 * fileCoords[1]
            y = 18.5
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

            fileCoords.append(x)
            fileCoords.append(y)
            fileCoords.append(z)

            # save histogram to memory
            hashTableAddress = int(list(fileNameWOPath)[-2] + list(fileNameWOPath)[-1])
            self.vortex_master_data[hashTableAddress] = [[x, y], fileCoords]
            self.currently_selected_vortex_histogram = hashTableAddress



    @Slot()
    def redraw_vortex_histogram(self):
        datasetName = self.ui.listWidget.currentItem().text()

        datasetIndex = int(list(datasetName)[-2] + list(datasetName)[-1])
        self.currently_selected_vortex_histogram = datasetIndex

        HistogramList = self.vortex_master_data[datasetIndex]
        x = HistogramList[0][0]
        y = HistogramList[0][1]

        # Graph selected Histogram
        self.ui.graphicsView_3.clear()
        bgi = pg.BarGraphItem(x0=x[:-1], x1=x[1:], height=y, pen='w', brush=(16,3,0,255))
        self.ui.graphicsView_3.addItem(bgi)

    @Slot()
    def delete_vortex_histogram(self):
        self.vortex_master_data[self.currently_selected_vortex_histogram] = None

        currentRow = self.ui.listWidget.currentRow()
        self.ui.listWidget.takeItem(currentRow)

    def edit_vortex_histogram(self):
        dlg = HistogramEditDialog(self)
        dlg.exec()




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
