import sys
import os
from PySide2.QtWidgets import *
from PySide2.QtCore import * 
from PySide2.QtGui import * 


class MyTree(QTreeWidget):
    def __init__(self, parent=None):
        super(MyTree, self).__init__(parent=parent)
        self.startDir = "C:/Users/Han/Desktop/python"
        self.fillTree()
        self.show()

    def fillTree(self):        
        def iterate(currentDir, currentItem):            
            for f in os.listdir(currentDir):
                path = os.path.join(currentDir, f)
                if os.path.isdir(path):
                    dirItem = QTreeWidgetItem(currentItem)
                    dirItem.setText(0, f)
                    iterate(path, dirItem)
                else:
                    fileItem = QTreeWidgetItem(currentItem)
                    fileItem.setText(0, f)
        iterate(self.startDir, self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyTree()
    sys.exit(app.exec_())