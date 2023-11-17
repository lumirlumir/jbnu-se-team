import re

from constants import EASTER_EGG_CODE, ERROR_MESSAGE
from exceptions import EasterEggException
from operatorasm import *

# 정규표현식을 이용한 정수 확인 함수
def is_integer(str):
    """Returns True if the string is an integer."""
    return re.match("[-]?\d+$", str) != None
    
def get_user_input():
    """Gets user inpus and return input as a list"""
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
    is_empty = len(user_inputs) == 0
    # 한 종류의 연산자만 입력된 경우
    is_operator_unique = not is_empty and all(element == user_inputs[1] for element in user_inputs[1::2])
    # 마지막 입력이 연산자인 경우
    is_operator_last_elem = not is_empty and user_inputs[-1] in Operator.operate
    # 모든 짝수 번째 요소들이 정수인 경우
    is_integer_even_elem = all(is_integer(element) for element in user_inputs[0::2])
    # 모든 홀수 번째 요소들이 연산자인 경우
    is_operator_odd_elem = all((element in Operator.operate) for element in user_inputs[1::2])
    
    return is_empty or is_operator_last_elem or not (is_operator_unique and is_integer_even_elem and is_operator_odd_elem)

# 사용자 입력을 이용해 계산하고 결과를 반환한다.
def calculate(user_inputs):
    """Run calculator and return the result."""
    result = None # 계산 결과
    operand = None # 피연산자
    operator = None # 연산자

    '''
    반복문 Logic
    1. 사용자 입력
    2. 입력에 따른 처리
        - 피연산자, 연산자가 번갈아 입력된다고 가정
        2.1. 피연산자가 입력된 경우
            2.1.1. 피연산자가 처음 입력된 경우
                - result에 입력된 피연산자 저장
            2.1.2. 피연산자와 연산자가 저장된 상태에서 피연산자가 입력된 경우
                - 저장된 result, operand, operator를 이용해 연산
                - 결과를 result에 저장
        2.2. 연산자가 입력된 경우
            - 입력받은 연산자를 operator 변수에 저장
        2.3. 등호가 입력된 경우
            - 결과 반환
    '''
    for user_input in user_inputs:
        # 등호가 입력된 경우 결과 출력
        if user_input == '=': 
            break
        # 정수가 입력된 경우
        elif is_integer(user_input): 
            # 사용자 입력을 피연산자 변수에 저장
            operand = int(user_input) 
            
            # 피연산자가 처음으로 입력된 경우 입력을 result에 저장
            if result == None: 
                result = operand
            else: 
                # 저장된 연산자와 피연산자를 이용해 연산 후 결과를 result에 저장
                result = Operator.operate[operator](result, operand)
            
            # 연산 후 연산자/피연산자 변수 초기화
            operator = None 
            operand = None 

        # 연산자가 입력된 경우
        elif user_input in Operator.operate: 
            # 사용자 입력을 연산자 변수에 저장
            operator = user_input 

    return result

def run_calculator():
    """Run calculator and return the result."""
    # 사용자 입력
    try:
        user_inputs = get_user_input()
    # 이스터에그 코드 입력 시 즉시 이스터에그 메시지 출력
    except EasterEggException as message:
        return message
    
    # 입력 오류 존재 시 오류 메시지 반환
    if has_error(user_inputs):
        return ERROR_MESSAGE

    # 입력 식 계산
    result = calculate(user_inputs)

    # 계산 결과 반환
    return result

def main():
    print(run_calculator())

if __name__ == "__main__":
    main()