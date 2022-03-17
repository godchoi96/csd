# 1. 사칙연산
def calculate(A, B):
    sum = 0
    sub = 0
    mul = 0
    div = 0
    res = 0

    sum = A + B
    sub = A - B
    mul = A * B
    div = A / B
    res = A % B
    
    return sum, sub, mul, div, res

# 2. 곱셈
def multiplication(A, B):
    first_result = 0
    second_result = 0
    third_result = 0
    fourth_result = 0
    B = str(B)

    first_result = A * int(str(B)[0])
    second_result = A * int(str(B)[1])
    third_result = A * int(str(B)[2])
    fourth_result = A * int(B)

    return first_result, second_result, third_result, fourth_result
    
# 3. 알람 시계
def alarm(H, M):
    if M < 45:
        if H == 0:
            H = 23
            M += 60
        else:
            H -= 1
            M += 60
    return H, M-45

print(alarm(10, 10))
print(alarm(0, 30))
print(alarm(23, 40))