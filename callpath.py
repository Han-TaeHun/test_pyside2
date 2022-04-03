#coding:utf8
import re

# 저장경로 가져오기
nk_path = nuke.root().name().replace("C:", "")



# 프로젝트 구하기
def get_project():
    
    
        
    result = re.findall("/show/(\w+)", nk_path)

    if result:
        project = result[0]
        return project

    else:
        nuke.message( "project 경로를 확인해주세요" )
        
get_project()

# 시퀀스 구하기
def get_seq():
    result = re.findall("/show/\w+/seq/(\w+)", nk_path)

    if result:
        seq = result[0]
        return seq

    else:
        nuke.message( "seq 경로를 확인해주세요" )

# 샷 구하기
def get_shot():
    result = re.findall("/show/\w+/seq/\w+/\w+_(\w+)", nk_path)

    if result:
        shot = result[0]
        return shot

    else:
        nuke.message( "shot 경로를 확인해주세요" )


# basename 구하기
def get_basename():
    result = re.findall("/show/\w+/seq/\w+/(\w+_\w+)", nk_path)

    if result:
        shot = result[0]
        return shot

    else:
        nuke.message( "seq 혹은 shot 경로를 확인해주세요" )



# 태스크 구하기
def get_task():
    result = re.findall("/show/\w+/seq/\w+/\w+_\w+/(\w+)", nk_path)

    if result:
        task = result[0]
        return task

    else:
        nuke.message( "task 경로를 확인해주세요" )


# 한방에 구하기
def get_all():
    result = re.findall("/show/(\w+)/seq/(\w+)/\w+_(\w+)/(\w+)", nk_path)

    if result:
        project = result[0][0]
        seq = result[0][1]
        shot = result[0][2]
        task = result[0][3]
        return project, seq, shot, task

    else:
        nuke.message( "필수경로인지 확인해주세요" )











