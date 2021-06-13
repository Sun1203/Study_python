def add(a, b):
    return a+b, a-b

print(add(3,4))         # (7, -1)


def lee(a, b):
    return a + b
    return a * b

print(lee(3, 4))       #  7 -> a * b는 실행안댐


def say(name):
    if name == "이재선":
        return
    print("나의 이름은 {0} 입니다" .format(name))    #  나의 이름은 재선 입니다

print(say("재선"))      # NONE


# 매개변수에 초깃값 미리 설정하기

def say_myself(name, old, man=True):
    print("나의 이름은 {} 입니다." .format(name))
    print("나이는 {}살입니다" .format(old))

    if man:
        print("남자입니다")
    
    else:
        print("여자입니다")
    

print(say_myself("이재선", 25, True))
print("----" * 5)
print(say_myself("김남주", 22, False))


'''
나의 이름은 이재선 입니다.
나이는 25살입니다
남자입니다
None
--------------------
나의 이름은 김남주 입니다.
나이는 22살입니다
여자입니다
None
'''


# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까 ?
# def 함수이름(*args)

def add_many(*args):

    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,3,4,5,6,7))          # 28
print(add_many(1,2,3,4,5,6,7,8,9,10))   # 55


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    
    return result

print(add_mul("add", 1,4,5,6,2,3,4,5))     # add를 한 값 : 30
print(add_mul('mul', 1,4,2,3,4,5,2,1,2))   # mul을 한 값 : 1920


'''
 **kwargs : **kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수
            kwargs는 딕셔너리가 되고 모든 key=value 형태의 결과값이 그
            딕셔러니에 저장된다!
'''
def print_kwargs(**lee):
    print(lee)

print_kwargs(a=1)      #  {'a': 1}
print_kwargs(name="이재선", age = 25, study = "encore")      #  {'name': '이재선', 'age': 25, 'study': 'encore'}
print_kwargs(name = "김남주")      #  {'name': '김남주'}
print_kwargs(사는곳 = "순천")      #  {'사는곳': '순천'}