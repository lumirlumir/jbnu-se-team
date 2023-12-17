# operatorasm.py
import math
from exceptions import InputException, OutOfRangeException
from utils import is_integer

class Operator: # 연산자 클래스 Calculater_operater로 정의.
    def add(num1, num2): # 덧셈.
        if not (is_integer(num1) and is_integer(num2)):
            raise InputException
        return int(num1) + int(num2)

    def sub(num1, num2): # 뺄셈.
        if not (is_integer(num1) and is_integer(num2)):
            raise InputException
        return int(num1) - int(num2)

    def mul(num1, num2): # 곱셈.
        if not (is_integer(num1) and is_integer(num2)):
            raise InputException
        return int(num1) * int(num2)
    
    def factorial(num):
        if not is_integer(num):
            raise InputException
        if int(num) < 0:
            raise OutOfRangeException
        return math.factorial(int(num))
    
    # 연산자 메소드 딕셔너리
    operate = { 
        '+': add,
        '-': sub,
        '*': mul,
        '!': factorial
    }