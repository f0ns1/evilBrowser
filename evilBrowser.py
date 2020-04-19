from mainWindowF0ns1 import *



def main():
    app = QApplication(sys.argv)
    win = MainWindowF0ns1()
    win.showMaximized()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main()) 
