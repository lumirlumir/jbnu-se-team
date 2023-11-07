# 더하기 계산 함수
def add(number_list):
    # 숫자 문자열의 리스트를 정수 리스트로 변환하고 합을 반환
    add_result = sum(map(int, number_list))
    return add_result

# 입력을 + 기준으로 분리하여 정수 리스트로 변환
def set_numbers(numbers):
    split_numbers = numbers.split('+')
    return split_numbers

# 사용자가 지금까지 입력한 input 모음
accumulated_input = ""

while True:
    # 현재 입력
    now_input = input()

    # "=" 이 입력될 때
    if now_input == '=':
        # 사용자가 지금까지 입력한 input 들을 "+"를 기준으로 구분
        add_numbers = set_numbers(accumulated_input)
        
        # add함수를 호출해 더한 결과 반환
        add_result = add(add_numbers)

        # 결과 출력
        print(add_result) 

        break
    # 현재 입력이 정수이거나 + 일 경우
    elif now_input.isdigit() or now_input == '+':
        accumulated_input += now_input

    # 예외
    else:
        print("예외처리")
