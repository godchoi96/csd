# 25. 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = False

    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            answer = True

    return answer

# 디버깅하는 곳입니다.
print(solution("a234"))
print(solution("1234"))