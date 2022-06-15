# 제너레이터 표현식

def show_all(s):
    for i in s:
        print(i, end=' ')

st = [i * 2 for i in range(1, 10)]
print(show_all(st))
"""
1.
위의 식은 이터러블 객체를 출력해주는 구조이다.
이 식을 사용한 이유는 제너레이터의 표현식이 이와 비슷하기 때문이다.
"""

st = (i * 2 for i in range(1, 10))
print(type(st))
print(st)
"""
2.
기존에 우리는 리스트 컴프리헨션이라는 문법을 배웠다. 또한, 람다식에서 map, filter를 사용하지 않아도 함수처럼 표현이 가능했다.
위에서 일부러 함수로 표현했지만 실질적으로는 람다식으로도 표현이 가능하다.
리스트 컴프리헨션 문법에 대괄호가 아닌 소괄호로 한다면 이는 즉시 제너레이터의 형태로 바뀐다.
다른 예제를 통해서 조금 적응해보자.
"""

print(next(st))
"""
3.
위에서 실행했던 것이 정말 제너레이터인지 next 모듈을 실행해보자.
그러면 yield 부분이 i * 2이기 때문에 이를 반환해주고 다음 next 모듈을 실행되는 것을 기다린다.
"""

def two():
    print('two')
    return 2

g = (two() * i for i in range(1, 10))
print(next(g))
print(next(g))
"""
4.
다시 한 번 제너레이터를 정리하자면 다음과 같다.
기존에 함수식으로 표현했을 때는 return 대신 yield를 통해 함수가 제너레이터임을 파이썬에게 알려주었다.
yield를 만나면 그 다음 이터레이터의 next 모듈을 기다릴 때까지 연산을 한다.
그냥 함수와 제너레이터의 차이는 메모리의 사용 여부이다. 함수에서는 참조되는 길이를 전부 메모리 상에 올려두지만 제너레이터는 한 번에 하나씩만 연산하기에 그렇지 않다.
따라서 메모리적인 면에서 제너레이터가 훨씬 관리하기 용이하다.

제너레이터를 많이 사용할 경우라면 지금처럼 함수식으로 적어도 된다.
하지만 한 두번 연산의 목적으로 사용할 때는 람다식으로 응용해서 사용한다. 이를테면 리스트 컴프리헨션을 사용하는 것을 의미한다.
하지만 리스트 컴프리헨션과 다르게 대괄호가 아닌 소괄호를 사용하며 이에 대한 type을 확인하면 제너레이터임을 알 수 있다.

가장 아래 예제를 보면 'two' 라는 문자열을 출력하고 2를 반환해주는 함수를 range(1, 10)의 이터러블 객체로 하나씩 연산해준다.
이를 g라는 변수에 참조하고 next를 찍어보면 'two' 라는 문자열을 계속 나오고 2 * 1을 연산해서 2 그 다음 4 등이 나온다.
이것이 제너레이터에서 Lazy Evaluation의 개념이다.
"""