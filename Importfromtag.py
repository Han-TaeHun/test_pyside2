#coding:utf8

# 태그로 해당 plate 혹은 outout 가져오기
panel = nuke.Panel("ImportFromTag")

# 기본값 들어가는 변수
p = "annara" #프로젝트
t = "Tag를 입력하세요" #태그값입력하나는 
f = "org" #추후 파이널과 org를 넣을 수 있게


panel.addSingleLineInput('Project',"{}".format(p))

panel.addSingleLineInput('Tag',"{}".format(t))


panel.addEnumerationPulldown('Format', 'org output')


panel.show()

#입력값으로 받은 애들 변수
print (panel.value("Project"))
print (panel.value("Tag"))
print (panel.value("Format"))


# 태그가 걸린 샷들의 리스트를 구해야함

# plate or outprut (을)를 불러오는 함수
# org로 입력되었을때
if panel.value("Format") == "org":
    pass

# output으로 입력되었을 때
if panel.value("Format") == "output":
    pass


















