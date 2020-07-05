##############################################
#    Covid-19 Tracker (State Wise) - India   #
#    Written by : Krishnendu Bhowmick        #
#    Mail ID: 9635.krishnendu@gmail.com      #
##############################################

# importing libraries
import sys
import requests
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel)
from bs4 import BeautifulSoup


class Window2(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title
        self.setWindowTitle("About Me")
        self.setWindowIcon(QtGui.QIcon('aboutme.png'))

        # setting  the geometry of window
        self.setGeometry(0, 0, 400, 300)

        # creating a label widget
        self.label_1 = QLabel('Written by:\nKrishnendu Bhowmick\nMail ID : 9635.krishnendu@gmail.com\nFB : fb.com/iamkbhowmick', self)

        # moving position
        self.label_1.move(80, 80)

        # setting up border
        self.label_1.setStyleSheet("border: 1px solid black;")
        self.label_1.setFixedWidth(250)
        self.label_1.setFixedHeight(60)
        # setting alignment to left
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)

        # creating a label widget
        self.label_2 = QLabel('All COVID-19 data source taken from\n https://www.mohfw.gov.in', self)

        # moving position
        self.label_2.move(80, 145)

        # setting up border
        self.label_2.setStyleSheet("border: 1px solid black;")
        self.label_2.setFixedWidth(250)
        self.label_2.setFixedHeight(50)
        # setting alignment to centre
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        # creating a label widget
        self.label_3 = QLabel('Platform use : Python 3.8. \nLibraries are : requestes, urllib3, sys, Qt5, bs4', self)

        # moving position
        self.label_3.move(80, 200)

        # setting up border
        self.label_3.setStyleSheet("border: 1px solid black;")
        self.label_3.setFixedWidth(250)
        self.label_3.setFixedHeight(50)
        # setting alignment to right
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

        # show all the widgets
        self.show()

    # create pyqt5 app

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Covid19 Tracker(State Wise) by Krishnendu ")
        self.setWindowIcon(QtGui.QIcon('covidindia.png'))
        # setting geometry
        self.setGeometry(100, 100, 400, 500)

        # calling method
        self.corona()

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    def corona(self):
        extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
        URL = 'https://www.mohfw.gov.in/'

        SHORT_HEADERS = ['SNo', 'State', 'Indian-Confirmed',
                         'Foreign-Confirmed', 'Cured', 'Death']

        response = requests.get(URL).content
        soup = BeautifulSoup(response, 'html.parser')
        header = extract_contents(soup.tr.find_all('th'))

        self.stats = []
        all_rows = soup.find_all('tr')

        for row in all_rows:
            stat = extract_contents(row.find_all('td'))
            if stat:
                if len(stat) == 6:
                    # last row
                    stat = ['', *stat]
                    self.stats.append(stat)
                elif len(stat) == 7:
                    self.stats.append(stat)

        self.stats[-1][1] = "Total Cases"

        self.stats.remove(self.stats[-1])

    # method for widgets
    def UiComponents(self):

        # creating a combo box widget
        self.combo_box = QComboBox(self)

        # setting geometry to combo box
        self.combo_box.setGeometry(100, 15, 200, 40)

        # setting font
        self.combo_box.setFont(QFont('Times', 10))

        # adding items to combo box
        for i in self.stats:
            self.combo_box.addItem(i[2])

        # adding action to the combo box
        self.combo_box.activated.connect(self.get_cases)
        # adding image
        self.label2 = QLabel(self)
        self.label2.setFixedWidth(250)
        self.label2.setFixedHeight(100)
        self.label2.move(75, 93)
        self.pixmap = QPixmap('coronaupdate.jpg')
        self.label2.setPixmap(self.pixmap)
        self.label2.resize(self.pixmap.width(),
                          self.pixmap.height())
        # Mid section label
        self.label1 = QLabel("This is a desktop application for Covid19 state wise tracking purpose\nAll data update automatically from \nhttps://www.mohfw.gov.in\n via Web Scraping", self)
        self.label1.setFixedWidth(350)
        self.label1.setFixedHeight(250)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.move(25,100)
        # creating label to show the total cases
        self.label_total = QLabel("Total Cases ", self)

        # setting geometry
        self.label_total.setGeometry(100, 270, 200, 40)

        # setting alignment to the text
        self.label_total.setAlignment(Qt.AlignCenter)

        # adding border to the label
        self.label_total.setStyleSheet("border : 2px solid black;")

        # creating label to show the recovered cases
        self.label_reco = QLabel("Recovered Cases ", self)

        # setting geometry
        self.label_reco.setGeometry(100, 312, 200, 40)

        # setting alignment to the text
        self.label_reco.setAlignment(Qt.AlignCenter)

        # adding border
        self.label_reco.setStyleSheet("border : 2px solid black;")

        # creating label to show death cases
        self.label_death = QLabel("Total Deaths ", self)

        # setting geometry
        self.label_death.setGeometry(100, 354, 200, 40)

        # setting alignment to the text
        self.label_death.setAlignment(Qt.AlignCenter)

        # adding border to the label
        self.label_death.setStyleSheet("border : 2px solid black;")

        # creating label to show confirmed cases
        self.label_confirmed = QLabel("Total Deaths ", self)

        # setting geometry
        self.label_confirmed.setGeometry(100, 395, 200, 40)

        # setting alignment to the text
        self.label_confirmed.setAlignment(Qt.AlignCenter)

        # adding border to the label
        self.label_confirmed.setStyleSheet("border : 2px solid black;")

        # Start button for about Me
        self.pushButton = QPushButton("About Me", self)
        self.pushButton.move(150, 470)
        self.pushButton.setToolTip("<h3>Click to know about Krishnendu Bhowmick</h3>")
        self.pushButton.clicked.connect(self.window2)  # <===

    # method called by push
    def get_cases(self):

        # getting index
        index = self.combo_box.currentIndex()

        # getting data
        total = self.stats[index][3]
        recovered = self.stats[index][4]
        deaths = self.stats[index][5]
        confirmed = self.stats[index][6]

        # show data through labels
        self.label_total.setText("Active Cases : " + total)
        self.label_reco.setText("Recovered Cases : " + recovered)
        self.label_death.setText("Total Deaths : " + deaths)
        self.label_confirmed.setText("Total Confirmed : " + confirmed)

    # About Me box
    def window2(self):  # <===
        self.w = Window2()
        self.w.show()
    # self.hide()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())
