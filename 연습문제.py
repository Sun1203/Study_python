# 문제
# 파일을 다운로드할 때의 평균 속도(average rate)를 r 이라 하고,
# 다운로드하는 데 걸린 시간(time)을 t 라고 할 때, 다운로드한 파일의 용량은 r * t 로 계산할 수 있습니다.

# 다운로드 속도가 초당 800kB이고 다운로드하는 데 걸린 시간이 110초라고 할 때, 
# 다운로드한 파일의 크기는 몇 MB일까요?
# 1MB = 1000KB 로 계산

r = 800                     # 평균속도
t = 110                     # 다운로드 하는데 걸리는 시간
result = (r * t) / 1000     # 속도 * 시간 나누기 1000
print(result)               # 88MB



'''

Q1
다음 코드의 결괏값은 무엇일까?

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

'''

# 결과값 : shirt

'''
Q2
 while문을 사용해 1부터 1000까지의 자연수 중
 3의 배수의 합을 구해 보자.
'''

a = 0
b = 1
while b < 1000:
    if a % 3 == 0:
        a += b
    b = b + 1
print(a)

'''
Q3
while문을 사용하여 다음과 같이 별(*)을
 표시하는 프로그램을 작성해 보자.

*
**
***
****
*****
'''

i = 0
while True:
    i += 1              # while문 수행 시 1씩 증가
    if i > 5: break     # i 값이 5보다 크면 while문을 벗어난다.
    print ('*' * i)     # i 값 개수만큼 *를 출력한다