import sys
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import * 
from evilTerminal import *


class Window2(QGraphicsScene):
    
    def __init__(self, view):
        super(Window2, self).__init__(view)
        
        _layout = QVBoxLayout(view)
        self.view = view
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.setStyleSheet("* { background-image: url('background.jpg'); color: white; font-size: large; font-weight: bold;}")
        self.tabs.currentChanged.connect(self.currentTabChanged)
        self.tabs.tabCloseRequested.connect(self.closeCurrentTab)
        
        self.history = [] # list of strings, string = "title;URL" needed for writing history in a file
        self.historyForEachTab = {} # key = tabIndex, value = tabIndexHistory - needed for back and forward methods
        self.addNewTab()
    
        button = QPushButton(QIcon('background.jpg'), 'evil')
        button.setStatusTip('Evil!!')
        button.clicked.connect(self.addNewTab) 
        self.tabs.setCornerWidget(button, Qt.TopLeftCorner)

        self.setBackgroundBrush(QBrush(QColor("background.jpg")))
        
        _layout.addWidget(self.tabs)
        
        
    def currentTabChanged(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.updateTitle(self.tabs.currentWidget())

    def closeCurrentTab(self, i):
        
        print(i)
        if self.tabs.count() < 2:
            return
        for j in range(i, self.tabs.count() - 1):
            self.historyForEachTab[j] = self.historyForEachTab[j+1]
            
        for j in range(i, self.tabs.count()):
            self.tabs.widget(j).loadFinished.disconnect()
            self.tabs.widget(j).loadFinished.connect(lambda _, i=j-1, web=self.tabs.widget(j): self.tabs.setTabText(i, web.title()))
            self.tabs.widget(j).loadFinished.connect(lambda _, web=self.tabs.widget(j): self.addToHistory(web.title(), web.url().toString()))

        self.tabs.removeTab(i)

    def addNewTab(self):
        qurl = QUrl('https://github.com/f0ns1/cryptoServer')
        web = QWebView()
        web.load(QUrl("https://github.com/f0ns1/cryptoServer"))
        i = self.tabs.addTab(web, "F0ns1")
        self.tabs.setCurrentIndex(i)
        web.urlChanged.connect(lambda qurl, web=web: self.update_urlbar(qurl, web))
        web.loadFinished.connect(lambda _, i=i, web=web: self.tabs.setTabText(i, web.title()))
        self.historyForEachTab[i] = self.tabs.currentWidget().page().history()

    def update_urlbar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return
        self.parent().parent().addressBar.setText(q.toString()) 
    def updateTitle(self, browser):
        if browser != self.tabs.currentWidget():
            return
        title = self.tabs.currentWidget().title()
        self.view.parent().setWindowTitle(title)



    def terminalButtonPush(self):
        term = Terminal()
        exit_status = term.run(sys.argv)
        
        
        
    def forwardButtonPush(self):
        self.historyForEachTab[self.tabs.currentIndex()].forward()
        
    def backButtonPush(self):
        self.historyForEachTab[self.tabs.currentIndex()].back()

    def refreshButtonPush(self):
        self.tabs.currentWidget().reload()

    def homeButtonPush(self):
        self.tabs.currentWidget().load(QUrl('https://www.google.com/'))

    def goButtonPush(self, address):
        tmp = address
        
        if(tmp == ''):
            return
        
        q = QUrl(tmp)
        if(q.scheme() == ""):
            q.setScheme("http")
            
        if(tmp.find('.') != -1 and tmp.find(' ') == -1):
            self.tabs.currentWidget().load(q)
                
        else:
            l = tmp.split()
            link = 'https://www.google.com/search?q=' + l[0]
            for i in range(1, len(l)):
                link += '+' + l[i]
            self.tabs.currentWidget().load(QUrl(link))
