# 디폴트 매개변수.py

def calc(n1,n2) : # 2개의 파라미터를 요구하는 함수
    return n1+n2

calc(2,3) # 인수를 2개를 반드시 전달
# calc(2) # TypeError: calc() missing 1 required positional argument: 'n2'

# 매개변수에 기본값을 지정할 수 있다.
print('abc', end = '0')
print('abc')

# 디폴트 매개변수를 사용 할 수 있다.
def greet(name,msg='안녕!!') : #msg = '안녕!!' 디폴트매개변수(기본값 지정)
    print(name + ',' + msg)

# 호출 시 매개변수 지정
greet('kim', 'hello') # kim,hello

# 호출시 매개변수 하나만 지정
greet('kim') # kim,안녕!!

# 디폴트 매개변수는 위치가 ㄱ반드시 마지막에 위치해야 함
# 앞에 올 경우 error
# def greet(name='안녕!!',msg) : # name 매개변수가 msg 뒤에 있어서
#     print(name + ',' + msg)   # SyntaxError: non-default argument follows default argument

# 디폴트 매개변수는 여러개 사용 할 수 있음
def show_info(name, year=4, age=23) :
    print(name, year, age)

show_info('홍길동')
show_info('홍길동',3)
show_info('홍길동',3,26)
# show_info('홍길동',,20) # 디폴트 매개변수는 앞을 건너 뛰고 사용하면 error

