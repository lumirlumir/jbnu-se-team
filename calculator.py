class Calculater_operater: # 연산자 클래스 Calculater_operater로 정의.
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

    if result == 321654987: # 이스터에그 코드.
        print('Hello! This Is Team Yeonhyo Easter Egg!!')
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
                print('연산자 중복입력으로 인한 ERROR!')
                break
            operand = float(operand)
            if (int(operand) != operand): # 에러 처리(정수가 아닌 경우).
                iserror = True

            if operand == 321654987: # 이스터에그 코드.
                print('Hello! This Is Team Yeonhyo Easter Egg!!')
                break

            if operator == '+': # 덧셈.
                result = Calculater_operater.add(result, operand)
            elif operator == '-': # 뺄셈.
                result = Calculater_operater.sub(result, operand)
            elif operator == '*': # 곱셈.
                result = Calculater_operater.mul(result, operand)    

if __name__ == "__main__":
    main()