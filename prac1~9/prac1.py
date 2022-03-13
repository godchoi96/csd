def solution(phone_number):
    answer = ''
    answer += (len(phone_number) - 4) * '*' + phone_number[-4:] # 문자열의 마지막 4번째는 나타나야함 -> 파라미터에서 -4번째부터 0번째까지 슬라이싱
                                                                # 나머지 문자열은 파라미터의 길이에서 4만큼 빼주고 이를 '*'을 곱해주면 어떤 파라미터가 와도 *로 처리
    return answer

# 디버깅하는 곳입니다.
print(solution('01071842939'))