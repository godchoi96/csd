# 3. 공간복잡도 알아보기 - 최빈값 찾기 알고리즘

# 첫번째 방법
def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    max_num = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        cnt = 0
        for char in string:
            if char == alphabet:
                cnt += 1
        
        if cnt > max_num:
            max_num = cnt
            max_alphabet = alphabet

    return max_alphabet

print(find_max_occurred_alphabet("Hello my name is sparta"))

# 두번째 방법
def find_max_occurred_alphabet2(string):
    temp_array = [0] * 26
    
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        temp_array[arr_index] += 1

    max_num = 0
    max_alphabet_index = 0

    for index in range(len(temp_array)):
        num = temp_array[index]
        if num > max_num:
            max_num = num
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))

print(find_max_occurred_alphabet2("Hello my name is sparta"))