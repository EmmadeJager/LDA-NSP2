import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot

from lda_nsp2.data_ingestion import Ingest_Data
from lda_nsp2.models.fitting import gaussfit
from lda_nsp2.views.lda_designer_gui import Ui_MainWindow


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.import_button.clicked.connect(self.ingest_data_to_gui)
        self.ui.fit_button.clicked.connect(self.do_fit)

        self.ui.param1_fit_output_label.setEnabled(False)
        self.ui.param2_fit_output_label.setEnabled(False)
        self.ui.param3_fit_output_label.setEnabled(False)

    @Slot()
    def ingest_data_to_gui(self):
        experiment = Ingest_Data("first measurement!!!!!")
        self.data = experiment.returndata()

        self.ui.graphicsView.plot(self.data[0], self.data[1], pen=None, symbol="o")

        self.ui.param1_guess_spinbox.setValue(max(self.data[1]))
        self.ui.param2_guess_spinbox.setValue(1 / (2 * 100**2))
        self.ui.param3_guess_spinbox.setValue(
            self.data[0][self.data[1].index(max(self.data[1]))]
        )

    @Slot()
    def do_fit(self):
        A_guess = self.ui.param1_guess_spinbox.value()
        B_guess = self.ui.param2_guess_spinbox.value()
        C_guess = self.ui.param3_guess_spinbox.value()

        fit_data = gaussfit(
            self.data[0],
            self.data[1],
            A_guess,
            B_guess,
            C_guess
        )

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


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
