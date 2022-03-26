# 30. 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]

    strings.sort()

    for i in range(len(strings)):
        answer.append(strings[i][1:])

    return answer

# 디버깅하는 곳입니다.
print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))