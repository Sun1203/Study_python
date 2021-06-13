'''
class : 객체(데이터들을 하나의 단위로 관리하는 실제 사용 가능한 메모리상의 역역)를 사용 가능하게 해주는 설계도
        (붕어빵과 비교시 붕어빵 = 객체, 붕어빵들 = class)

'''

class person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("이재선", 25)
print(p1.name, p1.age)          # 이재선 25

p2 = person("김남주", 25)
print(p2.name, p2.age)          # 김남주 25

print(p1.name, p2.name)         # 이재선 김남주



class encore:

    def __init__(self, sub, teacher):
        self.sub = sub
        self.teacher = teacher

e1 = encore("빅데이터", "이재선")
e2 = encore("웹개발자", "박서령")
e3 = encore("ai인공지능", "송이")

print(e1.sub, e2.teacher)                 # 빅데이터 박서령
print(e3.sub, e2.teacher, e1.teacher)     #  ai인공지능 박서령 이재선


# 학생들 정보를 관리하는 프로그램
# 데이터 = 학번(no)/이름(name)/학년(grade)...
# 메소드 : 데이터를 관리할 수 있는 기능의 메소드들도 주로 포함해서 개발


class student:

    def __init__(self, no, name, grade):
        self.no = no
        self.name = name
        self.grade = grade


    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name



s1 = student("14학번", "이재선", "4학년")
s2 = student("15학번", "박서령", "3학년")
s3 = student("16학번", "정진혁", "2학년")
s4 = student("17학번", "이방원", "1학년")

print(s1.name, s2.name, s3.name, s4.name)       # 이재선 박서령 정진혁 이방원
print(s1.name, s2.no, s3.no, s4.no)             # 이재선 15학번 16학번 17학번

print(s1.getName)   # <bound method student.getName of <__main__.student object at 0x0000016C0603BC10>>

s1.setName("유재석")
print(s1.name)




class restaurant:
    restaurant_name = "아웃백!"

    def __init__(self, main):
        self.main = main


r1 = restaurant("스테이크!!빵!!")
print(r1.restaurant_name, "의 메인 메뉴는는는~~~~두근두근???",r1.main)
# 아웃백! 의 메인 메뉴는는는~~~~두근두근??? 스테이크!!빵!!


# 사용자 정의 클래스 + 메소드, 변수 -> class 변수(필요성)

class UserClass:

    #생성자
    def __init__(self, data):
        self.instanceVar = data
        print("생성자")

    
    def getInstanceVar(self):
        return self.instanceVar

def getInstanceVar2():
    return "클래스 외부에 구현된 별도의 함수"

d = UserClass("생성자로 유입되는 데이터들")
print(d.getInstanceVar())