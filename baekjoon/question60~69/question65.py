# 65. 손익분기점
# https://www.acmicpc.net/problem/1712

# x, y, z -> x + n * y < n * z -> n을 반복시켜서 왼쪽의 부분이 성립할 때의 값을 구하면 될 듯 -> 이 방식은 타임아웃이 일어남
# 위의 공식을 다르게 생각해서 x + ny = nz일 때로 계산해보면,
# x = n(z - y)일 때 같아질 것이다. n(z - y) + 1일 때 x보다 커질 것이고 이를 이용해서 코드를 설계
# 재료와 인건비가 노트북 가격보다 비싸면 손익 분기점이 없음

default_price, change_price, notebook_price = map(int, input().split())

if change_price >= notebook_price:
    print('-1')
else:
    print(int(default_price / (notebook_price - change_price)) + 1)