from PyQt5.QtWidgets import *
from view import *
import csv

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.calendarWidget.selectionChanged.connect(self.date_changed)
        self.button_add_task.clicked.connect(lambda: self.add_task())
        self.button_get_info.clicked.connect(lambda: self.get_info())
        self.button_task_database.clicked.connect(lambda: self.task_database())
        self.task_name = []
        self.task_description = []
        self.task_from_dt = []
        self.task_to_dt = []
        self.calendarWidget.setMinimumDate(self.calendarWidget.selectedDate())
        self.from_date_time.setMinimumDate(self.calendarWidget.selectedDate())
        self.to_date_time.setMinimumDate(self.calendarWidget.selectedDate())


    def date_changed(self)->None:
        date_picked = self.calendarWidget.selectedDate()
        self.from_date_time.setDate(date_picked)
        self.to_date_time.setDate(date_picked)


    def add_task(self)->None:
        self.task_name.append(self.add_task_name.text())

        self.task_description.append(self.add_task_description.toPlainText())

        self.task_from_dt.append(self.from_date_time.dateTime().toString(self.from_date_time.displayFormat()))

        self.task_to_dt.append(self.to_date_time.dateTime().toString(self.to_date_time.displayFormat()))

        self.add_task_name.setText('')
        self.add_task_description.setText('')

    def get_info(self)->None:
        try:
            searching_task = self.get_info_task.text()
            index = self.task_name.index(searching_task)
            self.task_info_description.setText(self.task_description[index])
        except ValueError:
            warning_msg = QMessageBox()
            warning_msg.setWindowTitle('ERROR')
            warning_msg.setText('Task Does Not Exist. Try Again')
            warning_msg.setIcon(QMessageBox.Warning)
            warning_msg.setStandardButtons(QMessageBox.Retry)
            x = warning_msg.exec_()



    def task_database(self)->None:
        file_name = self.database_name.text()
        file_name_check = " " in file_name
        try:
            if file_name_check:
                raise ValueError
            else:
                field = ('Task', 'Task Description', 'From', 'To')
                with open(f'{file_name}', 'w', newline='') as csvfile:
                    content = csv.writer(csvfile, delimiter=',')
                    content.writerow(field)
                    for x in range(len(self.task_name)):
                        content.writerow([self.task_name[x], self.task_description[x], self.task_from_dt[x], self.task_to_dt[x]])

                self.database_name.setText('')

        except ValueError:
                error_msg = QMessageBox()
                error_msg.setWindowTitle('ERROR')
                error_msg.setText('Invalid file name. Try Again')
                error_msg.setIcon(QMessageBox.Critical)
                error_msg.setStandardButtons(QMessageBox.Retry)
                x = error_msg.exec_()














