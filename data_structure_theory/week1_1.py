# 1. 최빈값 구하기
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for i in range(len(string)):
        if string[i].isalpha():
            alphabet_occurrence_array[ord(string[i]) - ord('a')] += 1
        
        answer = chr(alphabet_occurrence_array.index(max(alphabet_occurrence_array)) + ord('a'))
        # 0 + 97 = 97 / 1 + 97 = 98
        # 인덱스 번호에서 97을 더하면 해당하는 인덱스 번호의 아스키 코드가 나온다. (현재 위 리스트에서는 빈도수 별로 저장되어 있기 때문)

    return answer

print(find_alphabet_occurrence_array("hello my name is sparta"))