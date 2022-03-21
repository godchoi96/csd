# 26. 소수 찾기 - 다른 방식
# https://programmers.co.kr/learn/courses/30/lessons/12921

# 에라토스테네스의 체
# 체를 걸러내듯이 2의 배수면 2를 제외한 나머지 수를 제거하는 식으로 작성한다.
# 2 / 4, 6, 8, 10, ~
# 3 / 6, 9, 12, 15, ~
# 4 / 8, 12, 16, ~
# 이런 식으로 거르는 방식을 에라토스테네스의 체라고 한다.

def solution(n):
    temp = []
    answer = []
    for i in range(n + 1):
        temp.append(0) # 전부 0으로 된 리스트를 작성 / 후에 소수가 아닌 수에는 1로 바꿀 예정
    
    for i in range(2, n + 1): # 1은 소수가 아니기에 과감히 버리고 2부터 입력받은 n까지 반복문 실행
        if temp[i] == 0: # 0은 소수임을 나타내는 것이고 2부터 시작 / 2가 0이면 2의 배수는 모두 제거
            for j in range(i*2, n + 1, i): # 이런 식으로 2의 배수, 3의 배수를 다 제거함.
                temp[j] = 1 # 이를 1로 표현한다. 이런 식으로 제거하다 보면 11의 배수 이후 남은 수는 다 소수이다.
    for i in range(2, n + 1): # 현재 위 temp는 소수를 제외하고 다 1로 처리되어 있을 것이다.
        if temp[i] == 0: # 다시 0인 것을 확인해서 그 인덱스를 answer에 append시킨다.
            answer.append(i)

    return len(answer)

# 디버깅하는 곳입니다.
print(solution(10))
print(solution(5))