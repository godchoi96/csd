# 1. 가위바위보
# https://level.goorm.io/exam/43056/%EA%B0%80%EC%9C%84%EB%B0%94%EC%9C%84%EB%B3%B4/quiz/1

# 1: 가위, 2: 바위, 3: 보

user_input = list(map(int, input().split()))
check = list(set(user_input))

# set으로 정렬한 리스트가 1 또는 3이면 비긴 경우이기 때문에 0을 출력
if len(check) == 1 or len(check) == 3:
    print(0)
else:
    # 1이 없는 케이스 > 2와 3을 비교했을 때 3이 이기기 때문에 입력받은 리스트에서 3의 개수를 계산
    if user_input.count(1) == 0:
        print(user_input.count(3))
    # 가위 / 보 상황
    elif user_input.count(2) == 0:
        print(user_input.count(1))
    # 가위 / 바위 상황
    else:
        print(user_input.count(2))

# 1 1 1 1 1 > 1
# 2 2 2 2 2 > 2
# 3 3 3 3 3 > 3
# 1 2 3 1 2 > 1 2 3 

# 1 1 2 2 2 > 1 2 > 2
# 1 1 3 3 3 > 1 3 > 1
# 2 2 3 3 3 > 2 3 > 3