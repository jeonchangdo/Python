# 가변길이 매개변수_args.py
# 가변길이 매개변수 : 1개의 매개변수로 개수가 정해지지 않은
# 여러개의 값을 전달 받을 때 사용하는 매개변수
# 매개변수 형태 : *매개변수 (인수값 여러개를 전달가능)

# 함수측에서는 어떤 형태로 전달 받는건지 확인

def test_args(*args) :
    print(type(args)) # *args는 튜플형태로 구성됨

test_args(1,2,3,4,5)

# kwargs 형태 확인
def test_kwargs(**kwargs) :
    print(type(kwargs)) # **kwargs는 <class 'dict'>

test_kwargs(a=1, b=2, c=3)

# *args 예제
def order_coffee(coffee, *options) : # 필수 매개변수와 가변길이 매개변수 혼용
    print(coffee + ", 옵션 : " , end= '')

    for opt in options :
        print(opt, end = ' ')
    print()

order_coffee('아마레카노')
order_coffee('아메리카노', 'tall', 'Hot', '시럽')
# order_coffee() TypeError: order_coffee() missing 1 required positional argument: 'coffee'

############################

def order_coffee_1(coffee, *options, fin='end') : # 필수 매개변수와 가변길이 매개변수 혼용
    print(coffee + ", 옵션 : " , end= '')

    for opt in options :
        print(opt, end = ' ')
    print(fin)

order_coffee_1('아마레카노')
order_coffee_1('아메리카노', 'tall', 'Hot', '시럽')

#########################

def order_coffee_2(coffee, fin='end', *options) : # 필수 매개변수와 가변길이 매개변수 혼용
    print(coffee + ", 옵션 : " , end= '')

    for opt in options :
        print(opt, end = ' ')
    print(fin)

order_coffee_2('아마레카노')
order_coffee_2('아메리카노', 'tall', 'Hot', '시럽')

# 필수매개변수, 디폴트매개변수, 가변길이변수 혼용가능
# 필수매개변수(일반)는 무조건 앞쪽에 배치 되어야 함