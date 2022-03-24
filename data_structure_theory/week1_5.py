# 6. 반복되지 않는 문자
def find_not_repeating_first_character(string):
    answer = []
    for index in range(len(string)):
        if not string[index].isalpha():
            continue
        if string[index] in answer:
            answer.remove(string[index])
        else:
            answer.append(string[index])
    if answer == []:
        answer.append(string[0])

    return ''.join(answer)[0]
    
print(find_not_repeating_first_character("abadabac"))
print(find_not_repeating_first_character("aabbcddd"))
print(find_not_repeating_first_character("aaaaaaaa"))
print(find_not_repeating_first_character("aab  bcddd"))