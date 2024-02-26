# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(646, 735)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Settings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(parent=Settings)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.ptGenPath = QtWidgets.QLineEdit(parent=Settings)
        self.ptGenPath.setText("")
        self.ptGenPath.setClearButtonEnabled(True)
        self.ptGenPath.setObjectName("ptGenPath")
        self.horizontalLayout_6.addWidget(self.ptGenPath)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=Settings)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.pictureBedPath = QtWidgets.QLineEdit(parent=Settings)
        self.pictureBedPath.setText("")
        self.pictureBedPath.setClearButtonEnabled(True)
        self.pictureBedPath.setObjectName("pictureBedPath")
        self.horizontalLayout_4.addWidget(self.pictureBedPath)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(parent=Settings)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.pictureBedToken = QtWidgets.QLineEdit(parent=Settings)
        self.pictureBedToken.setText("")
        self.pictureBedToken.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.pictureBedToken.setClearButtonEnabled(True)
        self.pictureBedToken.setObjectName("pictureBedToken")
        self.horizontalLayout_5.addWidget(self.pictureBedToken)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=Settings)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.screenshotPath = QtWidgets.QLineEdit(parent=Settings)
        self.screenshotPath.setText("")
        self.screenshotPath.setClearButtonEnabled(True)
        self.screenshotPath.setObjectName("screenshotPath")
        self.horizontalLayout_2.addWidget(self.screenshotPath)
        self.selectScreenshotPathButton = QtWidgets.QPushButton(parent=Settings)
        self.selectScreenshotPathButton.setStyleSheet("QPushButton {\n"
"    display: inline-block;\n"
"    padding: 3px 6px;\n"
"    font-size: 14px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"background-color: \n"
"                qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #16bf9d,\n"
"                                      stop:1 #10a266);\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: \n"
"                qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #11b998,\n"
"                                      stop:1 #08965e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: \n"
"                qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #0e9278,\n"
"                                      stop:1 #0e925c);\n"
"}\n"
"")
        self.selectScreenshotPathButton.setObjectName("selectScreenshotPathButton")
        self.horizontalLayout_2.addWidget(self.selectScreenshotPathButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_12 = QtWidgets.QLabel(parent=Settings)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.torrentPath = QtWidgets.QLineEdit(parent=Settings)
        self.torrentPath.setText("")
        self.torrentPath.setClearButtonEnabled(True)
        self.torrentPath.setObjectName("torrentPath")
        self.horizontalLayout_3.addWidget(self.torrentPath)
        self.selectTorrentPathButton = QtWidgets.QPushButton(parent=Settings)
        self.selectTorrentPathButton.setStyleSheet("QPushButton {\n"
"    display: inline-block;\n"
"    padding: 3px 6px;\n"
"    font-size: 14px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"background-color: \n"
"                qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #16bf9d,\n"
"                                      stop:1 #10a266);\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: \n"
"                qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #11b998,\n"
"                                      stop:1 #08965e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: \n"
"                qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #0e9278,\n"
"                                      stop:1 #0e925c);\n"
"}\n"
"")
        self.selectTorrentPathButton.setObjectName("selectTorrentPathButton")
        self.horizontalLayout_3.addWidget(self.selectTorrentPathButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(parent=Settings)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.screenshotNumber = QtWidgets.QSpinBox(parent=Settings)
        self.screenshotNumber.setMaximum(5)
        self.screenshotNumber.setProperty("value", 1)
        self.screenshotNumber.setObjectName("screenshotNumber")
        self.horizontalLayout_7.addWidget(self.screenshotNumber)
        self.label_2 = QtWidgets.QLabel(parent=Settings)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.screenshotThreshold = QtWidgets.QDoubleSpinBox(parent=Settings)
        self.screenshotThreshold.setDecimals(2)
        self.screenshotThreshold.setMaximum(5.0)
        self.screenshotThreshold.setSingleStep(0.01)
        self.screenshotThreshold.setProperty("value", 0.1)
        self.screenshotThreshold.setObjectName("screenshotThreshold")
        self.horizontalLayout_7.addWidget(self.screenshotThreshold)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(parent=Settings)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.screenshotStart = QtWidgets.QDoubleSpinBox(parent=Settings)
        self.screenshotStart.setDecimals(2)
        self.screenshotStart.setMaximum(1.0)
        self.screenshotStart.setSingleStep(0.01)
        self.screenshotStart.setProperty("value", 0.1)
        self.screenshotStart.setObjectName("screenshotStart")
        self.horizontalLayout_8.addWidget(self.screenshotStart)
        self.label_5 = QtWidgets.QLabel(parent=Settings)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.screenshotEnd = QtWidgets.QDoubleSpinBox(parent=Settings)
        self.screenshotEnd.setDecimals(2)
        self.screenshotEnd.setMaximum(1.0)
        self.screenshotEnd.setSingleStep(0.01)
        self.screenshotEnd.setProperty("value", 0.9)
        self.screenshotEnd.setObjectName("screenshotEnd")
        self.horizontalLayout_8.addWidget(self.screenshotEnd)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.autoUploadScreenshot = QtWidgets.QCheckBox(parent=Settings)
        self.autoUploadScreenshot.setChecked(True)
        self.autoUploadScreenshot.setObjectName("autoUploadScreenshot")
        self.horizontalLayout_9.addWidget(self.autoUploadScreenshot)
        self.pasteScreenshotUrl = QtWidgets.QCheckBox(parent=Settings)
        self.pasteScreenshotUrl.setChecked(True)
        self.pasteScreenshotUrl.setObjectName("pasteScreenshotUrl")
        self.horizontalLayout_9.addWidget(self.pasteScreenshotUrl)
        self.deleteScreenshot = QtWidgets.QCheckBox(parent=Settings)
        self.deleteScreenshot.setChecked(True)
        self.deleteScreenshot.setObjectName("deleteScreenshot")
        self.horizontalLayout_9.addWidget(self.deleteScreenshot)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.getThumbnails = QtWidgets.QCheckBox(parent=Settings)
        self.getThumbnails.setObjectName("getThumbnails")
        self.horizontalLayout_11.addWidget(self.getThumbnails)
        self.label_13 = QtWidgets.QLabel(parent=Settings)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.rows = QtWidgets.QSpinBox(parent=Settings)
        self.rows.setMinimum(1)
        self.rows.setMaximum(9)
        self.rows.setProperty("value", 4)
        self.rows.setObjectName("rows")
        self.horizontalLayout_11.addWidget(self.rows)
        self.label_14 = QtWidgets.QLabel(parent=Settings)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.cols = QtWidgets.QSpinBox(parent=Settings)
        self.cols.setMinimum(1)
        self.cols.setMaximum(9)
        self.cols.setProperty("value", 4)
        self.cols.setObjectName("cols")
        self.horizontalLayout_11.addWidget(self.cols)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(parent=Settings)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.renameFile = QtWidgets.QCheckBox(parent=Settings)
        self.renameFile.setChecked(False)
        self.renameFile.setObjectName("renameFile")
        self.horizontalLayout_10.addWidget(self.renameFile)
        self.makeDir = QtWidgets.QCheckBox(parent=Settings)
        self.makeDir.setChecked(False)
        self.makeDir.setObjectName("makeDir")
        self.horizontalLayout_10.addWidget(self.makeDir)
        self.secondConfirmFileName = QtWidgets.QCheckBox(parent=Settings)
        self.secondConfirmFileName.setChecked(False)
        self.secondConfirmFileName.setObjectName("secondConfirmFileName")
        self.horizontalLayout_10.addWidget(self.secondConfirmFileName)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.label_9 = QtWidgets.QLabel(parent=Settings)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_11 = QtWidgets.QLabel(parent=Settings)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 220))
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveButton = QtWidgets.QPushButton(parent=Settings)
        self.saveButton.setStyleSheet("QPushButton {\n"
"    display: inline-block;\n"
"    padding: 6px 6px;\n"
"    font-size: 14px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"background-color: \n"
"                qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #16bf9d,\n"
"                                      stop:1 #10a266);\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: \n"
"                qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #11b998,\n"
"                                      stop:1 #08965e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: \n"
"                qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #0e9278,\n"
"                                      stop:1 #0e925c);\n"
"}\n"
"")
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.cancelButton = QtWidgets.QPushButton(parent=Settings)
        self.cancelButton.setStyleSheet("QPushButton {\n"
"    display: inline-block;\n"
"    padding: 6px 6px;\n"
"    font-size: 14px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"background-color: \n"
"                qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #16bf9d,\n"
"                                      stop:1 #10a266);\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: \n"
"                qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #11b998,\n"
"                                      stop:1 #08965e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: \n"
"                qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #0e9278,\n"
"                                      stop:1 #0e925c);\n"
"}\n"
"")
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "设置"))
        self.label_8.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_8.setText(_translate("Settings", "PT Gen地址："))
        self.ptGenPath.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_6.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_6.setText(_translate("Settings", "图床api地址："))
        self.pictureBedPath.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_7.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_7.setText(_translate("Settings", "图床api密钥："))
        self.pictureBedToken.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_3.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_3.setText(_translate("Settings", "截图储存地址："))
        self.screenshotPath.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.selectScreenshotPathButton.setText(_translate("Settings", "浏览"))
        self.label_12.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_12.setText(_translate("Settings", "种子储存地址："))
        self.torrentPath.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.selectTorrentPathButton.setText(_translate("Settings", "浏览"))
        self.label.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label.setText(_translate("Settings", "截图数量："))
        self.screenshotNumber.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_2.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_2.setText(_translate("Settings", "关键帧复杂度："))
        self.screenshotThreshold.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_4.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_4.setText(_translate("Settings", "截图起始点（百分比）："))
        self.screenshotStart.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_5.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_5.setText(_translate("Settings", "截图终止点（百分比）："))
        self.screenshotEnd.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.autoUploadScreenshot.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.autoUploadScreenshot.setText(_translate("Settings", "自动上传图床"))
        self.pasteScreenshotUrl.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.pasteScreenshotUrl.setText(_translate("Settings", "将链接粘贴到简介后"))
        self.deleteScreenshot.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.deleteScreenshot.setText(_translate("Settings", "上传后删除本地图片"))
        self.getThumbnails.setText(_translate("Settings", "生成缩略图"))
        self.label_13.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_13.setText(_translate("Settings", "横向数量："))
        self.rows.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_14.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_14.setText(_translate("Settings", "纵向数量："))
        self.cols.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_10.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_10.setText(_translate("Settings", "获取标准命名时："))
        self.renameFile.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.renameFile.setText(_translate("Settings", "自动将文件（文件夹）重命名"))
        self.makeDir.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.makeDir.setText(_translate("Settings", "将电影文件放入同名文件夹"))
        self.secondConfirmFileName.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.secondConfirmFileName.setText(_translate("Settings", "二次确认文件名"))
        self.label_9.setText(_translate("Settings", "说明"))
        self.label_11.setStyleSheet(_translate("Settings", "QPushButton {\n"
"    display: inline-block;\n"
"    padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    outline: none;\n"
"    color:#fff;\n"
"    background-color: #559e24;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4a8821;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c6f1b;\n"
"}\n"
""))
        self.label_11.setText(_translate("Settings", "截图数量最多5个，图片越多、视频越高清速度越慢，请耐心等待。\n"
"关键帧复杂度指对画面的要求，数字越大画面越复杂，符合条件的画面也会越少，过大会导致截图数量不足。\n"
"截图起始点指截图开始的时刻在整个电影长度的占比，不易过小，以免截取片头。\n"
"截图终止点一定要比起始点大，否则无法截图，间隔如果太小也会导致截图数量不足。\n"
"对文件夹处理时仅获取其中第一个视频的参数信息，并仅对文件夹重命名。\n"
"制作种子时，如果选中的资源是文件夹，则直接制作；如果是文件，则对上级文件夹制作。\n"
"一键启动请取消勾选”二次确认文件名“，耐心等待勿反复点击，Pt-Gen连接性不好时不建议使用。\n"
"文件越大制作种子越慢，可查看任务管理器获取程序运行情况，资源路径可以直接复制文件粘贴到文本框中。\n"
"目前支持的图床：\n"
"https://img.agsvpt.com/\n"
"https://freeimage.host/\n"
"https://imgbb.com/\n"
"图床的api地址和密钥请到图床主页获取。"))
        self.saveButton.setText(_translate("Settings", "保存"))
        self.cancelButton.setText(_translate("Settings", "取消"))
