# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 474)
        MainWindow.setMinimumSize(QtCore.QSize(782, 474))
        MainWindow.setMaximumSize(QtCore.QSize(782, 474))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(26)
        MainWindow.setFont(font)
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 90, 391, 221))
        self.calendarWidget.setMouseTracking(False)
        self.calendarWidget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(255, 255, 127);\n"
"selection-color: rgb(85, 85, 85);\n"
"selection-background-color: rgb(51, 51, 51);\n"
"\n"
"\n"
"alternate-background-color: rgb(177, 20, 25);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.calendarWidget.setObjectName("calendarWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(410, 90, 361, 331))
        self.tabWidget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.Tab = QtWidgets.QWidget()
        self.Tab.setObjectName("Tab")
        self.to_date_time = QtWidgets.QDateTimeEdit(self.Tab)
        self.to_date_time.setGeometry(QtCore.QRect(10, 270, 211, 21))
        self.to_date_time.setStyleSheet("font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 85);")
        self.to_date_time.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 12, 1), QtCore.QTime(23, 59, 0)))
        self.to_date_time.setDate(QtCore.QDate(2022, 12, 1))
        self.to_date_time.setTime(QtCore.QTime(23, 59, 0))
        self.to_date_time.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 12, 1), QtCore.QTime(0, 0, 0)))
        self.to_date_time.setMinimumDate(QtCore.QDate(2022, 12, 1))
        self.to_date_time.setCalendarPopup(True)
        self.to_date_time.setObjectName("to_date_time")
        self.from_date_time = QtWidgets.QDateTimeEdit(self.Tab)
        self.from_date_time.setGeometry(QtCore.QRect(10, 210, 211, 22))
        self.from_date_time.setStyleSheet("font: 8pt \"Arial\";\n"
"background-color: rgb(85, 85, 85);\n"
"color: rgb(255, 255, 255);")
        self.from_date_time.setDate(QtCore.QDate(2022, 12, 1))
        self.from_date_time.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 12, 1), QtCore.QTime(0, 0, 0)))
        self.from_date_time.setMinimumDate(QtCore.QDate(2022, 12, 1))
        self.from_date_time.setCalendarPopup(True)
        self.from_date_time.setObjectName("from_date_time")
        self.label_3 = QtWidgets.QLabel(self.Tab)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.add_task_name = QtWidgets.QLineEdit(self.Tab)
        self.add_task_name.setGeometry(QtCore.QRect(10, 30, 331, 21))
        self.add_task_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.add_task_name.setObjectName("add_task_name")
        self.label = QtWidgets.QLabel(self.Tab)
        self.label.setGeometry(QtCore.QRect(10, 250, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Tab)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 55, 16))
        self.label_2.setStyleSheet("font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.button_add_task = QtWidgets.QPushButton(self.Tab)
        self.button_add_task.setGeometry(QtCore.QRect(250, 270, 91, 24))
        self.button_add_task.setStyleSheet("font: 8pt \"Arial\";\n"
"background-color: rgb(177, 20, 25);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"")
        self.button_add_task.setObjectName("button_add_task")
        self.label_4 = QtWidgets.QLabel(self.Tab)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.add_task_description = QtWidgets.QTextEdit(self.Tab)
        self.add_task_description.setGeometry(QtCore.QRect(10, 90, 331, 91))
        self.add_task_description.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.add_task_description.setObjectName("add_task_description")
        self.to_date_time.raise_()
        self.from_date_time.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.button_add_task.raise_()
        self.label_4.raise_()
        self.add_task_description.raise_()
        self.add_task_name.raise_()
        self.tabWidget.addTab(self.Tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 351, 31))
        self.label_5.setStyleSheet("font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.get_info_task = QtWidgets.QLineEdit(self.tab_2)
        self.get_info_task.setGeometry(QtCore.QRect(10, 50, 161, 22))
        self.get_info_task.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.get_info_task.setObjectName("get_info_task")
        self.button_get_info = QtWidgets.QPushButton(self.tab_2)
        self.button_get_info.setGeometry(QtCore.QRect(290, 50, 51, 24))
        self.button_get_info.setStyleSheet("font: 8pt \"Arial\";\n"
"background-color: rgb(177, 20, 25);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;")
        self.button_get_info.setObjectName("button_get_info")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.task_info_description = QtWidgets.QLabel(self.tab_2)
        self.task_info_description.setGeometry(QtCore.QRect(10, 90, 331, 191))
        self.task_info_description.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.task_info_description.setText("")
        self.task_info_description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.task_info_description.setObjectName("task_info_description")
        self.tabWidget.addTab(self.tab_2, "")
        self.monthly_planner = QtWidgets.QLabel(self.centralwidget)
        self.monthly_planner.setGeometry(QtCore.QRect(0, 0, 791, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setUnderline(False)
        self.monthly_planner.setFont(font)
        self.monthly_planner.setStyleSheet("background-color: rgb(4, 4, 4);\n"
"color: white;\n"
"\n"
"")
        self.monthly_planner.setAlignment(QtCore.Qt.AlignCenter)
        self.monthly_planner.setObjectName("monthly_planner")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 60, 791, 16))
        self.label_6.setStyleSheet("background-color: rgb(177, 20, 25);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.button_task_database = QtWidgets.QPushButton(self.centralwidget)
        self.button_task_database.setGeometry(QtCore.QRect(10, 396, 391, 21))
        self.button_task_database.setStyleSheet("font: 8pt \"Arial\";\n"
"background-color: rgb(177, 20, 25);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;")
        self.button_task_database.setObjectName("button_task_database")
        self.database_name = QtWidgets.QLineEdit(self.centralwidget)
        self.database_name.setGeometry(QtCore.QRect(10, 370, 391, 22))
        self.database_name.setObjectName("database_name")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 350, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 8pt \"Arial\";\n"
"color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 320, 391, 16))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_6.raise_()
        self.tabWidget.raise_()
        self.monthly_planner.raise_()
        self.calendarWidget.raise_()
        self.button_task_database.raise_()
        self.database_name.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Task:"))
        self.label.setText(_translate("MainWindow", "To:"))
        self.label_2.setText(_translate("MainWindow", "From:"))
        self.button_add_task.setText(_translate("MainWindow", "Add"))
        self.label_4.setText(_translate("MainWindow", "Task Descritption"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab), _translate("MainWindow", "Add Task"))
        self.label_5.setText(_translate("MainWindow", "Type Exact Task Name"))
        self.button_get_info.setText(_translate("MainWindow", "Info"))
        self.label_7.setText(_translate("MainWindow", "Task:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Task Info"))
        self.monthly_planner.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.monthly_planner.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.monthly_planner.setText(_translate("MainWindow", "Monthly Planner"))
        self.button_task_database.setText(_translate("MainWindow", "Open Task DataBase"))
        self.label_8.setText(_translate("MainWindow", "DataBase File Name:"))
        self.label_9.setText(_translate("MainWindow", "Input a desired file name for your database if not done before "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
