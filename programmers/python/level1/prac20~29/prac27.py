# 27. 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    s = s.lower()

    if s.count('p') == s.count('y'):
        return True
    elif s.count('p') != s.count('y'):
        return False
    else:
        return True

# 디버깅하는 곳입니다.
print(solution("pPoooyY"))
print(solution("Pyy"))
print(solution("ooo"))