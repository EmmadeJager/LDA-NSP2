import sys

import pyqtgraph as pg
from PySide6 import QtWidgets
from PySide6.QtCore import Slot

from lda_nsp2.data_ingestion import Ingest_Data
from lda_nsp2.models.fitting import gaussfit, parabfit
from lda_nsp2.models.velocitycalculation import bereken_v
from lda_nsp2.views.lda_designer_gui import Ui_MainWindow

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


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
