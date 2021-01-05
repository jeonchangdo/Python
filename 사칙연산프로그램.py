# 사칙연산 프로그램.py

# 함수
# calc(op,n1,n2)
# op : 연산자
# n1,n2 : 연산할 데이터
# 사칙연산중 op에 관련된 연산한 결과를 리턴하는 함수

# main
# 사용자에게 연산자, 수1, 수2 를 입력 받습니다.
# 연산자가 사칙연산이 아니면 다시 입력하게 유도
# calc 함수를 호출해서 연산을 한 후에
# 결과를 출력
# ex) 3+2 = 5
# 0으로 나눠지지 않게 작업

# 함수 정의
def calc(op,n1,n2) :
    if op == '+' :
        return n1+n2
    elif op == '-' :
        return n1-n2
    elif op == '*' :
        return n1*n2
    else :
        return n1/n2

#main(호출)

opr_list = ['+','-','*','/']

while True :
    opr = input('연산자를 입력하세요.(+,-,*,/)')
    if opr in opr_list :
        num1 = int(input('수 1을 입력하세요.'))
        num2 = int(input('수 2을 입력하세요.'))
        if (opr=='/') & ( num2 ==0 ) :
            print('0으로 나눌 수 없습니다. 연산자부터 다시 입력하세요')
        else :
            print('%d %s %d = %d' % (num1, opr, num2, calc(opr,num1,num2)))
            break
    else :
        print('잘못된 연산자 입니다. 다시 입력하세요.')
