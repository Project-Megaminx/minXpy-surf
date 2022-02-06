import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngine import *

#Window Config
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

#Navigation Bar Config
        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        #go 
        back_btn_navbar = QAction('Go Back',self)
        back_btn_navbar.triggered.connect(self.browser.back)
        navbar.addAction(back_btn_navbar)

        forward_btn_navbar = QAction('Go Forward', self)
        forward_btn_navbar.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn_navbar)

        reload_btn_navbar = QAction('Reload', self)
        reload_btn_navbar.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn_navbar)

        home_btn_navbar = QAction('Home', self)
        home_btn_navbar.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn_navbar)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, live_url):
        self.url_bar.setText(live_url.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('Megaminx Browser')
window = MainWindow()
app.exec()