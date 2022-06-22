# dict & defaultdict

dic = {'red': 1, 'blue': 2, 'green': 3}
dic['red'] = 1
print(dic)
"""
1.
딕셔너리에 대해 다시 정리하면 다음과 같다.
기존에 key 값이 존재하는데 새로운 값을 참조하라하면 그 값을 참조하게 된다.
"""

dic = {'blue': 2, 'green': 3}
dic['red'] = 1
print(dic)
"""
2.
이번엔 key 값이 존재하지 않는데 값을 참조하라하면 어떻게 될까?
새로운 key 값으로 객체를 참조해 딕셔너리 안으로 들어가 패킹된다.
"""

string = 'banana'
string_dic = {}

for alpha in string:
    if alpha in string_dic:
        string_dic[alpha] += 1
    else:
        string_dic[alpha] = 1

print(string_dic)
"""
3.
1번과 2번을 혼합해서 사용하면 다음과 같다.
딕셔너리에 키 값이 있으면 value를 1 증가시키고 없으면 1을 만들어내는 로직인 셈이다.
"""

string = 'banana'
string_dic = {}

for alpha in string:
    string_dic[alpha] = string_dic.setdefault(alpha, 0) + 1

print(string_dic)
"""
4.
위에서 딕셔너리에 key 값이 존재하면 참조한 객체에 1을 더해주고 아니면 1을 참조시켰다.
하지만 이는 조건문을 사용해서 작성했었다.
이를 보조해주는 것이 setdefault() 라고 하는 내장함수가 있다.
string_dic[alpha]으로 key 값을 불러와서 해당 키 값에 0을 참조시키고 1을 더해준다.
굳이 조건문을 사용하지 않아도 조건문을 사용한 것처럼 key 값에 따른 value 값을 조정해준다.
"""

from collections import defaultdict

string = 'banana'
string_dic = defaultdict(int)
print(string_dic)
for alpha in string:
    string_dic[alpha] += 1

print(string_dic)
"""
5.
defaultdict 이라는 내장함수를 사용해보자.
defaultdict(int)를 잠시 보면 아무런 값이 없는 것을 확인할 수 있다. 여기서 int로 정수형을 반환해주는데 아무 값이 없으면 0을 반환한다.
즉, 값이 없을 땐 0을 반환하고 1을 더해주고 값이 있으면 그 해당하는 키 값에 1을 더해주는 것이다.
"""

def zero():
    return 0

string_dic = defaultdict(zero)
print(string_dic['a'])
"""
6.
직접 0을 반환해주는 함수를 만들어도 다음과 같다.
키 값을 넣어도 해당 값이 없기 때문에 0을 반환해서 0이 나오게 된다. 여기서 zero 함수는 0을 반환하는 것이 목적이기 때문에 람다를 사용할 수도 있다.
"""

string_dic = defaultdict(lambda: 0)
print(string_dic['a'])
"""
7.
람다를 사용해서 0을 반환해 defaultdict 함수로 확인해보았다.

정리하면, 일반적으로 딕셔너리에서 키 값에 대한 값이 존재하지 않으면 에러가 발생한다.
따라서, if-else 문을 사용해서 값이 없으면 값을 만들어주고 값이 있으면 해당 키 값에 더해주는 방식으로 만들 수 있다.
하지만 이런 방식말고도 setdefault() 내장함수를 사용한다거나 defaultdict() 내장함수를 사용해서도 만들 수 있다.
if-else문의 심화과정이라 생각하지 말고 또 다른 방법이라고 생각하면 될 것 같다.
"""