# 제너레이터 함수

def gen_num():
    print('first_number')
    yield 1
    print('second_number')
    yield 2
    print('third_number')
    yield 3

print(type(gen_num()))

def gen_num():
    for i in [1, 2, 3]:
        yield i

g = gen_num()
print(next(g))
print(next(g))
print(next(g))
"""
1.
iterator라는 개념에 대해서 배웠다.
지금 하게 될 generator는 iterator의 일부분이다.
함수부터 구현하는 것을 보자면 return하지 않고 yield하는 것을 알 수 있다. 이를 통해 type 찍어보면 generator로 변경되어있다.
yield를 만나면 다음 yield 전까지 지속해서 연산을 수행하고 더 이상 yield할 것이 없어지면 StopIteration 예외처리를 발생시킨다.
"""

import time

def return_abc():
    alphabets = []
    for ch in "ABC":
        time.sleep(1)
        alphabets.append(ch)
    return alphabets

def yield_abc():
    for ch in "ABC":
        time.sleep(1)
        yield ch

for ch in return_abc():
    print(ch)

for ch in yield_abc():
    print(ch)

"""
2.
조금 더 세부적으로 알아보자.
똑같은 출력을 의도하지만 return_abc 함수는 return, yield_abc 함수는 yield를 사용했다.
일반적인 함수의 경우에는 3초가 걸리고 A B C 출력이 나오지만 제너레이터의 경우에는 1초마다 각 출력값이 하나씩 나온다.
즉, 기본적으로 함수는 메모리 상에서 한 번에 올려두고 이 값을 한 번에 출력해주지만 제너레이터의 경우에는 필요할 때마다 꺼내 쓰기에 메모리 소요가 적다.
"""

def yield_from_abc():
    test = "ABC"
    yield from test

for ch in yield_from_abc():
    time.sleep(1)
    print(ch)

"""
3.
파이썬 3.3 이상부터는 yield from이라는 모듈을 제공한다.
이는 for 구문 대신에 사용하는 것으로 조금 더 간단하게 제너레이터를 사용할 수 있다.

정리하면, 제너레이터는 이터레이터 객체 중 한 부분이다.
함수와 다르게 return이 아닌 yield를 통해 반환하는데 yield를 사용함과 동시에 이는 제너레이터 함수가 된다.
함수의 경우에는 반환된 값을 한 번에 메모리에 올려두기 때문에 많은 양을 차지하지만, 제너레이터의 경우에는 필요할 때마다 생성하기 때문에 많은 양을 차지하지 않는다.
제너레이터에서는 3.3 이상 버젼부터 yield from을 통해 for 구문 대신에 사용하기도 한다.
우리가 그 전까지 했던 map, filter 함수도 모두 이터레이터지만 사실 제너레이터이기도 하다.
"""