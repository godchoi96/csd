# 20. 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = []
    s = s.split(" ") # " "을 하지 않으면 모든 공백을 스플릿하게 됨. " "은 스페이스바 공백만 스플릿
    
    for i in range(len(s)):
        result = ''
        for j in range(len(s[i])):
            if j % 2 == 0:
                result += s[i][j].upper()
            else:
                result += s[i][j].lower()

        answer.append(result)

    return ' '.join(answer)

# 디버깅하는 곳입니다.
print(solution('try hello world'))