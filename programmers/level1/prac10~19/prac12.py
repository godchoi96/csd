# 12. 2021 카카오 채용연계형 인턴십 - 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    info = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

    for key, value in info.items():
        s = s.replace(value, str(key))
    s = int(s)
    return s

# 디버깅하는 곳입니다.
print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))