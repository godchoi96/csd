# 18. 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    # 문자열의 길이가 홀수이면 전체 문자열의 길이에서 2를 나눈 몫이 인덱스가 가운데
    # 짝수이면 전체 문자열의 길이에서 2를 나눈 몫과 그 몫에서 1을 뺀 것이 가운데 두 글자

    if len(s) % 2 != 0:
        answer = s[int(len(s) / 2)]
    else:
        answer = s[(int(len(s) / 2) - 1)] + s[(int(len(s) / 2))]
    return answer

# 디버깅하는 곳입니다.
print(solution("abcde"))
print(solution("qwer"))