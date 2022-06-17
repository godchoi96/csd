# 37. 피보나치 수
# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    """
    그냥 피보나치 수를 만드는 것이 아니라 마지막 값을 1234567로 나눈 나머지 값을 리턴하는 것이다.
    0, 1일 때는 빈 리스트에 붙이고 2이상일 때는 1234567을 나눠서 리턴한다.
    """
    array_list = []
    new_num = 0
    for i in range(n + 1):
        if n == 0 or n == 1:
            array_list.append(n)
        else:
            new_num = solution(n - 2) + solution(n - 1)
            array_list.append(new_num % 1234567)

    return array_list[-1]

# 디버깅하는 곳입니다.
print(solution(3))
print(solution(5))
"""
재귀호출로 했더니 시간초과가 난다.
그렇다면 재귀가 아닌 그냥 단순한 반복문 로직으로 내부를 더해야된다는 소리인가 싶다. 
"""

def solution2(n):
    array_list = []
    for i in range(n + 1):
        if i == 0 or i == 1:
            array_list.append(i)
        else:
            array_list.append((array_list[i - 2] + array_list[i - 1]) % 1234567)

    return array_list[-1]

print(solution2(3))
print(solution2(5))