# 더하기
def add(num1, num2):
    return num1 + num2

# 빼기
def sub(num1, num2):
    return num1 - num2

# 숫자 계산용
result = 0
user_input = input()

try:
    # 숫자 입력
    num = int(user_input)
    # 양수가 아닐 경우
    if num <= 0:
        print("error")
        exit()
    result = num
    # 정수가 아닐 경우
except ValueError:
    print("error")
    exit()

# 등호나 잘못된 부호가 나올 때까지 반복
while True:
    # 부호 입력
    operator = input()
    # 등호 입력 시
    if operator == '=':
        break
    
    # 더하기나 빼기가 아닐 시
    if operator not in ['+', '-']:
        print("error")
        break

    # 숫자 입력
    num_input = input()
    try:
        num = int(num_input)
        # 양수가 아닐 경우
        if num <= 0:
            print("error")
            break
    # 정수가 아닐 경우
    except ValueError:
        print("error")
        break

    # 더할 때
    if operator == '+':
        result = add(result, num)
    # 뺄 때
    elif operator == '-':
        result = sub(result, num)

# 결과 출력
print(result)
