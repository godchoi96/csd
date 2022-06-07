# Iterable 객체와 Iterator 객체

r = [1, 2, 3, 4]
for i in r:
    print(i, end= ' ')
"""
1.
기존에 리스트가 참조되어 있는 r이라는 변수에서 값을 빼는 것은 반복문을 사용해 하나씩 출력했다.
하지만 값을 하나씩 빼서 쓰는 것은 인덱스를 지정해 따로 해결했어야 했다.
따라서 iterator의 개념을 알아보자.
"""

r = [1, 2, 3, 4]
new_r = iter(r)
print(int(next(new_r)))
print(int(next(new_r)))
print(int(next(new_r)))
print(int(next(new_r)))
"""
2.
iter 모듈을 먼저 알아보면 다음과 같다.
가장 먼저 리스트를 iter 모듈을 통해 새로운 변수 new_r에 참조시킨다.
iter 모듈은 next 모듈을 제공한다. 실행시키면 스택에서 하나씩 뽑는 것처럼 사용할 수 있다.
더 이상 객체가 존재하지 않는다면 StopIteration의 예외처리가 발생하게 된다.

iterator 객체를 얻는 이유는 무엇일까?
예를 들면 변수 r의 참조된 리스트 [1, 2, 3, 4]에서 2까지만 값을 뽑고 나중에 3 이후의 값을 참조하고 싶다면 기존 for 구문으로는 멈출 수 없다.
따라서 원할 때 정지해서 그 값을 수정하거나 할 수 있도록 하는 것이 iterator 객체의 개념이다.

여기서 iter 모듈을 통해 iterator 객체로 만들기 위해서는 리스트와 같은 객체를 사용한다.
이를 iterable 객체라고 한다.

정리하면 iterable 객체는 iter 모듈에 인자로 전달 가능한 객체를 의미하고 iterator는 iter 모듈로 인해 생성해서 반환하는 객체를 의미한다.
"""

r = [1, 2]
new_r = r.__iter__()
print(int(new_r.__next__()))
print(int(new_r.__next__()))
"""
3.
여기서 잠시 짚고 넘어갈 부분이 있다. 바로 스페셜 메소드라는 것이다.
우리가 위에서 iter() 모듈을 사용하거나 next() 모듈을 사용했는데 파이썬에서는 __iter__()와 __next()__로 인식해서 사용된다.
이런 메소드를 이제 스페셜 메소드라고 부르는데 우리는 간접적으로 iter() 등을 사용하지만 직접적으로 스페셜 메소드를 사용해도 상관은 없다.
"""

r = (1, 2, 3)
new_r = iter(r)
print(int(next(new_r)))
print(int(next(new_r)))
print(int(next(new_r)))
"""
4.
리스트는 iterable 객체임을 알 수 있었다.
iter 모듈에 또한 튜플을 넣어도 값을 하나씩 뽑아 사용할 수 있는데 튜플도 iterable 객체임을 알 수 있다.
"""

list_r = [1, 2, 3]
tupel_r = (1, 2, 3)
string_r = '123'
print(dir(list_r))
print(dir(tupel_r))
print(dir(string_r))
"""
4.
dir 모듈로 iterable한 객체인지 확인할 수 있다.
dir 모듈로 실행 시 __iter__ 라는 스페셜 메소드가 존재한다면 이는 iterable 객체라는 의미이다.
"""

print(hasattr(list_r, '__iter__'))
print(hasattr(tupel_r, '__iter__'))
print(hasattr(string_r, '__iter__'))
"""
5.
dir() 모듈을 통해서 확인하면 사용할 수 있는 모든 스페셜 메소드가 나와버려서 어지럽다.
따라서 hasattr() 이라는 모듈을 사용하면 boolean 값으로 사용할 수 있는지 없는지 알 수 있다.
"""

r = iter([1, 2, 3])
while True:
    try:
        i = next(r)
        print(i, end=' ')
    except StopIteration:
        break

"""
6.
우리가 흔히 썼던 for 구문의 iterable한 객체 반복은 위의 로직이다.
즉, for 내부 로직이 iter() 모듈을 사용하기 때문에 iterable한 객체를 사용해야 한다.
iterator는 iterable한 객체를 인자로 받아 사용하기 때문이다.
"""

r = iter([1, 2, 3])
for i in r:
    print(i, end=' ')
"""
7.
기존에 우리가 iterable한 객체인 리스트에서 값을 하나씩 빼서 출력할 때 for 구문을 사용한다고 했다.
그럼 iterable 객체가 아닌 iterator 객체를 넣어도 동작을 할까?
결과는 동작한다. 이 얘기를 정리하면 다음과 같다.
iterator 객체는 iterable한 객체 뿐만 아니라 iterator 객체 자체도 iterator에 들어갈 수 있다는 뜻이다.

최종적으로 정리하면 다음과 같다.
iterator 객체는 값을 하나씩 빼서 사용하는데 원하는 때에 멈출 수 있다.
이런 iterator의 인자로 받는 객체는 iterable한 객체만 가능하다.
하지만 iterator 객체로 되어 있어도 iterator는 통과할 수 있다. iterator는 iterator 객체이자 iterable 객체라는 의미이다.
"""