# 38. 최솟값 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(list1, list2):
    """
    문제에서 요구하는 것을 다음과 같다.
    [1, 4, 2] / [5, 4, 4] 두 개의 리스트가 존재한다.
    첫번째 경우는 모든 리스트의 첫번째 값을 곱해서 디폴트 값 0을 더한다. (0 + 5 = 5)
    두번째 경우는 첫번째 리스트에서 두번째 인자를 그리고 두번째 리스트는 남은 인자 중에서 가장 작은 값을 곱하고 첫번째 경우를 더한다. (5 + 16 = 21)
    세번째 경우는 첫번째 리스트에서 세번째 인자를 그리고 두번째 리스트는 남은 인자 중에서 가장 작은 값을 곱하고 두번째 경우를 더한다. (21 + 8 = 29)

    라고 생각했는데 조금 틀렸다.
    [1, 4, 2] / [5, 4, 4] 두 개의 리스트에서
    첫번째의 경우는 모든 리스트의 첫번째 값이 아닌 첫번째 리스트의 첫번째 인자와 두번째 리스트의 가장 큰 값을 곱하고 디폴트 값 0을 더한다. (0 + 5 = 5)
    """
    length = len(list1)
    answer = 0
    for i in range(length):
        answer += list1[i] * max(list2)
        del list2[list2.index(max(list2))]
    
    return answer

# 디버깅하는 곳입니다.
print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))

"""
예제 테스트 케이스는 통과했지만 나머지 테스트케이스에서 걸린다.
아마 리스트의 길이를 같게 설정해서 그런 것 같다. 문제에서는 안 나와 있기 때문.

나는 값을 제거하는 방식으로 갔는데 첫번째 리스트는 정렬, 두번째 리스트는 역정렬해서 곱하면 간단히 해결될 듯하다.
"""

def solution2(list1, list2):
    answer = 0
    list1.sort()
    list2.sort()
    list2 = list2[::-1]

    for i in range(len(list1)):
        answer += list1[i] * list2[i]

    return answer

print(solution2([1, 4, 2], [5, 4, 4]))
print(solution2([1, 2], [3, 4]))