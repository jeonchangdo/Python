# 정의 부분
# 전역변수(함수 내에서도 사용될) 정의
a = 1
b1 = 1

def show() :
    c = a + b1 # c는 지역변수
    print('함수 내부에서 출력')
    print(a) # 전역변수
    print(b1) # 전역변수
    print(c) # 지역변수

def add() :
    global a
    a = a + 1  # a라는 전역변수 - global 처리
    c = a + b1 # b1 은 전역변수
    print('함수 내부에서 출력')
    print(a)
    print(b1)
    print(c) # 지역변수

b1 += 10 # 호출되는 지점전에 변경되면 변경된 값으로 변경된다.

show()
add()
print('함수 외부에서 출력')
print(a) # 2 - add 함수가 끝난 시점에서 a에서 1 증가
print(b1) # 11

