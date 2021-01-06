# 지역변수_전역변수.py

# 지역변수(local variable)
# -함수 내부에서 정의된 변수
# -함수안에서만 사용 가능
# -함수 호출 시 생성
# -함수가 종료되면 소멸되어 더이상 사용 불가

def show() :
    a=1 # 지역변수(show() 안에서만 사용) - 변수생성
    print(a) # 코드 실행 후 변수가 사라짐

show()
# print(a) # 함수 외부이기 때문에 사용 불가

# 함수의 매개변수도 지역변수
# 외부로부터 값을 전달 받아서
# 함수 내부에서만 사용하는 지역변수

def show2(b) : # 매개변수 a가 1 받음
    b = b+1 # 함수 내에서 지역변수 1 증가
    print(b) # 2 출력 - b 변수는 종료

show2(10)
# print(b)

# 전역변수(global variable)
# - 함수 외부에서 정의된 변수
# - 프로그램 내 모든 곳에서 사용 가능
# - 함수 내에서 전역변수 값을 변경하려면 global 키워드 사용

a = 1 # 함수 밖에서 정의 된 전역변수 a
def show() :
    c = a + b1 # c는 지역변수
    print(a) # 전역변수
    print(b1) # 전역변수
    print(c) # 지역변수

def add() :
    print(a)
    print(b1)

b1 = 2 # 함수 밖에서 정의된 전역변수 (함수 호출 후에 정의하면 error)
show() # show 함수의 동작이 시작되는 지점
        # show 함수의 동작이 종료
add()
print(a)
print(b1)
