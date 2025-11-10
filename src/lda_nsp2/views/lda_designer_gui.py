# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lda_designer_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1009, 663)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalTabWidget = QTabWidget(self.centralwidget)
        self.horizontalTabWidget.setObjectName(u"horizontalTabWidget")
        self.horizontalTabWidget.setGeometry(QRect(9, 9, 991, 591))
        self.gauss_fit_pane = QWidget()
        self.gauss_fit_pane.setObjectName(u"gauss_fit_pane")
        self.horizontalLayout = QHBoxLayout(self.gauss_fit_pane)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphicsView = QGraphicsView(self.gauss_fit_pane)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.gauss_fit_pane)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_4 = QLabel(self.gauss_fit_pane)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.line = QFrame(self.gauss_fit_pane)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(4)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label = QLabel(self.gauss_fit_pane)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.param1_guess_spinbox = QDoubleSpinBox(self.gauss_fit_pane)
        self.param1_guess_spinbox.setObjectName(u"param1_guess_spinbox")
        self.param1_guess_spinbox.setWrapping(False)
        self.param1_guess_spinbox.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.param1_guess_spinbox)

        self.param1_fit_output_label = QLabel(self.gauss_fit_pane)
        self.param1_fit_output_label.setObjectName(u"param1_fit_output_label")
        self.param1_fit_output_label.setFrameShape(QFrame.Shape.StyledPanel)

        self.horizontalLayout_3.addWidget(self.param1_fit_output_label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_2 = QLabel(self.gauss_fit_pane)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.param2_guess_spinbox = QDoubleSpinBox(self.gauss_fit_pane)
        self.param2_guess_spinbox.setObjectName(u"param2_guess_spinbox")
        self.param2_guess_spinbox.setWrapping(False)
        self.param2_guess_spinbox.setReadOnly(False)

        self.horizontalLayout_4.addWidget(self.param2_guess_spinbox)

        self.param2_fit_output_label = QLabel(self.gauss_fit_pane)
        self.param2_fit_output_label.setObjectName(u"param2_fit_output_label")
        self.param2_fit_output_label.setFrameShape(QFrame.Shape.StyledPanel)

        self.horizontalLayout_4.addWidget(self.param2_fit_output_label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_3 = QLabel(self.gauss_fit_pane)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.param3_guess_spinbox = QDoubleSpinBox(self.gauss_fit_pane)
        self.param3_guess_spinbox.setObjectName(u"param3_guess_spinbox")
        self.param3_guess_spinbox.setWrapping(False)
        self.param3_guess_spinbox.setReadOnly(False)

        self.horizontalLayout_5.addWidget(self.param3_guess_spinbox)

        self.param3_fit_output_label = QLabel(self.gauss_fit_pane)
        self.param3_fit_output_label.setObjectName(u"param3_fit_output_label")
        self.param3_fit_output_label.setEnabled(True)
        self.param3_fit_output_label.setFrameShape(QFrame.Shape.StyledPanel)

        self.horizontalLayout_5.addWidget(self.param3_fit_output_label)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.fit_button = QPushButton(self.gauss_fit_pane)
        self.fit_button.setObjectName(u"fit_button")
        self.fit_button.setCheckable(False)

        self.verticalLayout.addWidget(self.fit_button)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.import_button = QPushButton(self.gauss_fit_pane)
        self.import_button.setObjectName(u"import_button")

        self.horizontalLayout_2.addWidget(self.import_button)

        self.pushButton_2 = QPushButton(self.gauss_fit_pane)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.gauss_fit_pane)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalTabWidget.addTab(self.gauss_fit_pane, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1009, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Initial Guess:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Final Fit:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fitting Parameter 1:", None))
        self.param1_fit_output_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Fitting Parameter 2:", None))
        self.param2_fit_output_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fitting Parameter 3:", None))
        self.param3_fit_output_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.fit_button.setText(QCoreApplication.translate("MainWindow", u"Do Fit", None))
        self.import_button.setText(QCoreApplication.translate("MainWindow", u"Import Data", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.horizontalTabWidget.setTabText(self.horizontalTabWidget.indexOf(self.gauss_fit_pane), QCoreApplication.translate("MainWindow", u"Gaussian Fit", None))
    # retranslateUi

