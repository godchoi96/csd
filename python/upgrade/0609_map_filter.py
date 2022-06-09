# map과 filter

def square(n):
    return n ** 2

r1 = [1, 2, 3]
r2 = [square(r1[0]), square(r1[1]), square(r1[2])]
print(r2)
"""
1.
r1 이라는 리스트를 참조하는 변수가 있다. 이 안의 인자들을 모두 제곱해서 출력해주려면 어떻게 해야할까?
반복문을 통해서 인자를 하나씩 꺼내 연산을 실행하거나 위처럼 직접적으로 대입해주는 방법이 있을 것이다.
하지만 map이라는 iterator 객체를 사용하면 훨씬 더 간단히 사용할 수 있다.
"""

print(list(map(square, r1)))

def sum_num(n, m):
    return n + m
r1 = [1, 2, 3]
r2 = [3, 4, 5]
print(list(map(sum_num, r1, r2)))
"""
2.
위 아래 모두 같은 출력값을 확인할 수 있다.
map 내부의 파라미터를 보자면 함수, 그리고 인자임을 알 수 있는데 여기서 인자에는 iterable한 객체인 리스트나, 튜플 등이 들어가야 한다.
부가적으로 파라미터를 두 개 입력받아야 한다면, map 내부에 인자를 두 개 넣으면 된다.
"""

r1 = [1, 2, 3]
new_r1 = list(map(lambda x: x ** 2, r1))
print(new_r1)

r1 = [1, 2, 3]
r2 = [3, 4, 5]
print(list(map(lambda x, y: x + y, r1, r2)))
"""
3.
기존에 우리가 작성해왔던 함수를 보면 모두 반환 목적의 함수이다.
따라서 굳이 def를 사용하지 않고 lambda 식을 사용하면 더 간단한 코드가 완성된다.
"""

def is_odd(n):
    return n % 2

st = [1, 2, 3, 4, 5]
new_st = list(filter(is_odd, st))
print(new_st)
"""
4.
filter 함수는 map과 상당히 유사한 모습을 띈다.
다만, filter 함수의 목적은 값을 걸러주는 역할을 한다. 
위의 예제를 보면 is_odd() 함수가 있는데 홀수일 때 1을 리턴해서 True를 반환해주고 짝수일 때는 False를 반환시킨다.
출력해보면 홀수만 나오는 것을 알 수 있고 filter가 False일 때는 반환해주지 않는 것을 알 수 있다.
"""

st = [1, 2, 3, 4, 5]
new_st = list(filter(lambda n: n % 2, st))
print(new_st)
"""
5.
이를 람다식을 사용해도 같은 값을 뽑아낼 수 있다. 어쨌거나 함수 객체는 반환이 목적이기 때문이다.
그렇다면 하나 예제를 만들어보자. 1부터 10까지의 제곱 수 중 3의 배수만 출력하는 것을 만들어내보자.
"""

array = list(range(1, 11))
answer = list(filter(lambda x: not(x % 3), list(map(lambda x: x ** 2, array))))
print(answer)
"""
6.
map을 사용해서 제곱 리스트를 만들어냈다.
그리고 그 리스트를 또 3의 배수를 만들어주는 람다식을 만들어내서 이를 filter 처리했다.
그렇게 뽑아내면 제곱 수 중에서 3의 배수만인 리스트가 생성이 된다.
"""