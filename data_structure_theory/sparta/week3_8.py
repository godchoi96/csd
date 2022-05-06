# 문제 풀어보기
# 2. 올바른 괄호
def my_answer_correct_parent(string):
    first_count = string.count('(')
    second_count = string.count(')')

    if string[0] == ')':
        return False
    else:
        if first_count == second_count:
            return True
        else:
            return False

def corrct_paren(string):
    stack = []

    for i in range(len(string)):
        if string[i] == '(':
            stack.append(string[i])
        elif string[i] == ')':
            if len(string) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True

print(corrct_paren('(())'))
print(corrct_paren('!!!!!!!!()('))

# (())) 이런 식이면 제대로 닫혀있지 않아 False, (())은 True이다.
# 일단 가장 먼저 떠오른 것은 (의 개수와 )의 개수가 다르면 제대로 닫혀있지 않다는 뜻이고 (으로 시작하지 않아도 제대로 열려있지 않다는 뜻이다.
# 문자열도 리스트이기 때문에 잘 닫혀있는지 확인하면 될 것 같다.

