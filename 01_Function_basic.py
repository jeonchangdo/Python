# 함수기초개념 .py

# 함수(function)
# 특정 작업을 수행하는 코드 집합

# 함수 예 :
# Built_in_Functions : 파이썬에 이미 만들어져서 포함되어 있는 함수
# print()
# input()
# type()

# 사용자 정의 함수 : 개발자가 프로그램 내에서 임의로 생성해서 사용하는 함수

# 함수 정의
# def 함수명([매개변수1, 매개변수2, ...) : # 매개변수 : 사용자가 함수 실행에 필요한 값을 전달하면 저장하는 변수
#   함수 실행부분...
#   [반환문(return)]

print(10) #print 라는 함수를 호출하고 매개변수의 값으로 10을 전달

def show_info() :
    print("성명 : 홍길동")
    print("나이 : 20")

# 매개변수가 있는 함수
def show_info_input(name,age) :
    print("성명 : ", name)
    print("나이 : ", age)

# 리턴값(반환값)이 있는 함수
from datetime import date
def return_today() : # 오늘 날짜를 반환하는 함수
    return date.today()


# 함수 정의만 되어있는 상태에서 실행은 아무작업도 일어나지 않는다.

# 정의된 함수는 호출해야 실행된다.
# 호출 : 함수명([값,값2,값3)
test = show_info() # 함수 호출 - 반환값 없는데 변수에 대입 : None 값이 입력
show_info_input('김철수', '30')
dt = return_today() # 오늘 날짜가 반환
print(test)
print(dt)



