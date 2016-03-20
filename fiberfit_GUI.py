#!/usr/local/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, heigth, width):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(0.3*int(width.__str__()), 0.1*int(heigth.__str__()))
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(10000, 10000))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.midGrid = QtWidgets.QGridLayout()
        self.midGrid.setObjectName("midGrid")
        self.selectImgBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectImgBox.sizePolicy().hasHeightForWidth())
        self.selectImgBox.setSizePolicy(sizePolicy)
        self.selectImgBox.setMinimumSize(QtCore.QSize(170, 0))
        self.selectImgBox.setMaximumSize(QtCore.QSize(170, 16777215))
        self.selectImgBox.setObjectName("selectImgBox")
        self.midGrid.addWidget(self.selectImgBox, 0, 0, 1, 1)

          #  Progress bar
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)

        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())

        self.progressBar.setSizePolicy(sizePolicy)

        self.progressBar.setMinimumSize(QtCore.QSize(50, 0))
        self.progressBar.setMaximumSize(QtCore.QSize(50, 20))

        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.progressBar.hide()

        spacerItem0 = QtWidgets.QSpacerItem(0.08*int(width.__str__()), 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.midGrid.addItem(spacerItem0, 0, 3, 1, 1)

        self.sigLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.sigLabel.setFont(font)
        self.sigLabel.setObjectName("sigLabel")

        self.sigLabel.setToolTip("Standard Deviation Of Fiber Distribution")
        self.midGrid.addWidget(self.sigLabel, 0, 10, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.midGrid.addItem(spacerItem, 0, 11, 1, 1)
        # R^2 label
        self.RLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setItalic(False)
        self.RLabel.setFont(font)
        self.RLabel.setTextFormat(QtCore.Qt.AutoText)
        self.RLabel.setObjectName("RLabel")


        #tip = QtWidgets.QToolTip()
        #tip.showText("Goodness of Fit")
        #tip.setFont("Times New Roman")
        #self.RLabel.setToolTip(tip)
        self.RLabel.setToolTip("Goodness of Fit")
        self.midGrid.addWidget(self.RLabel, 0, 4, 1, 1)

        wWidth = 0.04*int(width.__str__())

        spacerItem1 = QtWidgets.QSpacerItem(0.04*int(width.__str__()), 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.midGrid.addItem(spacerItem1, 0, 5, 1, 1)

        # mu label
        self.muLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.muLabel.setFont(font)
        self.muLabel.setObjectName("muLabel")
        self.muLabel.setToolTip("Mean Orientation")
        self.midGrid.addWidget(self.muLabel, 0, 6, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(wWidth, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.midGrid.addItem(spacerItem2, 0, 7, 1, 1)

        #k label
        self.kLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setItalic(False)
        self.kLabel.setFont(font)
        self.kLabel.setTextFormat(QtCore.Qt.AutoText)
        self.kLabel.setObjectName("kLabel")
        self.kLabel.setToolTip("Fiber Dispersion")
        self.midGrid.addWidget(self.kLabel, 0, 8, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(wWidth, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.midGrid.addItem(spacerItem3, 0, 9, 1, 1)



        # spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
  #       self.midGrid.addItem(spacerItem4, 0, 9, 1, 1)


        self.gridLayout.addLayout(self.midGrid, 1, 0, 1, 1)
        self.figureWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.figureWidget.sizePolicy().hasHeightForWidth())
        self.figureWidget.setSizePolicy(sizePolicy)
        self.figureWidget.setObjectName("figureWidget")
        self.figureLayout = QtWidgets.QGridLayout(self.figureWidget)
        self.figureLayout.setObjectName("figureLayout")

        self.gridLayout.addWidget(self.figureWidget, 2, 0, 1, 1)
        self.topGrid = QtWidgets.QGridLayout()
        self.topGrid.setObjectName("topGrid")
        spacerItem3 = QtWidgets.QSpacerItem(wWidth, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topGrid.addItem(spacerItem3, 0, 6, 1, 1)
        #self.topGrid.addWidget(self.progressBar, 0, 5, 1, 1)


        # self.verticalLayout = QtWidgets.QHBoxLayout()
        # self.verticalLayout.setObjectName("verticalLayout")
        # self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        # # self.progressBar = QtWidgets.QProgressBar(self.widget)
        # # self.progressBa.setProperty("value", 24)
        # # self.progressBar_2.setObjectName("progressBar_2")
        # self.verticalLayout.addWidget(self.progressBar)
        # spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        # self.verticalLayout.addItem(spacerItem3)
        # self.topGrid.addLayout(self.verticalLayout, 0, 5, 1, 1)

        # self.widget = QtWidgets.QWidget(self.centralwidget)
        # self.widget.setObjectName("widget")
        # self.topGrid = QtWidgets.QGridLayout(self.widget)
        # self.topGrid.setContentsMargins(0, 0, 0, 0)
        # self.topGrid.setObjectName("topGrid")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())



        self.barWidget = QtWidgets.QWidget()
        self.barWidget.setObjectName("barWidget")
        self.barWidget.setSizePolicy(sizePolicy)
        self.gridPLayout = QtWidgets.QGridLayout(self.barWidget)
        self.gridPLayout.setContentsMargins(0, 0, 0, 0)
        self.gridPLayout.setObjectName("gridLayout")
        # self.progressBar = QtWidgets.QProgressBar(self.barWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        # self.progressBar.setSizePolicy(sizePolicy)
        # self.progressBar.setProperty("value", 24)
        # self.progressBar.setObjectName("progressBar")
        self.gridPLayout.addWidget(self.progressBar, 0, 0, 1, 1)
        self.topGrid.addWidget(self.barWidget, 0, 5, 1, 1)


        self.clearButton = QtWidgets.QPushButton(self.centralwidget)











        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(70, 60))
        self.clearButton.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.clearButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.find_data_file('clearButton.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #icon.addPixmap(QtGui.QPixmap("images/clearButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon)
        self.clearButton.setIconSize(QtCore.QSize(40, 40))
        self.clearButton.setObjectName("clearButton")
        self.topGrid.addWidget(self.clearButton, 0, 4, 1, 1)
        self.clearButton.setToolTip("Clear Images")
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportButton.sizePolicy().hasHeightForWidth())
        self.exportButton.setSizePolicy(sizePolicy)
        self.exportButton.setMinimumSize(QtCore.QSize(70, 60))
        self.exportButton.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.exportButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.find_data_file('export.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #icon1.addPixmap(QtGui.QPixmap("images/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportButton.setIcon(icon1)
        self.exportButton.setIconSize(QtCore.QSize(50, 50))
        self.exportButton.setObjectName("exportButton")
        self.exportButton.setToolTip("Export")
        self.topGrid.addWidget(self.exportButton, 0, 2, 1, 1)
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadButton.sizePolicy().hasHeightForWidth())
        self.loadButton.setSizePolicy(sizePolicy)
        self.loadButton.setMinimumSize(QtCore.QSize(70, 60))
        self.loadButton.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.loadButton.setAcceptDrops(False)
        self.loadButton.setAutoFillBackground(False)
        self.loadButton.setText("")

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.find_data_file('open.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #icon2.addPixmap(QtGui.QPixmap("images/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadButton.setIcon(icon2)
        self.loadButton.setIconSize(QtCore.QSize(50, 50))
        self.loadButton.setObjectName("loadButton")
        self.loadButton.setToolTip("Open")
        self.topGrid.addWidget(self.loadButton, 0, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(70, 60))
        self.startButton.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.startButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(self.find_data_file('start-icon.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #icon3.addPixmap(QtGui.QPixmap("images/start-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon3)
        self.startButton.setIconSize(QtCore.QSize(40, 40))
        self.startButton.setObjectName("startButton")
        self.startButton.setToolTip("Run")
        self.topGrid.addWidget(self.startButton, 0, 1, 1, 1)

        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
        self.settingsButton.setSizePolicy(sizePolicy)
        self.settingsButton.setMinimumSize(QtCore.QSize(70, 60))
        self.settingsButton.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.settingsButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.settingsButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(self.find_data_file('settings.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #icon4.addPixmap(QtGui.QPixmap("images/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon4)
        self.settingsButton.setIconSize(QtCore.QSize(40, 40))
        self.settingsButton.setObjectName("settingsButton")
        self.settingsButton.setToolTip("Settings")
        self.topGrid.addWidget(self.settingsButton, 0, 3, 1, 1)

        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setMinimumSize(QtCore.QSize(95, 32))
        self.nextButton.setMaximumSize(QtCore.QSize(1000000, 1000000))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        self.topGrid.addWidget(self.nextButton, 0, 8, 1, 1)
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevButton.sizePolicy().hasHeightForWidth())
        self.prevButton.setSizePolicy(sizePolicy)
        self.prevButton.setMinimumSize(QtCore.QSize(95, 32))
        self.prevButton.setMaximumSize(QtCore.QSize(1000000, 1000000))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.prevButton.setFont(font)
        self.prevButton.setObjectName("prevButton")
        self.topGrid.addWidget(self.prevButton, 0, 7, 1, 1)
        self.gridLayout.addLayout(self.topGrid, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 22))
        self.menubar.setObjectName("menubar")
        self.menuFiberfit = QtWidgets.QMenu(self.menubar)
        self.menuFiberfit.setObjectName("menuFiberfit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFiberfit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FiberFit"))
        self.RLabel.setText(_translate("MainWindow", ('R'+u"\u00B2"+" = ")))
        self.kLabel.setText(_translate("MainWindow", "k = "))
        self.muLabel.setText(_translate("MainWindow", "μ ="))
        self.nextButton.setText(_translate("MainWindow", "→"))
        self.prevButton.setText(_translate("MainWindow", "←"))
        self.menuFiberfit.setTitle(_translate("MainWindow", "Fiberfit"))
        self.sigLabel.setText(_translate("MainWindow", "σ = "))

    def find_data_file(self, filename):
        if getattr(sys, 'frozen', False):
            datadir = os.path.dirname(sys.executable)
        else:
            datadir = os.path.dirname('images/' + filename)
        return os.path.join(datadir, filename)
    