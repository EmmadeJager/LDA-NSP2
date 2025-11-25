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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QHeaderView, QLCDNumber,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

from pyqtgraph import (GraphicsLayoutWidget, PlotWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2108, 1219)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalTabWidget = QTabWidget(self.centralwidget)
        self.horizontalTabWidget.setObjectName(u"horizontalTabWidget")
        self.gauss_fit_pane = QWidget()
        self.gauss_fit_pane.setObjectName(u"gauss_fit_pane")
        self.horizontalLayout = QHBoxLayout(self.gauss_fit_pane)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphicsView = PlotWidget(self.gauss_fit_pane)
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
        self.param3_guess_spinbox.setMaximum(99999999.000000000000000)

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
        self.velocity_pane = QWidget()
        self.velocity_pane.setObjectName(u"velocity_pane")
        self.horizontalLayoutWidget = QWidget(self.velocity_pane)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, -1, 2051, 1101))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.x_measurement_spinbox = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.x_measurement_spinbox.setObjectName(u"x_measurement_spinbox")
        self.x_measurement_spinbox.setMaximum(200.000000000000000)
        self.x_measurement_spinbox.setValue(97.000000000000000)

        self.horizontalLayout_9.addWidget(self.x_measurement_spinbox)

        self.label_9 = QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.x_uncertainty_spinbox = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.x_uncertainty_spinbox.setObjectName(u"x_uncertainty_spinbox")
        self.x_uncertainty_spinbox.setValue(1.000000000000000)

        self.horizontalLayout_9.addWidget(self.x_uncertainty_spinbox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.y_measurement_spinbox = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.y_measurement_spinbox.setObjectName(u"y_measurement_spinbox")
        self.y_measurement_spinbox.setMaximum(200.000000000000000)
        self.y_measurement_spinbox.setValue(17.000000000000000)

        self.horizontalLayout_10.addWidget(self.y_measurement_spinbox)

        self.label_10 = QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.y_uncertainty_spinbox = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.y_uncertainty_spinbox.setObjectName(u"y_uncertainty_spinbox")
        self.y_uncertainty_spinbox.setValue(1.000000000000000)

        self.horizontalLayout_10.addWidget(self.y_uncertainty_spinbox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.z_measurement_spinbox = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.z_measurement_spinbox.setObjectName(u"z_measurement_spinbox")
        self.z_measurement_spinbox.setMaximum(200.000000000000000)
        self.z_measurement_spinbox.setValue(2.500000000000000)

        self.horizontalLayout_11.addWidget(self.z_measurement_spinbox)

        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.z_uncertainty_spinbox = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.z_uncertainty_spinbox.setObjectName(u"z_uncertainty_spinbox")
        self.z_uncertainty_spinbox.setValue(1.000000000000000)

        self.horizontalLayout_11.addWidget(self.z_uncertainty_spinbox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.refraction_correction_checkbox = QCheckBox(self.horizontalLayoutWidget)
        self.refraction_correction_checkbox.setObjectName(u"refraction_correction_checkbox")

        self.verticalLayout_3.addWidget(self.refraction_correction_checkbox)

        self.label_12 = QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(False)

        self.verticalLayout_3.addWidget(self.label_12)

        self.refraction_coefficient_spinbox = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.refraction_coefficient_spinbox.setObjectName(u"refraction_coefficient_spinbox")
        self.refraction_coefficient_spinbox.setEnabled(False)
        self.refraction_coefficient_spinbox.setMaximum(200.000000000000000)

        self.verticalLayout_3.addWidget(self.refraction_coefficient_spinbox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.velocity_lcd = QLCDNumber(self.horizontalLayoutWidget)
        self.velocity_lcd.setObjectName(u"velocity_lcd")
        self.velocity_lcd.setFrameShape(QFrame.Shape.StyledPanel)
        self.velocity_lcd.setFrameShadow(QFrame.Shadow.Plain)
        self.velocity_lcd.setSmallDecimalPoint(False)
        self.velocity_lcd.setDigitCount(15)
        self.velocity_lcd.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.velocity_lcd.setProperty(u"value", 0.000000000000000)

        self.verticalLayout_3.addWidget(self.velocity_lcd)

        self.label_14 = QLabel(self.horizontalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_14)

        self.velocity_lcd_uncertainty = QLCDNumber(self.horizontalLayoutWidget)
        self.velocity_lcd_uncertainty.setObjectName(u"velocity_lcd_uncertainty")
        self.velocity_lcd_uncertainty.setFrameShape(QFrame.Shape.StyledPanel)
        self.velocity_lcd_uncertainty.setFrameShadow(QFrame.Shadow.Plain)
        self.velocity_lcd_uncertainty.setSmallDecimalPoint(False)
        self.velocity_lcd_uncertainty.setDigitCount(15)
        self.velocity_lcd_uncertainty.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.velocity_lcd_uncertainty.setProperty(u"value", 0.000000000000000)

        self.verticalLayout_3.addWidget(self.velocity_lcd_uncertainty)

        self.calculate_velocity_button = QPushButton(self.horizontalLayoutWidget)
        self.calculate_velocity_button.setObjectName(u"calculate_velocity_button")

        self.verticalLayout_3.addWidget(self.calculate_velocity_button)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_15 = QLabel(self.horizontalLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_4.addWidget(self.label_15)

        self.tableWidget = QTableWidget(self.horizontalLayoutWidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.parabola_fit_button = QPushButton(self.horizontalLayoutWidget)
        self.parabola_fit_button.setObjectName(u"parabola_fit_button")

        self.verticalLayout_4.addWidget(self.parabola_fit_button)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.graphicsView_2 = PlotWidget(self.horizontalLayoutWidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.horizontalLayout_8.addWidget(self.graphicsView_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.label_13 = QLabel(self.horizontalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_13)

        self.measurement_depth_spinbox = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.measurement_depth_spinbox.setObjectName(u"measurement_depth_spinbox")

        self.horizontalLayout_12.addWidget(self.measurement_depth_spinbox)

        self.add_to_table_button = QPushButton(self.horizontalLayoutWidget)
        self.add_to_table_button.setObjectName(u"add_to_table_button")

        self.horizontalLayout_12.addWidget(self.add_to_table_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.horizontalTabWidget.addTab(self.velocity_pane, "")
        self.Vortex = QWidget()
        self.Vortex.setObjectName(u"Vortex")
        self.horizontalLayout_19 = QHBoxLayout(self.Vortex)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.tabWidget = QTabWidget(self.Vortex)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.DataIngestionTab = QWidget()
        self.DataIngestionTab.setObjectName(u"DataIngestionTab")
        self.verticalLayout_17 = QVBoxLayout(self.DataIngestionTab)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label_16 = QLabel(self.DataIngestionTab)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout_6.addWidget(self.label_16)

        self.listWidget = QListWidget(self.DataIngestionTab)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout_6.addWidget(self.listWidget)

        self.EditSelectedHistogramButton = QPushButton(self.DataIngestionTab)
        self.EditSelectedHistogramButton.setObjectName(u"EditSelectedHistogramButton")

        self.verticalLayout_6.addWidget(self.EditSelectedHistogramButton)

        self.DeleteSelectedHistogramButton = QPushButton(self.DataIngestionTab)
        self.DeleteSelectedHistogramButton.setObjectName(u"DeleteSelectedHistogramButton")

        self.verticalLayout_6.addWidget(self.DeleteSelectedHistogramButton)


        self.horizontalLayout_13.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.graphicsView_3 = PlotWidget(self.DataIngestionTab)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy1)
        self.graphicsView_3.setMinimumSize(QSize(900, 0))
        self.graphicsView_3.setMaximumSize(QSize(100000, 10000))

        self.horizontalLayout_15.addWidget(self.graphicsView_3)

        self.verticalFrame_2 = QFrame(self.DataIngestionTab)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_8 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalFrame_8 = QFrame(self.verticalFrame_2)
        self.verticalFrame_8.setObjectName(u"verticalFrame_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.verticalFrame_8.sizePolicy().hasHeightForWidth())
        self.verticalFrame_8.setSizePolicy(sizePolicy2)
        self.verticalFrame_8.setMinimumSize(QSize(0, 0))
        self.verticalFrame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_14 = QVBoxLayout(self.verticalFrame_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.LowPassFilterCheckBox = QCheckBox(self.verticalFrame_8)
        self.LowPassFilterCheckBox.setObjectName(u"LowPassFilterCheckBox")

        self.verticalLayout_14.addWidget(self.LowPassFilterCheckBox)

        self.label_20 = QLabel(self.verticalFrame_8)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_14.addWidget(self.label_20)

        self.LowPassFilterSpinbox = QSpinBox(self.verticalFrame_8)
        self.LowPassFilterSpinbox.setObjectName(u"LowPassFilterSpinbox")
        self.LowPassFilterSpinbox.setMaximum(10000)

        self.verticalLayout_14.addWidget(self.LowPassFilterSpinbox)

        self.label_24 = QLabel(self.verticalFrame_8)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_14.addWidget(self.label_24)

        self.LowPassFilterK_value_Spinbox = QDoubleSpinBox(self.verticalFrame_8)
        self.LowPassFilterK_value_Spinbox.setObjectName(u"LowPassFilterK_value_Spinbox")
        self.LowPassFilterK_value_Spinbox.setDecimals(4)
        self.LowPassFilterK_value_Spinbox.setValue(1.000000000000000)

        self.verticalLayout_14.addWidget(self.LowPassFilterK_value_Spinbox)


        self.verticalLayout_8.addWidget(self.verticalFrame_8)

        self.verticalFrame_7 = QFrame(self.verticalFrame_2)
        self.verticalFrame_7.setObjectName(u"verticalFrame_7")
        sizePolicy2.setHeightForWidth(self.verticalFrame_7.sizePolicy().hasHeightForWidth())
        self.verticalFrame_7.setSizePolicy(sizePolicy2)
        self.verticalFrame_7.setMinimumSize(QSize(0, 0))
        self.verticalFrame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_13 = QVBoxLayout(self.verticalFrame_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.HighPassFilterCheckBox = QCheckBox(self.verticalFrame_7)
        self.HighPassFilterCheckBox.setObjectName(u"HighPassFilterCheckBox")

        self.verticalLayout_13.addWidget(self.HighPassFilterCheckBox)

        self.label_18 = QLabel(self.verticalFrame_7)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_13.addWidget(self.label_18)

        self.HighPassFilterSpinbox = QSpinBox(self.verticalFrame_7)
        self.HighPassFilterSpinbox.setObjectName(u"HighPassFilterSpinbox")
        self.HighPassFilterSpinbox.setMaximum(10000)

        self.verticalLayout_13.addWidget(self.HighPassFilterSpinbox)

        self.label_23 = QLabel(self.verticalFrame_7)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_13.addWidget(self.label_23)

        self.HighPassFilterK_value_Spinbox = QDoubleSpinBox(self.verticalFrame_7)
        self.HighPassFilterK_value_Spinbox.setObjectName(u"HighPassFilterK_value_Spinbox")
        self.HighPassFilterK_value_Spinbox.setDecimals(4)
        self.HighPassFilterK_value_Spinbox.setValue(1.000000000000000)

        self.verticalLayout_13.addWidget(self.HighPassFilterK_value_Spinbox)


        self.verticalLayout_8.addWidget(self.verticalFrame_7)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)


        self.horizontalLayout_15.addWidget(self.verticalFrame_2)

        self.horizontalLayout_15.setStretch(0, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalFrame_5 = QFrame(self.DataIngestionTab)
        self.verticalFrame_5.setObjectName(u"verticalFrame_5")
        self.verticalFrame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_10 = QVBoxLayout(self.verticalFrame_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.SaveHistogramButton = QPushButton(self.verticalFrame_5)
        self.SaveHistogramButton.setObjectName(u"SaveHistogramButton")

        self.verticalLayout_10.addWidget(self.SaveHistogramButton)

        self.label_25 = QLabel(self.verticalFrame_5)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_10.addWidget(self.label_25)


        self.horizontalLayout_14.addWidget(self.verticalFrame_5)

        self.verticalFrame_6 = QFrame(self.DataIngestionTab)
        self.verticalFrame_6.setObjectName(u"verticalFrame_6")
        self.verticalFrame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_12 = QVBoxLayout(self.verticalFrame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_19 = QLabel(self.verticalFrame_6)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_12.addWidget(self.label_19)

        self.HistoStartRangeSpinbox = QSpinBox(self.verticalFrame_6)
        self.HistoStartRangeSpinbox.setObjectName(u"HistoStartRangeSpinbox")
        self.HistoStartRangeSpinbox.setMaximum(10000)

        self.verticalLayout_12.addWidget(self.HistoStartRangeSpinbox)


        self.horizontalLayout_14.addWidget(self.verticalFrame_6)

        self.verticalFrame_4 = QFrame(self.DataIngestionTab)
        self.verticalFrame_4.setObjectName(u"verticalFrame_4")
        self.verticalFrame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_9 = QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_17 = QLabel(self.verticalFrame_4)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_9.addWidget(self.label_17)

        self.HistoEndRangeSpinbox = QSpinBox(self.verticalFrame_4)
        self.HistoEndRangeSpinbox.setObjectName(u"HistoEndRangeSpinbox")
        self.HistoEndRangeSpinbox.setMaximum(10000)

        self.verticalLayout_9.addWidget(self.HistoEndRangeSpinbox)


        self.horizontalLayout_14.addWidget(self.verticalFrame_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_13.addLayout(self.verticalLayout_7)

        self.horizontalLayout_13.setStretch(1, 1)

        self.verticalLayout_17.addLayout(self.horizontalLayout_13)

        self.horizontalFrame_2 = QFrame(self.DataIngestionTab)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.BottomButtonBar = QHBoxLayout(self.horizontalFrame_2)
        self.BottomButtonBar.setObjectName(u"BottomButtonBar")
        self.ImportSingleButton = QPushButton(self.horizontalFrame_2)
        self.ImportSingleButton.setObjectName(u"ImportSingleButton")

        self.BottomButtonBar.addWidget(self.ImportSingleButton)

        self.ImportMultipleButton = QPushButton(self.horizontalFrame_2)
        self.ImportMultipleButton.setObjectName(u"ImportMultipleButton")

        self.BottomButtonBar.addWidget(self.ImportMultipleButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.BottomButtonBar.addItem(self.horizontalSpacer_2)

        self.label_21 = QLabel(self.horizontalFrame_2)
        self.label_21.setObjectName(u"label_21")

        self.BottomButtonBar.addWidget(self.label_21)

        self.spinBox = QSpinBox(self.horizontalFrame_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(10000)

        self.BottomButtonBar.addWidget(self.spinBox)

        self.label_22 = QLabel(self.horizontalFrame_2)
        self.label_22.setObjectName(u"label_22")

        self.BottomButtonBar.addWidget(self.label_22)

        self.spinBox_3 = QSpinBox(self.horizontalFrame_2)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(10000)

        self.BottomButtonBar.addWidget(self.spinBox_3)


        self.verticalLayout_17.addWidget(self.horizontalFrame_2)

        self.tabWidget.addTab(self.DataIngestionTab, "")
        self.DataViewTab = QWidget()
        self.DataViewTab.setObjectName(u"DataViewTab")
        self.verticalLayout_18 = QVBoxLayout(self.DataViewTab)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.Fit_All_Histograms_Button = QPushButton(self.DataViewTab)
        self.Fit_All_Histograms_Button.setObjectName(u"Fit_All_Histograms_Button")
        self.Fit_All_Histograms_Button.setMinimumSize(QSize(150, 75))

        self.verticalLayout_15.addWidget(self.Fit_All_Histograms_Button)

        self.label_26 = QLabel(self.DataViewTab)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_15.addWidget(self.label_26)

        self.comboBox = QComboBox(self.DataViewTab)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_15.addWidget(self.comboBox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_3)


        self.horizontalLayout_16.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.heatMapView = GraphicsLayoutWidget(self.DataViewTab)
        self.heatMapView.setObjectName(u"heatMapView")

        self.verticalLayout_16.addWidget(self.heatMapView)


        self.horizontalLayout_16.addLayout(self.verticalLayout_16)


        self.verticalLayout_11.addLayout(self.horizontalLayout_16)


        self.verticalLayout_18.addLayout(self.verticalLayout_11)

        self.tabWidget.addTab(self.DataViewTab, "")
        self.ModelFitTab = QWidget()
        self.ModelFitTab.setObjectName(u"ModelFitTab")
        self.horizontalLayout_18 = QHBoxLayout(self.ModelFitTab)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalFrame_71 = QFrame(self.ModelFitTab)
        self.verticalFrame_71.setObjectName(u"verticalFrame_71")
        self.verticalFrame_71.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_22 = QVBoxLayout(self.verticalFrame_71)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_27 = QLabel(self.verticalFrame_71)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_22.addWidget(self.label_27)

        self.fitVatistas_button = QPushButton(self.verticalFrame_71)
        self.fitVatistas_button.setObjectName(u"fitVatistas_button")

        self.verticalLayout_22.addWidget(self.fitVatistas_button)

        self.fitLambOseen_button = QPushButton(self.verticalFrame_71)
        self.fitLambOseen_button.setObjectName(u"fitLambOseen_button")

        self.verticalLayout_22.addWidget(self.fitLambOseen_button)

        self.fitRankine_button = QPushButton(self.verticalFrame_71)
        self.fitRankine_button.setObjectName(u"fitRankine_button")

        self.verticalLayout_22.addWidget(self.fitRankine_button)

        self.fitModifiedRankine_button = QPushButton(self.verticalFrame_71)
        self.fitModifiedRankine_button.setObjectName(u"fitModifiedRankine_button")

        self.verticalLayout_22.addWidget(self.fitModifiedRankine_button)

        self.fitKaufmann_button = QPushButton(self.verticalFrame_71)
        self.fitKaufmann_button.setObjectName(u"fitKaufmann_button")

        self.verticalLayout_22.addWidget(self.fitKaufmann_button)

        self.fitBurgers_button = QPushButton(self.verticalFrame_71)
        self.fitBurgers_button.setObjectName(u"fitBurgers_button")

        self.verticalLayout_22.addWidget(self.fitBurgers_button)

        self.fitSullivan_button = QPushButton(self.verticalFrame_71)
        self.fitSullivan_button.setObjectName(u"fitSullivan_button")

        self.verticalLayout_22.addWidget(self.fitSullivan_button)

        self.fitBatchelor_button = QPushButton(self.verticalFrame_71)
        self.fitBatchelor_button.setObjectName(u"fitBatchelor_button")

        self.verticalLayout_22.addWidget(self.fitBatchelor_button)

        self.fitTwoCell_button = QPushButton(self.verticalFrame_71)
        self.fitTwoCell_button.setObjectName(u"fitTwoCell_button")

        self.verticalLayout_22.addWidget(self.fitTwoCell_button)

        self.line_2 = QFrame(self.verticalFrame_71)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_22.addWidget(self.line_2)

        self.showfittedplot_checkBox = QCheckBox(self.verticalFrame_71)
        self.showfittedplot_checkBox.setObjectName(u"showfittedplot_checkBox")

        self.verticalLayout_22.addWidget(self.showfittedplot_checkBox)

        self.fitAllModels_button = QPushButton(self.verticalFrame_71)
        self.fitAllModels_button.setObjectName(u"fitAllModels_button")

        self.verticalLayout_22.addWidget(self.fitAllModels_button)


        self.verticalLayout_20.addWidget(self.verticalFrame_71)

        self.VortexFitLog = QTextEdit(self.ModelFitTab)
        self.VortexFitLog.setObjectName(u"VortexFitLog")

        self.verticalLayout_20.addWidget(self.VortexFitLog)

        self.label_28 = QLabel(self.ModelFitTab)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_20.addWidget(self.label_28)

        self.lcdNumber = QLCDNumber(self.ModelFitTab)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.verticalLayout_20.addWidget(self.lcdNumber)


        self.horizontalLayout_17.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.VortexModelFit_GraphicsView = GraphicsLayoutWidget(self.ModelFitTab)
        self.VortexModelFit_GraphicsView.setObjectName(u"VortexModelFit_GraphicsView")
        self.VortexModelFit_GraphicsView.setMinimumSize(QSize(1800, 0))

        self.verticalLayout_21.addWidget(self.VortexModelFit_GraphicsView)


        self.horizontalLayout_17.addLayout(self.verticalLayout_21)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)

        self.tabWidget.addTab(self.ModelFitTab, "")

        self.horizontalLayout_19.addWidget(self.tabWidget)

        self.horizontalTabWidget.addTab(self.Vortex, "")

        self.verticalLayout_5.addWidget(self.horizontalTabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2108, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.horizontalTabWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


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
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"X Measurement:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Y Measurement:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Z Measurement:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.refraction_correction_checkbox.setText(QCoreApplication.translate("MainWindow", u"Tube/Water Refraction Correction", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Refraction Coefficient:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.calculate_velocity_button.setText(QCoreApplication.translate("MainWindow", u"Calculate Water Velocity", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Parabola Table", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Depth", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Speed", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.parabola_fit_button.setText(QCoreApplication.translate("MainWindow", u"Do Fit", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Measurement Depth:", None))
        self.add_to_table_button.setText(QCoreApplication.translate("MainWindow", u"Add to parabola table", None))
        self.horizontalTabWidget.setTabText(self.horizontalTabWidget.indexOf(self.velocity_pane), QCoreApplication.translate("MainWindow", u"Velocity Calulation", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Measurements:", None))
        self.EditSelectedHistogramButton.setText(QCoreApplication.translate("MainWindow", u"Edit Selected", None))
        self.DeleteSelectedHistogramButton.setText(QCoreApplication.translate("MainWindow", u"Delete Selected", None))
        self.LowPassFilterCheckBox.setText(QCoreApplication.translate("MainWindow", u"Lowpass Filter", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Frequency:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"K-Value:", None))
        self.HighPassFilterCheckBox.setText(QCoreApplication.translate("MainWindow", u"Highpass Filter", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Frequency:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"K-Value:", None))
        self.SaveHistogramButton.setText(QCoreApplication.translate("MainWindow", u"Save Histogram", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"This action is irreversible", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Start Range [Hz]:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"End Range [Hz]:", None))
        self.ImportSingleButton.setText(QCoreApplication.translate("MainWindow", u"Import Single Point", None))
        self.ImportMultipleButton.setText(QCoreApplication.translate("MainWindow", u"Import Multiple Points", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Horizontal View Range:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataIngestionTab), QCoreApplication.translate("MainWindow", u"Data Ingestion", None))
        self.Fit_All_Histograms_Button.setText(QCoreApplication.translate("MainWindow", u"Fit All Histograms", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Depth:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataViewTab), QCoreApplication.translate("MainWindow", u"Data View", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Fit Model:", None))
        self.fitVatistas_button.setText(QCoreApplication.translate("MainWindow", u"Vatistas", None))
        self.fitLambOseen_button.setText(QCoreApplication.translate("MainWindow", u"Lamb-Oseen", None))
        self.fitRankine_button.setText(QCoreApplication.translate("MainWindow", u"Rankine", None))
        self.fitModifiedRankine_button.setText(QCoreApplication.translate("MainWindow", u"Modified Rankine (Smooth transition)", None))
        self.fitKaufmann_button.setText(QCoreApplication.translate("MainWindow", u"Kaufmann/Scully", None))
        self.fitBurgers_button.setText(QCoreApplication.translate("MainWindow", u"Burgers", None))
        self.fitSullivan_button.setText(QCoreApplication.translate("MainWindow", u"Sullivan", None))
        self.fitBatchelor_button.setText(QCoreApplication.translate("MainWindow", u"Batchelor", None))
        self.fitTwoCell_button.setText(QCoreApplication.translate("MainWindow", u"Two-Cell", None))
        self.showfittedplot_checkBox.setText(QCoreApplication.translate("MainWindow", u"Show Fitted Plot", None))
        self.fitAllModels_button.setText(QCoreApplication.translate("MainWindow", u"Fit all", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Reduced Chi-Square:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ModelFitTab), QCoreApplication.translate("MainWindow", u"Model Fit", None))
        self.horizontalTabWidget.setTabText(self.horizontalTabWidget.indexOf(self.Vortex), QCoreApplication.translate("MainWindow", u"Vortex", None))
    # retranslateUi

