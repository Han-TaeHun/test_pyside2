#coding:utf8
import os
import sys
import re

#import csi3
#import nuke
#import nukescripts

# UI구성
class ImportFromTag( nukescripts.PythonPanel ):

    def __init__( self ):

        nukescripts.PythonPanel.__init__( self, "ImportFromTag" )
        self.projectKnob = nuke.String_Knob("{}".format(""), "Project")
        self.tag_shotKnob = nuke.Enumeration_Knob("Tag&Shot", "", ["Tag", "Shot"])
        self.inputKnob = nuke.String_Knob("", "")
        self.inputKnob.clearFlag(nuke.STARTLINE)
        self.plateKnob = nuke.Bitmask_Knob("Type", "Type", ["org", "output"])

        for k in ( self.projectKnob,  self.tag_shotKnob, self.inputKnob, self.plateKnob ):
            self.addKnob( k )

    def call_project(self):
        # project 찾는 함수
        pass

# 반복될 코드들 
class CallDef:
    def __init__(self, project):
        self.project = project
        
    def aaa(self):
        # org 가져오는 함수
        pass

    def bbb(self):
        # output 가져오는 함수
        pass

    def ccc(self):
        # path 경로?
        pass

# UI 불러오기
p = ImportFromTag()
p.showModalDialog()

#프로젝트는....생각해보고
# Tag로 찾을때
if p.tag_shotKnob.value() == "Tag":

    if not p.inputKnob.value() == "":

        if p.plateKnob.value() == "org":
            # tag를 통한 org 불러오는 함수
            pass

        if p.plateKnob.value() == "output":
            # tag를 통한 output 불러오는 함수
            pass        

        if p.plateKnob.value() == "all":
            # tag를 통한 org&output 불러오는 함수
            pass

    else:
        nuke.message("Tag를 입력해주세요")

# Shot으로 찾을 때
if p.tag_shotKnob.value() == "Shot":

    if not p.inputKnob.value() == "":

        if p.plateKnob.value() == "org":
            # shot를 통한 org 불러오는 함수
            pass

        if p.plateKnob.value() == "output":
            # shot를 통한 output 불러오는 함수
            pass        

        if p.plateKnob.value() == "all":
            # shot를 통한 org&output 불러오는 함수
            pass

    else:
        nuke.message("Shotname을 입력해주세요")














































