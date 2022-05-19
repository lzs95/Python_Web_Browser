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
        #Home Button
        home_button = QAction("Home", self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)
        #Url_Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        #Url_Search_Bar
        # self.url_search_bar = QLineEdit()
        # self.url_bar.returnPressed.connect(self.search)
        # navbar.addWidget(self.url_search_bar)
        #Capture URL Chain
        self.browser.urlChanged.connect(self.url_update)
        
    #Home button returns to specified Website    
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))
    
    def navigate_to_url(self):
        #Gets input from url_bar
        url = self.url_bar.text()
        if "https://" in url:
            self.browser.setUrl(QUrl(url))
        else:
            print('not')
            self.browser.setUrl(QUrl(f"https://{url}.com"))
        
    def url_update(self, url):
        self.url_bar.setText(url.toString())
        
    # def search(self):
    #     url2 = self.url_search_bar.text()
    #     self.browser.setUrl(QUrl(f"https://duckduckgo.com/?q={url2}&t=h_&ia=web"))
    #     self.navigate_to_url()
    
        
    
     
# QApplication Handles Events and Initialisation   
app = QApplication(sys.argv)
QApplication.setApplicationName('Muh Chrome')
window = MainWindow()
app.exec_()      