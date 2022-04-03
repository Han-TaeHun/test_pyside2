#coding:utf8
import re
import os

# 저장경로 가져오기
nk_path = nuke.root().name().replace("C:", "")


class call_path:
    def __init__(self, path):
        path.replace( "\\" , "/" )
        self.path = path

    # 프로젝트 구하기
    def get_project(self):
        
        result = re.findall("/show/(\w+)", self.path)
    
        if result:
            project = result[0]
            return project
    
        else:
            nuke.message( "project 경로를 확인해주세요" )
            

    # 시퀀스 구하기
    def get_seq(self):
        result = re.findall("/show/\w+/seq/(\w+)", self.path)
    
        if result:
            seq = result[0]
            return seq
    
        else:
            nuke.message( "seq 경로를 확인해주세요" )
    
    # 샷 구하기
    def get_shot(self):
        result = re.findall("/show/\w+/seq/\w+/\w+_(\w+)",  self.path)
    
        if result:
            shot = result[0]
            return shot
    
        else:
            nuke.message( "shot 경로를 확인해주세요" )
    
    
    # basename 구하기
    def get_basename(self):
        result = re.findall("/show/\w+/seq/\w+/(\w+_\w+)", self.path)
    
        if result:
            shot = result[0]
            return shot
    
        else:
            nuke.message( "seq 혹은 shot 경로를 확인해주세요" )
    
    
    
    # 태스크 구하기
    def get_task(self):
        result = re.findall("/show/\w+/seq/\w+/\w+_\w+/(\w+)", self.path)
    
        if result:
            task = result[0]
            return task
    
        else:
            nuke.message( "task 경로를 확인해주세요" )
    
    
    # 한방에 구하기
    def get_all(self):
        result = re.findall("/show/(\w+)/seq/(\w+)/\w+_(\w+)/(\w+)", self.path)
    
        if result:
            project = result[0][0]
            seq = result[0][1]
            shot = result[0][2]
            task = result[0][3]
            return project, seq, shot, task
    
        else:
            nuke.message( "규칙에 맞는 경로인지 확인해주세요" )









