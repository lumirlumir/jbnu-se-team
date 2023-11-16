# 상수
EASTER_EGG_CODE = '987654321987654321'
ERROR_MESSAGE = "ERROR!"
EASTER_EGG_MESSAGE = "Hello! This Is Team Yeonhyo Easter Egg!!"

class Operator: # 연산자 클래스 Calculater_operater로 정의.
    def add(num1, num2): # 덧셈.
        return int(num1) + int(num2)

    def sub(num1, num2): # 뺄셈.
        return int(num1) - int(num2)

    def mul(num1, num2): # 곱셈.
        return int(num1) * int(num2)
    
    # 연산자 메소드 딕셔너리
    operate = { 
        '+': add,
        '-': sub,
        '*': mul,
    }
    
def main():
    # Variables
    iserror = False # 에러 값.
    result = float(input()) # 결과 값.
    if (int(result) != result): # 에러 처리(정수가 아닌 경우).
        iserror = True

    if result == EASTER_EGG_CODE: # 이스터에그 코드.
        print(EASTER_EGG_MESSAGE)
        return
    # Calculator
    while True: # 등호나 잘못된 부호가 나올 때까지 무한 반복.
        operator = input()
        if(operator not in Operator.operate and operator != '='): # 에러 처리('+, -, *'가 아닌 경우).
            iserror = True
        
        if operator == '=': # '=' 입력.
            if(iserror):
                print(ERROR_MESSAGE)
            else:
                print(result)
            break
        else: # '+, -, *' 입력.
            operand = input()
            if(operand in Operator.operate and operator != '='): #에러 처리(연산자가 연달아 입력되었을 경우).
                print(ERROR_MESSAGE)
                break
            operand = float(operand)
            if (int(operand) != operand): # 에러 처리(정수가 아닌 경우).
                iserror = True

            if operand == EASTER_EGG_CODE: # 이스터에그 코드.
                print(EASTER_EGG_MESSAGE)
                break

            result = Operator.operate[operator](result, operand)

if __name__ == "__main__":
    main()