from window2 import *


class Browser(QGraphicsView):

    def __init__(self, parent):
        super(Browser, self).__init__(parent)
        self.page = Window2(self)
        self.setScene(self.page)
        
