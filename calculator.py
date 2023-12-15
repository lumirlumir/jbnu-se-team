import re

from constants import EASTER_EGG_CODE, ERROR_MESSAGE
from exceptions import EasterEggException
from operatorasm import *

# 정규표현식을 이용한 정수 확인 함수
def is_integer(str):
    return re.match("[-]?\d+$", str) != None
    
def get_user_input():
    user_inputs = []
    user_input = None

    # 등호가 입력될 때까지 반복
    while True:
        # 사용자 입력을 문자열 형태로 저장
        user_input = input()
        if user_input == '=':
            break
        
        # 사용자 입력을 inputs 리스트에 삽입
        user_inputs.append(user_input)
        
        # 이스터에그 코드가 입력된 경우 즉시 반환
        if user_input == EASTER_EGG_CODE: 
            raise EasterEggException
        
    return user_inputs

def has_error(user_inputs):
    # 사용자 입력이 없는 경우 ('='만 입력된 경우)
    is_empty = len(user_inputs) == 0  # 이 줄이 누락되었을 수 있습니다.

    # 마지막 입력이 연산자인 경우 (팩토리얼 제외)
    is_operator_last_elem = not is_empty and user_inputs[-1] in Operator.operate and user_inputs[-1] != '!'

    # 모든 짝수 번째 요소들이 정수인 경우
    is_integer_even_elem = all(is_integer(element) for element in user_inputs[0::2])

    # 모든 홀수 번째 요소들이 연산자인 경우 (팩토리얼 포함)
    is_operator_odd_elem = all((element in Operator.operate) for element in user_inputs[1::2])

    # 팩토리얼 연산자 '!'가 올바르게 사용되었는지 검증하는 로직
    is_factorial_used_correctly = all(
        (i == 0 or user_inputs[i-1] not in Operator.operate) and 
        (i == len(user_inputs) - 1 or user_inputs[i+1] not in Operator.operate)
        for i, element in enumerate(user_inputs) if element == '!'
    )
    
    return (is_empty or 
            is_operator_last_elem or 
            not (is_integer_even_elem and is_operator_odd_elem) or
            not is_factorial_used_correctly)
    
    # 팩토리얼 연산자 '!'가 올바르게 사용되었는지 검증하는 로직
    is_factorial_used_correctly = not any(
        element == '!' and (i == len(user_inputs) - 1 or user_inputs[i + 1] in Operator.operate)
        for i, element in enumerate(user_inputs)
    )
    
    return is_empty or is_operator_last_elem or not (is_integer_even_elem and is_operator_odd_elem) or not is_factorial_used_correctly

def calculate(user_inputs):
    result = None  # 계산 결과
    operand = None  # 피연산자
    operator = None  # 연산자

    for user_input in user_inputs:
        # 정수가 입력된 경우
        if is_integer(user_input):
            operand = int(user_input)
            if operator:
                # 연산자가 팩토리얼일 경우
                if operator == '!':
                    result = Operator.operate[operator](operand)
                    operand = None
                else:
                    result = Operator.operate[operator](result, operand)
                    operand = None
            else:
                result = operand
        # 연산자가 입력된 경우
        elif user_input in Operator.operate:
            if user_input == '!':
                if operand is not None:
                    result = Operator.operate[user_input](operand)
                    operand = None
            else:
                operator = user_input

    return result


def run_calculator():
    try:
        user_inputs = get_user_input()
    except EasterEggException as message:
        return message
    
    if has_error(user_inputs):
        return ERROR_MESSAGE

    result = calculate(user_inputs)
    return result

def main():
    print(run_calculator())

if __name__ == "__main__":
    main()
