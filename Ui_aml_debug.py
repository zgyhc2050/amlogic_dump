# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\code\Python\amlogic_debug_tool\aml_debug.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AmlDebug_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.AmlDebug_tabWidget.setEnabled(True)
        self.AmlDebug_tabWidget.setGeometry(QtCore.QRect(0, 0, 741, 191))
        self.AmlDebug_tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.AmlDebug_tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.AmlDebug_tabWidget.setDocumentMode(False)
        self.AmlDebug_tabWidget.setTabsClosable(False)
        self.AmlDebug_tabWidget.setMovable(False)
        self.AmlDebug_tabWidget.setTabBarAutoHide(False)
        self.AmlDebug_tabWidget.setObjectName("AmlDebug_tabWidget")
        self.AmlAudioDebug_tab = QtWidgets.QWidget()
        self.AmlAudioDebug_tab.setObjectName("AmlAudioDebug_tab")
        self.AmlAudioDebugStart_pushButton = QtWidgets.QPushButton(self.AmlAudioDebug_tab)
        self.AmlAudioDebugStart_pushButton.setGeometry(QtCore.QRect(410, 20, 75, 31))
        self.AmlAudioDebugStart_pushButton.setObjectName("AmlAudioDebugStart_pushButton")
        self.AmlAudioDebugMode_groupBox = QtWidgets.QGroupBox(self.AmlAudioDebug_tab)
        self.AmlAudioDebugMode_groupBox.setEnabled(True)
        self.AmlAudioDebugMode_groupBox.setGeometry(QtCore.QRect(0, 0, 91, 101))
        self.AmlAudioDebugMode_groupBox.setObjectName("AmlAudioDebugMode_groupBox")
        self.AmlAudioDebugModeAuto_radioButton = QtWidgets.QRadioButton(self.AmlAudioDebugMode_groupBox)
        self.AmlAudioDebugModeAuto_radioButton.setGeometry(QtCore.QRect(10, 30, 89, 16))
        self.AmlAudioDebugModeAuto_radioButton.setChecked(True)
        self.AmlAudioDebugModeAuto_radioButton.setObjectName("AmlAudioDebugModeAuto_radioButton")
        self.AmlAudioDebugModeManual_radioButton = QtWidgets.QRadioButton(self.AmlAudioDebugMode_groupBox)
        self.AmlAudioDebugModeManual_radioButton.setEnabled(True)
        self.AmlAudioDebugModeManual_radioButton.setGeometry(QtCore.QRect(10, 60, 89, 16))
        self.AmlAudioDebugModeManual_radioButton.setObjectName("AmlAudioDebugModeManual_radioButton")
        self.AmlAudioDebugStop_pushButton = QtWidgets.QPushButton(self.AmlAudioDebug_tab)
        self.AmlAudioDebugStop_pushButton.setEnabled(False)
        self.AmlAudioDebugStop_pushButton.setGeometry(QtCore.QRect(410, 70, 75, 31))
        self.AmlAudioDebugStop_pushButton.setObjectName("AmlAudioDebugStop_pushButton")
        self.AmlAudioDebugOptions_groupBox = QtWidgets.QGroupBox(self.AmlAudioDebug_tab)
        self.AmlAudioDebugOptions_groupBox.setGeometry(QtCore.QRect(90, 0, 111, 101))
        self.AmlAudioDebugOptions_groupBox.setObjectName("AmlAudioDebugOptions_groupBox")
        self.AmlAudioDebugOptionsLogcat_checkBox = QtWidgets.QCheckBox(self.AmlAudioDebugOptions_groupBox)
        self.AmlAudioDebugOptionsLogcat_checkBox.setGeometry(QtCore.QRect(20, 80, 81, 16))
        self.AmlAudioDebugOptionsLogcat_checkBox.setChecked(True)
        self.AmlAudioDebugOptionsLogcat_checkBox.setObjectName("AmlAudioDebugOptionsLogcat_checkBox")
        self.AmlAudioDebugOptionsDump_checkBox = QtWidgets.QCheckBox(self.AmlAudioDebugOptions_groupBox)
        self.AmlAudioDebugOptionsDump_checkBox.setGeometry(QtCore.QRect(20, 50, 91, 16))
        self.AmlAudioDebugOptionsDump_checkBox.setChecked(True)
        self.AmlAudioDebugOptionsDump_checkBox.setObjectName("AmlAudioDebugOptionsDump_checkBox")
        self.AmlAudioDebugOptionsDebug_checkBox = QtWidgets.QCheckBox(self.AmlAudioDebugOptions_groupBox)
        self.AmlAudioDebugOptionsDebug_checkBox.setEnabled(True)
        self.AmlAudioDebugOptionsDebug_checkBox.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.AmlAudioDebugOptionsDebug_checkBox.setMouseTracking(True)
        self.AmlAudioDebugOptionsDebug_checkBox.setChecked(True)
        self.AmlAudioDebugOptionsDebug_checkBox.setObjectName("AmlAudioDebugOptionsDebug_checkBox")
        self.AmlAudioDebugPrintDebug_groupBox = QtWidgets.QGroupBox(self.AmlAudioDebug_tab)
        self.AmlAudioDebugPrintDebug_groupBox.setGeometry(QtCore.QRect(200, 50, 111, 51))
        self.AmlAudioDebugPrintDebug_groupBox.setObjectName("AmlAudioDebugPrintDebug_groupBox")
        self.AmlAudioPrintDebugEnable_checkBox = QtWidgets.QCheckBox(self.AmlAudioDebugPrintDebug_groupBox)
        self.AmlAudioPrintDebugEnable_checkBox.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.AmlAudioPrintDebugEnable_checkBox.setObjectName("AmlAudioPrintDebugEnable_checkBox")
        self.AmlAudioDebugCaptureTime_groupBox = QtWidgets.QGroupBox(self.AmlAudioDebug_tab)
        self.AmlAudioDebugCaptureTime_groupBox.setGeometry(QtCore.QRect(200, 0, 111, 51))
        self.AmlAudioDebugCaptureTime_groupBox.setObjectName("AmlAudioDebugCaptureTime_groupBox")
        self.AmlAudioCaptureTime_spinBox = QtWidgets.QSpinBox(self.AmlAudioDebugCaptureTime_groupBox)
        self.AmlAudioCaptureTime_spinBox.setEnabled(True)
        self.AmlAudioCaptureTime_spinBox.setGeometry(QtCore.QRect(20, 20, 42, 22))
        self.AmlAudioCaptureTime_spinBox.setMaximum(1000)
        self.AmlAudioCaptureTime_spinBox.setProperty("value", 3)
        self.AmlAudioCaptureTime_spinBox.setObjectName("AmlAudioCaptureTime_spinBox")
        self.label = QtWidgets.QLabel(self.AmlAudioDebugCaptureTime_groupBox)
        self.label.setGeometry(QtCore.QRect(70, 20, 21, 21))
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setObjectName("label")
        self.AmlAudioCreateZipEnable_checkBox = QtWidgets.QCheckBox(self.AmlAudioDebug_tab)
        self.AmlAudioCreateZipEnable_checkBox.setGeometry(QtCore.QRect(320, 20, 91, 16))
        self.AmlAudioCreateZipEnable_checkBox.setObjectName("AmlAudioCreateZipEnable_checkBox")
        self.AmlDebug_tabWidget.addTab(self.AmlAudioDebug_tab, "")
        self.AmlSystemOperation_tab = QtWidgets.QWidget()
        self.AmlSystemOperation_tab.setObjectName("AmlSystemOperation_tab")
        self.AmlSystemFile_tabWidget = QtWidgets.QTabWidget(self.AmlSystemOperation_tab)
        self.AmlSystemFile_tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 161))
        self.AmlSystemFile_tabWidget.setObjectName("AmlSystemFile_tabWidget")
        self.AmlSystemFilePush_tab = QtWidgets.QWidget()
        self.AmlSystemFilePush_tab.setObjectName("AmlSystemFilePush_tab")
        self.AmlSystemPushCustomPush_pushButton = QtWidgets.QPushButton(self.AmlSystemFilePush_tab)
        self.AmlSystemPushCustomPush_pushButton.setGeometry(QtCore.QRect(510, 110, 61, 23))
        self.AmlSystemPushCustomPush_pushButton.setObjectName("AmlSystemPushCustomPush_pushButton")
        self.label_3 = QtWidgets.QLabel(self.AmlSystemFilePush_tab)
        self.label_3.setGeometry(QtCore.QRect(0, 50, 41, 16))
        self.label_3.setObjectName("label_3")
        self.AmlSystemPushDolbyDtsPush_pushButton = QtWidgets.QPushButton(self.AmlSystemFilePush_tab)
        self.AmlSystemPushDolbyDtsPush_pushButton.setGeometry(QtCore.QRect(510, 40, 61, 23))
        self.AmlSystemPushDolbyDtsPush_pushButton.setObjectName("AmlSystemPushDolbyDtsPush_pushButton")
        self.AmlSystemPushMs12Src_lineEdit = QtWidgets.QLineEdit(self.AmlSystemFilePush_tab)
        self.AmlSystemPushMs12Src_lineEdit.setGeometry(QtCore.QRect(50, 80, 311, 21))
        self.AmlSystemPushMs12Src_lineEdit.setText("")
        self.AmlSystemPushMs12Src_lineEdit.setObjectName("AmlSystemPushMs12Src_lineEdit")
        self.label_2 = QtWidgets.QLabel(self.AmlSystemFilePush_tab)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 41, 16))
        self.label_2.setObjectName("label_2")
        self.AmlSystemPushMs12Dst_lineEdit = QtWidgets.QLineEdit(self.AmlSystemFilePush_tab)
        self.AmlSystemPushMs12Dst_lineEdit.setGeometry(QtCore.QRect(380, 80, 121, 21))
        self.AmlSystemPushMs12Dst_lineEdit.setObjectName("AmlSystemPushMs12Dst_lineEdit")
        self.AmlSystemPushDtsSrc_lineEdit = QtWidgets.QLineEdit(self.AmlSystemFilePush_tab)
        self.AmlSystemPushDtsSrc_lineEdit.setGeometry(QtCore.QRect(50, 50, 311, 21))
        self.AmlSystemPushDtsSrc_lineEdit.setObjectName("AmlSystemPushDtsSrc_lineEdit")
        self.AmlSystemPushCustomSrc_lineEdit = QtWidgets.QLineEdit(self.AmlSystemFilePush_tab)
        self.AmlSystemPushCustomSrc_lineEdit.setGeometry(QtCore.QRect(50, 110, 311, 21))
        self.AmlSystemPushCustomSrc_lineEdit.setText("")
        self.AmlSystemPushCustomSrc_lineEdit.setObjectName("AmlSystemPushCustomSrc_lineEdit")
        self.AmlSystemPushAllPush_pushButton = QtWidgets.QPushButton(self.AmlSystemFilePush_tab)
        self.AmlSystemPushAllPush_pushButton.setGeometry(QtCore.QRect(580, 40, 51, 91))
        self.AmlSystemPushAllPush_pushButton.setObjectName("AmlSystemPushAllPush_pushButton")
        self.label_7 = QtWidgets.QLabel(self.AmlSystemFilePush_tab)
        self.label_7.setGeometry(QtCore.QRect(360, 80, 21, 21))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.AmlSystemFilePush_tab)
        self.label_5.setGeometry(QtCore.QRect(0, 110, 51, 16))
        self.label_5.setObjectName("label_5")
        self.AmlSystemPushMs12Push_pushButton = QtWidgets.QPushButton(self.AmlSystemFilePush_tab)
        self.AmlSystemPushMs12Push_pushButton.setGeometry(QtCore.QRect(510, 80, 61, 23))
        self.AmlSystemPushMs12Push_pushButton.setObjectName("AmlSystemPushMs12Push_pushButton")
        self.label_8 = QtWidgets.QLabel(self.AmlSystemFilePush_tab)
        self.label_8.setGeometry(QtCore.QRect(360, 110, 21, 21))
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.AmlSystemFilePush_tab)
        self.label_4.setGeometry(QtCore.QRect(0, 80, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.AmlSystemFilePush_tab)
        self.label_6.setGeometry(QtCore.QRect(360, 40, 21, 21))
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.AmlSystemFilePush_tab)
        self.label_10.setGeometry(QtCore.QRect(390, 0, 111, 16))
        self.label_10.setObjectName("label_10")
        self.AmlSystemPushDolbyDtsDst_lineEdit = QtWidgets.QLineEdit(self.AmlSystemFilePush_tab)
        self.AmlSystemPushDolbyDtsDst_lineEdit.setGeometry(QtCore.QRect(380, 40, 121, 21))
        self.AmlSystemPushDolbyDtsDst_lineEdit.setObjectName("AmlSystemPushDolbyDtsDst_lineEdit")
        self.label_9 = QtWidgets.QLabel(self.AmlSystemFilePush_tab)
        self.label_9.setGeometry(QtCore.QRect(140, 0, 101, 16))
        self.label_9.setObjectName("label_9")
        self.AmlSystemPushCustomDst_lineEdit = QtWidgets.QLineEdit(self.AmlSystemFilePush_tab)
        self.AmlSystemPushCustomDst_lineEdit.setGeometry(QtCore.QRect(380, 110, 121, 21))
        self.AmlSystemPushCustomDst_lineEdit.setObjectName("AmlSystemPushCustomDst_lineEdit")
        self.AmlSystemPushDolbySrc_lineEdit = QtWidgets.QLineEdit(self.AmlSystemFilePush_tab)
        self.AmlSystemPushDolbySrc_lineEdit.setGeometry(QtCore.QRect(50, 20, 311, 21))
        self.AmlSystemPushDolbySrc_lineEdit.setText("")
        self.AmlSystemPushDolbySrc_lineEdit.setObjectName("AmlSystemPushDolbySrc_lineEdit")
        self.AmlSystemFile_tabWidget.addTab(self.AmlSystemFilePush_tab, "")
        self.AmlSystemFilePullh_tab = QtWidgets.QWidget()
        self.AmlSystemFilePullh_tab.setObjectName("AmlSystemFilePullh_tab")
        self.label_11 = QtWidgets.QLabel(self.AmlSystemFilePullh_tab)
        self.label_11.setGeometry(QtCore.QRect(390, 0, 111, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.AmlSystemFilePullh_tab)
        self.label_12.setGeometry(QtCore.QRect(140, 0, 101, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.AmlSystemFilePullh_tab)
        self.label_13.setGeometry(QtCore.QRect(350, 20, 21, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.AmlSystemFilePullh_tab)
        self.label_14.setGeometry(QtCore.QRect(0, 20, 51, 16))
        self.label_14.setObjectName("label_14")
        self.AmlSystemPullCustom1Dst_lineEdit = QtWidgets.QLineEdit(self.AmlSystemFilePullh_tab)
        self.AmlSystemPullCustom1Dst_lineEdit.setGeometry(QtCore.QRect(370, 20, 131, 21))
        self.AmlSystemPullCustom1Dst_lineEdit.setObjectName("AmlSystemPullCustom1Dst_lineEdit")
        self.AmlSystemPullCustom1Src_lineEdit = QtWidgets.QLineEdit(self.AmlSystemFilePullh_tab)
        self.AmlSystemPullCustom1Src_lineEdit.setGeometry(QtCore.QRect(50, 20, 301, 21))
        self.AmlSystemPullCustom1Src_lineEdit.setText("")
        self.AmlSystemPullCustom1Src_lineEdit.setObjectName("AmlSystemPullCustom1Src_lineEdit")
        self.AmlSystemPullCustom1Pull__pushButton = QtWidgets.QPushButton(self.AmlSystemFilePullh_tab)
        self.AmlSystemPullCustom1Pull__pushButton.setGeometry(QtCore.QRect(510, 20, 61, 23))
        self.AmlSystemPullCustom1Pull__pushButton.setObjectName("AmlSystemPullCustom1Pull__pushButton")
        self.label_28 = QtWidgets.QLabel(self.AmlSystemFilePullh_tab)
        self.label_28.setGeometry(QtCore.QRect(0, 50, 51, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.AmlSystemFilePullh_tab)
        self.label_29.setGeometry(QtCore.QRect(350, 50, 21, 21))
        self.label_29.setObjectName("label_29")
        self.AmlSystemPullCustom2Dst_lineEdit = QtWidgets.QLineEdit(self.AmlSystemFilePullh_tab)
        self.AmlSystemPullCustom2Dst_lineEdit.setGeometry(QtCore.QRect(370, 50, 131, 21))
        self.AmlSystemPullCustom2Dst_lineEdit.setObjectName("AmlSystemPullCustom2Dst_lineEdit")
        self.AmlSystemPullCustom2Pull2__pushButton = QtWidgets.QPushButton(self.AmlSystemFilePullh_tab)
        self.AmlSystemPullCustom2Pull2__pushButton.setGeometry(QtCore.QRect(510, 50, 61, 23))
        self.AmlSystemPullCustom2Pull2__pushButton.setObjectName("AmlSystemPullCustom2Pull2__pushButton")
        self.AmlSystemPullCustom2Src_lineEdit = QtWidgets.QLineEdit(self.AmlSystemFilePullh_tab)
        self.AmlSystemPullCustom2Src_lineEdit.setGeometry(QtCore.QRect(50, 50, 301, 21))
        self.AmlSystemPullCustom2Src_lineEdit.setText("")
        self.AmlSystemPullCustom2Src_lineEdit.setObjectName("AmlSystemPullCustom2Src_lineEdit")
        self.AmlSystemFile_tabWidget.addTab(self.AmlSystemFilePullh_tab, "")
        self.AmlSystemOperationSystem_groupBox = QtWidgets.QGroupBox(self.AmlSystemOperation_tab)
        self.AmlSystemOperationSystem_groupBox.setGeometry(QtCore.QRect(640, 0, 91, 121))
        self.AmlSystemOperationSystem_groupBox.setObjectName("AmlSystemOperationSystem_groupBox")
        self.AmlSystemRemount_pushButton = QtWidgets.QPushButton(self.AmlSystemOperationSystem_groupBox)
        self.AmlSystemRemount_pushButton.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.AmlSystemRemount_pushButton.setObjectName("AmlSystemRemount_pushButton")
        self.AmlSystemReboot_pushButton = QtWidgets.QPushButton(self.AmlSystemOperationSystem_groupBox)
        self.AmlSystemReboot_pushButton.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.AmlSystemReboot_pushButton.setObjectName("AmlSystemReboot_pushButton")
        self.AmlSystemCloseAvb_pushButton = QtWidgets.QPushButton(self.AmlSystemOperationSystem_groupBox)
        self.AmlSystemCloseAvb_pushButton.setGeometry(QtCore.QRect(10, 80, 75, 23))
        self.AmlSystemCloseAvb_pushButton.setObjectName("AmlSystemCloseAvb_pushButton")
        self.AmlDebug_tabWidget.addTab(self.AmlSystemOperation_tab, "")
        self.AmlDebugTerminalLog_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.AmlDebugTerminalLog_groupBox.setGeometry(QtCore.QRect(0, 200, 741, 341))
        self.AmlDebugTerminalLog_groupBox.setObjectName("AmlDebugTerminalLog_groupBox")
        self.AmlAudioTerminalLog_textBrowser = QtWidgets.QTextBrowser(self.AmlDebugTerminalLog_groupBox)
        self.AmlAudioTerminalLog_textBrowser.setEnabled(True)
        self.AmlAudioTerminalLog_textBrowser.setGeometry(QtCore.QRect(0, 20, 731, 311))
        self.AmlAudioTerminalLog_textBrowser.setMouseTracking(False)
        self.AmlAudioTerminalLog_textBrowser.setObjectName("AmlAudioTerminalLog_textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.AmlDebug_tabWidget.setCurrentIndex(0)
        self.AmlSystemFile_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AmlAudioDebugStart_pushButton.setText(_translate("MainWindow", "Start"))
        self.AmlAudioDebugMode_groupBox.setTitle(_translate("MainWindow", "Mode"))
        self.AmlAudioDebugModeAuto_radioButton.setText(_translate("MainWindow", "Auto"))
        self.AmlAudioDebugModeManual_radioButton.setText(_translate("MainWindow", "Manual"))
        self.AmlAudioDebugStop_pushButton.setText(_translate("MainWindow", "Stop"))
        self.AmlAudioDebugOptions_groupBox.setTitle(_translate("MainWindow", "Options"))
        self.AmlAudioDebugOptionsLogcat_checkBox.setText(_translate("MainWindow", "Logcat"))
        self.AmlAudioDebugOptionsDump_checkBox.setText(_translate("MainWindow", "Dump Data"))
        self.AmlAudioDebugOptionsDebug_checkBox.setText(_translate("MainWindow", "Debug Info"))
        self.AmlAudioDebugPrintDebug_groupBox.setTitle(_translate("MainWindow", "Print Debug"))
        self.AmlAudioPrintDebugEnable_checkBox.setText(_translate("MainWindow", "Enable"))
        self.AmlAudioDebugCaptureTime_groupBox.setTitle(_translate("MainWindow", "Capture Time(s)"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\">s</span></p></body></html>"))
        self.AmlAudioCreateZipEnable_checkBox.setText(_translate("MainWindow", "Create Zip"))
        self.AmlDebug_tabWidget.setTabText(self.AmlDebug_tabWidget.indexOf(self.AmlAudioDebug_tab), _translate("MainWindow", "Audio Debug"))
        self.AmlSystemPushCustomPush_pushButton.setText(_translate("MainWindow", "Push"))
        self.label_3.setText(_translate("MainWindow", "Dts:"))
        self.AmlSystemPushDolbyDtsPush_pushButton.setText(_translate("MainWindow", "Push"))
        self.label_2.setText(_translate("MainWindow", "Dolby:"))
        self.AmlSystemPushAllPush_pushButton.setText(_translate("MainWindow", "Push\n"
"All"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600;\">&gt;</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Custom:"))
        self.AmlSystemPushMs12Push_pushButton.setText(_translate("MainWindow", "Push"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600;\">&gt;</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Ms12:"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600;\">&gt;</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Destination path"))
        self.label_9.setText(_translate("MainWindow", "Source path"))
        self.AmlSystemFile_tabWidget.setTabText(self.AmlSystemFile_tabWidget.indexOf(self.AmlSystemFilePush_tab), _translate("MainWindow", "Push"))
        self.label_11.setText(_translate("MainWindow", "Destination path"))
        self.label_12.setText(_translate("MainWindow", "Source path"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600;\">&gt;</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Custom:"))
        self.AmlSystemPullCustom1Pull__pushButton.setText(_translate("MainWindow", "Pull"))
        self.label_28.setText(_translate("MainWindow", "Custom:"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600;\">&gt;</span></p></body></html>"))
        self.AmlSystemPullCustom2Pull2__pushButton.setText(_translate("MainWindow", "Pull"))
        self.AmlSystemFile_tabWidget.setTabText(self.AmlSystemFile_tabWidget.indexOf(self.AmlSystemFilePullh_tab), _translate("MainWindow", "Pull"))
        self.AmlSystemOperationSystem_groupBox.setTitle(_translate("MainWindow", "system"))
        self.AmlSystemRemount_pushButton.setText(_translate("MainWindow", "Remount"))
        self.AmlSystemReboot_pushButton.setText(_translate("MainWindow", "Reboot"))
        self.AmlSystemCloseAvb_pushButton.setText(_translate("MainWindow", "Close AVB"))
        self.AmlDebug_tabWidget.setTabText(self.AmlDebug_tabWidget.indexOf(self.AmlSystemOperation_tab), _translate("MainWindow", "System Operation"))
        self.AmlDebugTerminalLog_groupBox.setTitle(_translate("MainWindow", "Terminal log"))
        self.AmlAudioTerminalLog_textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
