from browser import *
from gi.repository import Gtk as gtk
from gi.repository import Gdk as gdk

class MainWindowF0ns1(QMainWindow):

    def __init__(self,parent=None):
        super(MainWindowF0ns1, self).__init__(parent) #super(subClass, instance).__init__(parent)
        self.setGeometry(10, 10, 1000, 800) #setGeometry(topLeftX, topLeftY, width, height)
        
        self.setWindowTitle('Evil Browser')
        self.setWindowIcon(QIcon('web.png'))
        

        self.addressBar = QLineEdit()
        self.addressBar.setPlaceholderText('Search with Google or enter address')
        
        self.createBrowser() # Method that creates graphics view 
        
        #---------------------Toolbar buttons section-----------------------
        tb = self.addToolBar("File")
        tb.setMovable(False)
        self.backAction = QAction(QIcon('back.png'), 'Back', self)
        self.backAction.setShortcut('Ctrl+B')
        self.backAction.triggered.connect(self.browser.page.backButtonPush)

        self.forwardAction = QAction(QIcon('forward.png'), 'Forward', self)
        self.forwardAction.setShortcut('Ctrl+F')
        self.forwardAction.triggered.connect(self.browser.page.forwardButtonPush)

        self.homeAction = QAction(QIcon('home.png'), 'Home', self)
        self.homeAction.setShortcut('Ctrl+H')
        self.homeAction.triggered.connect(self.browser.page.homeButtonPush)
        
        self.goAction = QAction(QIcon('search.png'), 'Go', self)
        self.goAction.setShortcut(Qt.Key_Return)
        self.goAction.triggered.connect(lambda: self.browser.page.goButtonPush(self.addressBar.text()))
        
        self.terminal = QAction(QIcon('background.jpg'), 'Back', self)
        self.terminal.setShortcut('Ctrl+B')
        self.terminal.triggered.connect(self.browser.page.terminalButtonPush)
        
        
        
        tb.addAction(self.backAction)
        tb.addAction(self.forwardAction)
        tb.addAction(self.homeAction)
        tb.addWidget(self.addressBar)
        tb.addAction(self.goAction)
        tb.addAction(self.terminal)
        self.css = b"""* { background-image: url('background.jpg'); color: white; font-size: large; font-weight: bold;}"""
        css_provider = gtk.CssProvider()
        css_provider.load_from_data(self.css)
        context = gtk.StyleContext()
        screen = gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider, gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        
        
    def createBrowser(self):
        self.browser = Browser(self)
        self.setCentralWidget(self.browser)
        
        
    def closeEvent(self, event):  
        
     
        
        reply = QMessageBox.question(self, 'Confirm close',
        "Do you want to close ??", QMessageBox.Yes | 
        QMessageBox.No, QMessageBox.Yes) # parent, title, message, buttons, default button

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 
            
