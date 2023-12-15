# operatorasm.py
import math

class Operator: # 연산자 클래스 Calculater_operater로 정의.
    def add(num1, num2): # 덧셈.
        return int(num1) + int(num2)

    def sub(num1, num2): # 뺄셈.
        return int(num1) - int(num2)

    def mul(num1, num2): # 곱셈.
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