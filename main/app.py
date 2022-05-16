from imp import reload
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5.QtWebEngineWidgets import *

# Widgets are Graphical Elements example: Buttons,Text_field,Containers...
# Main Window Handles Graphics and Logic
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://duckduckgo.com/"))
        self.setCentralWidget(self.browser)
        super().showMaximized()
        
        #Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)  
        #Back Button    
        back_button = QAction('Back',self)
        #When back button is triggered use browser's back method
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)
        #Foward Button
        forward_button = QAction("Forward",self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)
        #Refresh Button
        reload_button = QAction('Reload',self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)
    
        
     
# QApplication Handles Events and Initialisation   
app = QApplication(sys.argv)
QApplication.setApplicationName('My Browser')
window = MainWindow()
app.exec_()      