# 반환값있는 sum 함수.py
# 사용자로부터 두수를 전달 받아서 더한 결과를 출력하는 함수

# 함수 정의 부분
def sum() :
    op = input('연산자 : ')
    n1 = int(input('숫자 1 입력 : '))
    n2 = int(input('숫자 2 입력 : '))
    return  n1 op n2

# main(호출부분)

tot = sum()
# tot = 7
print('두 수의 합 : ', tot)
print('두 수의 합 : ', sum())
