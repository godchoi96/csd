# 1. 최빈값 구하기
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for i in range(len(string)):
        if string[i].isalpha():
            alphabet_occurrence_array[ord(string[i]) - ord('a')] += 1
        
        answer = chr(alphabet_occurrence_array.index(max(alphabet_occurrence_array)) + ord('a'))

    return answer

print(find_alphabet_occurrence_array("hello my name is sparta"))