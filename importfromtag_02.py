#coding:utf-8
import os
import sys
import re
import glob
try:
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *
    from PySide2 import QtCore, QtGui, QtWidgets
except:
    from PySide.QtCore import *
    from PySide.QtGui import *
    from PySide.QtUiTools import *

import nuke
import nukescripts


class ImportFromTag(QWidget):

    def __init__(self):
        super(ImportFromTag, self).__init__()

        # ui 경로
        uiFilepath = "C:\Users\Han\Desktop\pyside2\ui\importfromtag.ui"
        uiFile = QFile(uiFilepath)
        uiFile.open(QFile.Readonly)
        self.ui = QUiLoader().load(uiFile)
        uiFile.close()

        # 기능연결

        self.project_LE.setText(self.current_nk_project())
        # 버튼설정
        self.call_Btn.clicked.connect(self.call)
        self.cancel_Btn.clicked.connect(self.quit)

        # type 설정
        self.org_CHBox.stateChanged.connect(self.find_org)
        self.output_CHBox.stateChanged.connect(self.find_output)

        # status 설정
        self.status_CB.additems(["ALL",""])

    # find_org와 find_output의 샷리스트를 받아서
    # read로 가져옴
    def call(self):
        if self.org_CBox.isChecked() == True:
            pass

        if self.output_CBox.isChecked() == True:
            pass

        if self.org_CBox.isChecked() == False and self.output_CBox.isChecked() == False:
            nuke.message("type을 설정해주세요")
            return
        # 마지막 종료되게
       
        
    # 그냥 나가는 함수
    def quit(self):
        # Cancle 버튼 눌렀을 때
        print("quit")


    # Project input 받는 함수        
    def get_project(self):
        
        # line edit에 있는 text를 받는 메소드
        self.project = self.project_LE.text()
        if self.project == "":
            nuke.message("projcet를 입력해주세요")
        return self.project


    # Tag input 받는 함수
    def get_tag(self):

        # line edit에 있는 text를 받는 메소드
        self.tag = self.tag_LE.text()
        if self.tag == "":
            nuke.message("tag를 입력해주세요")
        return self.tag
        
    # Status combobox 받는 함수    
    # 디폴트 all로 설정
    def get_status(self):
        # combobox의 값을 받는 메소드
        self.status = self.status_CB.currentText()

        return self.status


    #Project, Tag, Status를 받아서 샷리스트반환하는 함수
    def make_shotlist(self):      
        pass


    # 샷리스틑 받아서 org경로를 찾아주는 함수    
    def find_org(self):
        pass


    # 샷리스틑 받아서 output경로를 찾아주는 함수
    def find_output(self):
        pass

    # 현재 누크프로젝트의 프로젝트를 가져와 넣는 함수    
    def current_nk_project(self):
        pass
        # 프로젝트 찾는거 없을경우도
        

    
    # 컬러스페이스와 확장자찾는 함수
    # 2가지 return
    def color_ext(self,path):
        pass


    # Read노드로 부르는 함수
    # call 버튼에 넣기
    def make_read_node(self):   
        pass
    

    

    # 실행
    def main():
        global app
        try:
            app.close()

        except:
            pass
        app = ImportFromTag()
        app.show












