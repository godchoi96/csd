# dict & ordereddict

dic1 = dict(a = 1, b = 2, c = 3)
dic2 = dict(b = 2, c = 3, a = 1)
print(dic1 == dic2)
print(dic1 is dic2)
"""
1.
dic1과 dic2는 서로 참조하는 것이 다르다. 따라서 dic1 is dic2는 False가 나온다.
하지만 information은 같기에 dic1 == dic2는 True가 나온다.
여기서 알 수 있는 것은 딕셔너리는 순서가 다르게 저장되도 동일한 것으로 간주한다는 것이다.
"""

from collections import OrderedDict

dic1 = OrderedDict(a = 1, b = 2, c = 3)
dic2 = OrderedDict(b = 2, c = 3, a = 1)
print(dic1 == dic2)
print(dic1 is dic2)
"""
2.
위와 다르게 dic1 == dic2도 False가 나오게 된다.
OrderedDict 이라는 내장함수를 사용하면 딕셔너리 형태와 유사하지만 순서까지도 information으로 간주해 저장한다.
"""

dic1 = OrderedDict(a = 1, b = 2, c = 3)
dic1.move_to_end('b')
print(dic1)

dic2 = OrderedDict(a = 1, b = 2, c = 3)
dic2.move_to_end('b', last = False)
print(dic2)
"""
3.
또, OrderedDict 내장함수는 key 값을 통해 순서를 조정할 수도 있다.
move_to_end() 라는 메소드가 존재해서 이 안에 파라미터로 key 값을 넣는다면 해당 key와 value 값이 가장 뒤로 밀려난다.
가장 앞으로 보내고 싶다면 last = False 라는 함수 인자를 추가한다.

즉, OrderedDict을 사용하는 이유는 기존에 딕셔너리는 순서까지 저장하지는 않았다.
하지만 OrderedDict을 사용함으로써 순서도 저장하고 키 값을 자유자재로 위치를 이동시킬 수 있게 되었다. 그래서 순서가 보장되어야 할 때, 많이 사용한다.
"""