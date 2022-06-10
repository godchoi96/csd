# map, filter를 대신하는 리스트 컴프리헨션

r = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, r)))
print(list(filter(lambda x: x % 2, map(lambda x: x ** 2, r))))
"""
1.
기존에 학습했던 lambda, map, filter는 다음과 같다.
첫번째 출력은 map을 통해 lambda식에 하나씩 넣고 반환해준 값을 리스트로 처리하는 것이다.
두번재 출력은 그 중에서 filter를 사용해서 홀수만 출력하는 것이다.
"""

r = [1, 2, 3, 4, 5]
print([x ** 2 for x in r])
print([x ** 2 for x in r if x % 2])
"""
2.
사실 근데 위 map, filter를 대신해서 리스트 컴프리헨션을 사용하면 동일한 값을 출력해낼 수 있다.
되려 아래 방식이 좀 더 간단하다고 느낄 수도 있다.
"""

st = list(range(1, 11))
print(list(map(lambda x: x ** 2, filter(lambda x : not(x % 2), st))))
print([x ** 2 for x in st if not(x % 2)])
"""
3.
위 예제는 1부터 10까지의 숫자 중에서 짝수만 가져와서 그것을 제곱한 결과이다.
리스트 컴프리헨션을 사용하는게 좀 더 간단해보인다.

즉, map과 filter를 대신해서 리스트 컴프리헨션을 사용한다면 가독성이 더 높다.
무분별할 map, filter 함수를 사용하지말고 지나치게 코드가 길어진다면 리스트 컴프리헨션을 고민해볼 만 한 것 같다.
"""