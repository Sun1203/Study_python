# len() : 리스트 안에 몇개가 들어 있는지 호출해주는 함수!
# family[0] : 리스트 안에 첫번째 값을 호출

family = ['mother', 'father', 'gentleman', 'sexy lady']
print(len(family))      # 4
print(family[0])        # mother
print(family[1])        # father
print(family[2])        # gentleman
print(family[3])        # sexy lady


# remove() : 리스트 안에서 값을 제거하는 함수

family.remove('mother')
print(family)              # ['father', 'gentleman', 'sexy lady']


# append() : 리스트의 맨 마지막에 값을 추가하는 함수
family.append('mother')
print(family)               # ['father', 'gentleman', 'sexy lady', 'mother']


# sort()   : 리스트의 요소를 순서대로 정렬해주는 함수

lst = [1, 4, 2, 5, 7, 8]
lst.sort()
print(lst)                  # [1, 2, 4, 5, 7, 8]


# reverse(): 현재의 리스트를 그대로 거꾸로 뒤집어주는 함수
# reverse 함수는 요소들을 순서대로 정렬한 다음 다시 역순으로
# 정렬하는 것이 아닌 그저 현재의 리스트를 그대로 거꾸로 뒤집어줌

lst = [1, 4, 2, 5, 7, 8]
lst.reverse()
print(lst)                  # [8, 7, 5, 2, 4, 1]


# index()  : 리스트에 값이 있으면 값의 위치 값을 돌려주는 함수

lst = [1, 4, 2, 5, 7, 8]
print(lst.index(2))         # 2 : lst 리스트안에 2번째 값
print(lst.index(4))         # 1 : lst 리스트안에 1번째 값



# insert(a,b) : 리스트의 a번째 위치에 b를 삽입하는 함수

lst = [1, 4, 2, 5, 7, 8]
lst.insert(1, 3)           # lst 리스트에 index 1의 위치에 3의 값을 넣겠다는 의미
print(lst)                 # 1, 3, 4, 2, 5, 7, 8]


# pop()     : 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제하는 함수


lst = [1, 4, 2, 5, 7, 8]
lst.pop()                  # lst 리스트 안에 맨마지막 요소 삭제
print(lst)                 # [1, 4, 2, 5, 7]

lst.pop(1)                 # lst 리스트 안에 index 1번째에 해당하는 값을 삭제
print(lst)                 # [1, 2, 5, 7]


# count(x)   : 리스트 안에 몇개가 있는지 조사하여 그 개수를 돌려주는 함수

lst = [1, 4, 2, 5, 7, 8, 1]
print(lst.count(1))         # 2 -> lst 리스트안에 1이 두개 있다는 뜻


# extend()   :  원래의 리스트에 또다른 리스트를 더하는 함수

lst = [1, 4, 2, 5, 7, 8]
lst1 = [2, 3]

lst.extend(lst1)            # lst 리스트에 lst1 리스트를 더하는 함수
print(lst)                  # [1, 4, 2, 5, 7, 8, 2, 3]

