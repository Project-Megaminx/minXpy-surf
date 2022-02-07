import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("minXsurf-Base.95-22")
        self.setWindowIcon(QIcon("icons/outline_api_black_36dp.png"))

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("icons/outline_arrow_back_black_24dp.png"))
        self.backButton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backButton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("icons/outline_arrow_forward_black_24dp.png"))
        self.forwardButton.clicked.connect(self.forwardBtn)
        toolbar.addWidget(self.forwardButton)

        self.refreshButton = QPushButton()
        self.refreshButton.setIcon(QIcon("icons/outline_refresh_black_24dp.png"))
        self.refreshButton.clicked.connect(self.refreshBtn)
        toolbar.addWidget(self.refreshButton)

        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon("icons/outline_home_black_24dp.png"))
        self.homeButton.clicked.connect(self.homeBtn)
        toolbar.addWidget(self.homeButton)

        self.addressInput = QLineEdit()
        self.addressInput.setFont(QFont("Sanserif", 10))
        toolbar.addWidget(self.addressInput)

        self.goButton = QPushButton()
        self.goButton.setIcon(QIcon("icons/outline_launch_black_24dp.png"))
        self.goButton.clicked.connect(self.searchBtn)
        toolbar.addWidget(self.goButton)


        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = "https://duckduckgo.com"
        self.addressInput.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))

    def searchBtn(self):
        myurl = self.addressInput.text()
        self.webEngineView.load(QUrl(myurl))

    def backBtn(self):
        self.webEngineView.back()

    def forwardBtn(self):
        self.webEngineView.forward()

    def homeBtn(self):
        homeUrl = "https://duckduckgo.com"
        self.webEngineView.load(QUrl(homeUrl))

    def refreshBtn(self):
        self.webEngineView.reload()



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
