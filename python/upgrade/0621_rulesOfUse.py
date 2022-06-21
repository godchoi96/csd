# 함수 호출과 매개변수 선언에 있어서 *와 **의 사용 규칙

n1, n2, *others = [1, 2, 3, 4, 5]
print(others)
"""
1.
*에 대해서 정리하자면, 다음과 같다. *의 정확한 용어는 Asterisk라고 한다.
기존에 사용할 때는 언패킹 용도로 많이 사용하는데 함수 호출에서만 패킹이 되어진다고 했었다.
현재 위의 예제는 언패킹이 되어 n1, n2에 각 1, 2이라는 객체가 참조되고 나머지 3, 4, 5 객체가 묶인 것을 확인할 수 있다.
"""

def who(a, b, c):
    print(a, b, c, sep=', ')

who(*[1, 2, 3])
who(*(0.1, 0.2, 0.3))
who(*('abc'))
"""
2.
who 함수는 리턴 값이 없고 출력만 해주는 함수이다.
who 함수에 *[1, 2, 3]을 넣으면 언패킹되어 1, 2, 3 객체가 각 who 함수 내의 print 변수로 들어가게 된다.
리스트, 튜플, 문자열 모두 iterable 객체이기 때문에 가능한 일이다.
"""

def who(a, b, c):
    print(a, b, c, sep=', ')

dic = dict(a = 1, b = 2, c = 3)
who(*dic)
who(**dic)
"""
3.
딕셔너리 또한 iterable 객체이기 때문에 가능하다.
딕셔너리의 경우에는 *, **의 형태가 있는데 이는 다음과 같다.
*dic을 했을 경우에는 key 값이 언패킹되어 인자가 전달되고 **dic을 했을 경우에는 value 값이 언패킹되어 인자가 전달된다.
"""

def who(a, b, c):
    print(a, b, c, sep=', ')

dic = dict(a = 1, b = 2, c = 3)
who(*(dic.items()))
"""
4.
지난번에 학습했던 딕셔너리 루핑을 통해서 확인해보자.
key, value의 형태로 만들어주는 items() 내장함수를 통해 언패킹하여 인자를 전달한다.
확인해보면 튜플 형식으로 패킹되어 출력되고 있음을 알 수 있다.
"""

def func(*args):
    print(args)

func()
func(1)
func(1, 2)
"""
5.
위에서는 함수 호출에서 *를 어떻게 사용하는지 확인했는데 이번엔 인자 생성에서는 어떻게 쓰이는지 다시 정리하겠다.
*args 라고 인자를 선언하면 이는 튜플로 인자를 받아 저장한다.
출력해보면 (), (1, ), (1, 2)가 나오는데 튜플로 나오는 것을 알 수 있다.
"""

def func2(**args):
    print(args)

func2(a = 1)
func2(a = 1, b = 2)
"""
6.
**args를 함수에서 인자로 선언했을 때는 어떨까?
이는 딕셔너리 형태로 저장된다.
마찬가지로 출력해보면 {'a': 1}, {'a': 1, 'b': 2}가 나온다.
"""

def func3(*args, **kwargs):
    print(args, kwargs)

func3(1, 2, a = 1, b = 2)
"""
7.
내가 자주 보았던 함수 형태이다.
args, kwargs는 단지 함수에서 실행되는 인자명이었고 *, **의 의미를 알게 되었다.

정리하면 함수 인자 선언에서의 *, **의 역할은 다음과 같다.
*은 튜플 형태로 패킹, **은 딕셔너리 형태로 패킹이 된다.
함수 호출에서의 *, **의 역할은 다음과 같다.
iterable 객체 중 딕셔너리를 제외하고 *은 모두 언패킹되어 하나씩 인자를 보내준다.
딕셔너리에서는 *은 key 값을 언패킹, **은 value 값을 언패킹해서 하나씩 인자를 보내준다.
"""