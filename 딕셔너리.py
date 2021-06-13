'''
딕셔너리(dictionary)는 key와 value를 한 쌍으로 갖는 자료형이다.
딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고
key를 통해 value를 얻는다
'''




lee = {
    "name": "이재선",
    "phone": 79371280,
    "brith": 1203,
    "age": 25
}
# key : name, phone, brith, age
# value : 이재선, 79371280, 1203, 25

'''
key	   |value
-------|------
name   |이재선
phone  |79371280
birth  |1203
age    |25
'''


print(lee["name"])      # 이재선
print(lee["phone"])     # 79371280
print(lee["brith"])     # 1203
print(lee["age"])       # 25



# lee.keys() : 딕셔너리 lee의 key만을 모아서 duct_keys 객체를 돌려준다
# lee.values() : key를 얻는것과 마찬가지로 value값들만 얻고 싶을때 사용할수 있음
# lee.items() :  key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려줌

print(lee.keys())       # dict_keys(['name', 'phone', 'brith', 'age'])
print(lee.values())     # dict_values(['이재선', 79371280, 1203, 25])
print(lee.items())      # dict_items([('name', '이재선'), ('phone', 79371280), ('brith', 1203), ('age', 25)])


lee = {
    "name": "이재선",
    "phone": 79371280,
    "brith": 1203,
    "age": 25
}


for x in lee.keys():
    print(x)

'''
name
phone
brith
age
'''

for y in lee.values():
    print(y)

'''
이재선
79371280
1203
25
'''

for x, y in lee.items():
    print(x, y)

'''
name 이재선
phone 79371280
brith 1203
age 25
'''

# key로 value얻기(get)


print(lee.get("name"))      # 이재선
print(lee.get("phone"))      # 79371280
print(lee.get("brith"))      # 1203
print(lee.get("age"))      # 25