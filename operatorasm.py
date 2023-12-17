# operatorasm.py
import math
from exceptions import NotIntegerException
from utils import is_integer

class Operator: # 연산자 클래스 Calculater_operater로 정의.
    def add(num1, num2): # 덧셈.
        if not (is_integer(num1) and is_integer(num2)):
            raise NotIntegerException
        return int(num1) + int(num2)

    def sub(num1, num2): # 뺄셈.
        if not (is_integer(num1) and is_integer(num2)):
            raise NotIntegerException
        return int(num1) - int(num2)

    def mul(num1, num2): # 곱셈.
        if not (is_integer(num1) and is_integer(num2)):
            raise NotIntegerException
        return int(num1) * int(num2)
    
    @staticmethod
    def factorial(num):
        if num < 0:
            raise ValueError("팩토리얼은 음수에 대해 정의할 수 없음")
        return math.factorial(num)
    
    # 연산자 메소드 딕셔너리
    operate = { 
        '+': add,
        '-': sub,
        '*': mul,
        '!': factorial
    }