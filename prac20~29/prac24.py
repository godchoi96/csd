# 24. 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = []
    for i in range(len(s)):
        if s[i] == ' ':
            answer.append(' ')
        else:
            if s[i].islower():
                if ord(s[i]) + n < 123:
                    answer.append(chr(ord(s[i]) + n))
                else:
                    answer.append(chr(ord(s[i]) + n - 26))
            else:
                if ord(s[i]) + n < 91:
                    answer.append(chr(ord(s[i]) + n))
                else:
                    answer.append(chr(ord(s[i]) + n - 26))

    return ''.join(answer)

# 디버깅하는 곳입니다.
print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))