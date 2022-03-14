import sys
import os
from PySide2.QtWidgets import *

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self._generateUI()
        #self._simple_tree_widget()
        self.load_project_structure()
        self.startpath = "D:\\"
        
    def _generateUI(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        self.tree_widget = QTreeWidget()
        main_layout.addWidget(self.tree_widget)

    def load_project_structure(self.startpath, tree):
        for element in os.listdir(startpath):
            path_info = self.startpath + "/" + element
            parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
            if os.path.isdir(path_info):
                load_project_structure(path_info, parent_itm)
                #parent_itm.setIcon(0, QIcon('assets/folder.ico'))
            else:
                pass
                #parent_itm.setIcon(0, QIcon('assets/file.ico'))

    # def _tree_widget2(self):
    #     ...

def launch():
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    widget = MyMainWindow()
    widget.show()
    app.exec_()

launch()