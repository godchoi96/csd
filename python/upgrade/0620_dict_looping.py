# dict의 루핑 기술과 컴프리헨션

intro = {"name": "최승대", "age": 27, "born": "Incheon"}
for key in intro.keys():
    print(key)

for value in intro.values():
    print(value)

for kvalue in intro.items():
    print(kvalue)
"""
1.
루핑 기술이라고 해서 사실 무슨 의미인지 잘 몰랐지만 예제를 보고 쉽게 알았다.
딕셔너리 내부에 존재하는 keys, values, items 내장함수를 사용해서 다음과 같이 값을 만들 수 있다.
items() 내장함수의 경우에는 튜플 형태로 key, value 형태를 띈다.

이렇게 새 메소드를 통해서 받은 객체를 뷰 객체라고 한다.
뷰 객체는 iterable한 특성으로 인해 for 구문을 사용하면 값을 하나씩 참조할 수 있게 된다.
"""

dict1 = dict(a = 1, b = 2, c = 3)
dict2 = {k : v*2 for k, v in dict1.items()}
dict3 = {k : v*2 for k, v in dict2.items()}
print(dict1)
print(dict2)
print(dict3)
"""
2.
딕셔너리 컴프리헨션에 대해서 알아보자.
dict1은 일반적인 딕셔너리 생성 방식이다.
dict2는 dict1 딕셔너리의 items() 내장함수를 통해 key, value를 가져오는데 이를 컴프리헨션 방식으로 value에 2를 곱하게 만들었다.
dict3는 dict2 만드는 방식과 유사하지만 dict1이 아닌 dict2의 items() 내장함수를 사용했다.
"""

dict = dict(a = 1, b = 2, c = 3, d = 4)
dict2 = {k : v for k, v in dict.items() if v % 2}
print(dict2)
"""
3.
리스트 컴프리헨션 때 했던 것처럼 조건문을 넣어도 똑같이 동작한다.
"""

k_list = ['a', 'b', 'c', 'd']
v_list = [1, 2, 3, 4]
dict = {k: v for k, v in zip(k_list, v_list)}
print(dict)
"""
4.
지난 번에 했던 zip 모듈을 통해서 주어진 리스트를 튜플로 병합해서 만든다. ('a', 1), ... 이런 식으로 만들어졌을 것이다.
튜플 또한 iterable한 객체이기 때문에 for 구문을 통해 값을 하나씩 빼올 수 있다. 이것을 딕셔너리 컴프리헨션으로 딕셔너리로 만든다.
"""
