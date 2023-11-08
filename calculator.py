class op: # 연산자 클래스
    def add(num1, num2): # 덧셈.
        return int(num1) + int(num2)

    def sub(num1, num2): # 뺄셈.
        return int(num1) - int(num2)

    def mul(num1, num2): # 곱셈.
        return int(num1) * int(num2)
    
def main():
    # Variables
    iserror = False # 에러 값.
    result = float(input()) # 결과 값.
    if (int(result) != result): # 에러 처리(정수가 아닌 경우).
        iserror = True

    if result == 321654987:
        print('Hello!')
        return
    # Calculator
    while True: # 등호나 잘못된 부호가 나올 때까지 무한 반복.
        operator = input()
        if(operator not in ['=', '+', '-', '*']): # 에러 처리('+, -, *'가 아닌 경우).
            iserror = True
        
        if operator == '=': # '=' 입력.
            if(iserror):
                print('ERROR!')
            else:
                print(result)
            break
        else: # '+, -, *' 입력.
            operand = input()
            if(operand in ['=', '+', '-', '*']): #에러 처리(연산자가 연달아 입력되었을 경우).
                print('ERROR!')
                break
            operand = float(operand)
            if (int(operand) != operand): # 에러 처리(정수가 아닌 경우).
                iserror = True

            if operand == 321654987:
                print('Hello!')
                break

            if operator == '+': # 덧셈.
                result = op.add(result, operand)
            elif operator == '-': # 뺄셈.
                result = op.sub(result, operand)
            elif operator == '*': # 곱셈.
                result = op.mul(result, operand)    

if __name__ == "__main__":
    main()