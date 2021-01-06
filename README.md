# 함수

## 0.함수 개념

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105150633562.png" alt="image-20210105150633562" style="zoom: 50%;" />

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105150729406.png" alt="image-20210105150729406" style="zoom:50%;" />

​                                                          <img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105151006635.png" alt="image-20210105151006635" style="zoom:50%;" />

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105151204475.png" alt="image-20210105151204475" style="zoom:50%;" />





<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105151714591.png" alt="image-20210105151714591" style="zoom:50%;" />



<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105151840411.png" alt="image-20210105151840411" style="zoom:50%;" />



<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105151957077.png" alt="image-20210105151957077" style="zoom:50%;" />

## 1.함수 기초

```python
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
# 함수 실행부분...
# [반환문(return)]

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
test = show_info() #성명 : 홍길동 나이 : 20
# 함수 호출 - 반환값 없는데 변수에 대입 : None 값이 입력
show_info_input('김철수', '30')
dt = return_today() # 오늘 날짜가 반환
print(test) # None
print(dt) # 2021-01-06
```

### 1.연습 문제

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105153120833.png" alt="image-20210105153120833" style="zoom:50%;" />

```python
def show_info() :
    print("홍길동")
    print("20")
    print("010-124")

show_info() 
#홍길동 
#20 
#010-124

```

### 2.함수 연습문제

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105154658696.png" alt="image-20210105154658696" style="zoom:50%;" />

```python
# 두 수를 전달받아서 더한 결과를 출력하는 함수

# 함수정의 부분
def sum(num1, num2) :
    print('합 : ', num1+num2)

# main(호출부분)

n1 = int(input("숫자1 입력:"))
n2 = int(input("숫자2 입력:"))

# sum(5,7)
sum(n1,n2)

########################################
#숫자1 입력:3
#숫자2 입력:4
#합 :  7
```

## 2.반환값이 있는 함수

### 1.반환값이 있는 함수 개념

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105160852462.png" alt="image-20210105160852462" style="zoom:50%;" />

```python
# 반환값있는 sum 함수.py
# 사용자로부터 두수를 전달 받아서 더한 결과를 출력하는 함수

# 함수 정의 부분
def sum() :
    n1 = int(input('숫자 1 입력 : '))
    n2 = int(input('숫자 2 입력 : '))
    return  n1 + n2

# main(호출부분)

tot = sum()
# tot = 7

# 함수 호출하면 결과값이 함수값이 함수이름 위치로 반환되고
# 반한된 값은 왼쪽의 변수에 저장
print('두 수의 합 : ', tot)
print('두 수의 합 : ', sum()) # 반환 값을 변수에 저장하지 않고 바로사용 
```

### 2.함수 연습문제

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105161020954.png" alt="image-20210105161020954" style="zoom:50%;" />

```python
# 함수 정의 부분
def get_area() :
    width = int(input("가로길이 입력 : "))
    height = int(input("세로길이 입력 : "))
    area = width * height
    return area # 결과값 반환

rect_area = get_area() # 함수 호출하고 반환값 받기
print("사각형의 면적 : %d" % rect_area)
```

### 3. 여러개의 반환값 / 여러개의 리턴

#### 여러개의 반환값 연습문제

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105162459109.png" alt="image-20210105162459109" style="zoom:50%;" />

```python
# 정의

def order() :
    pr = int(input('상품가격입력 : '))
    qt = int(input('주문수량입력 : '))
    amt = pr * qt
    return pr,qt,amt

# main(호출)
price,qty,amount = order()
print('-----------')
print('상품가격 : ', price, '원')
print('주문수량 : %d개' % qty)
print('주문액 : %d개' % amount)
```

### 4.다른자료형의 리턴

```python
# 다른자료형의 리턴.py
def get_names() :
    names = []
    for i in range(3):
        name = input('이름입력 : ')
        names.append(name)

    return names # 리스트를 반환하는 함수

def get_names_dict():
    names = {}
    for i in range(3):
        name = input('이름입력 : ')
        age = input('나이 입력 : ')
        names[name] = age # 딕셔너리 반환

    return names

# 리스트 반환
print(get_names())
# 딕셔너리 반환
print(get_names_dict())
```

## 3.매개변수가 있는 함수

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105163936282.png" alt="image-20210105163936282" style="zoom:50%;" />

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210105163957934.png" alt="image-20210105163957934" style="zoom:50%;" />

### 1.사칙연산

```python
# 03_Functino_parameter_four.py
# 값 두개를 전달받아 +,-,*,/ 정의
def add(n1,n2) :
    return n1 + n2

def sub(n1,n2) :
    return n1 - n2

def mul(n1,n2) :
    return n1 * n2

def div(n1,n2) :
    if n2 != 0:
        return n1 / n2

# 호출
print(add(3,9))
print(sub(3,9))
print(mul(3,9))
print(div(3,9))
```

#### 사칙연산 프로그램

```python
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
        print('잘못된 연산자 입니다. 다시 입력하세요.')매개변수 예제
```

### 2.이자율 계산 예제

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210106091511622.png" alt="image-20210106091511622" style="zoom:50%;" />

```python
# 함수예제_이자액 계산.py

# 선언부분
# import 관련한 부분
# 변수 선언(변수관련 초기화 부분)

# 정의부분
# 함수정의(def)
def get_interest(dps, rate) : # 매개변수 : 함수에서 사용할 실제 값을 전달받는 공간, 함수내에서만 사용
    inter = dps * rate / 100
    return int(inter) # 정수 반환

# main(실행 시작 부분)
deposit = int(input('예금액 입력 : '))
int_rate = float(input('이자율 입력(%) : '))

interest = format(get_interest(deposit, int_rate), ',') # 천단위 구분자 설정(format 함수)
                                                        # 쉼표 추가한 복합문자 (문자)

print('이자액 : %s 원' % interest)
```

### 3.list, dict, tuple

```python
# 함수에 집합자료형전달.py
# 매개변수로 list, dict, Tuple

# 함수에 리스트 전달
def show_names(names) :
    for name in names :
        print(name, end= ' ')

name_list = ['kim', 'lee', 'park']
show_names(name_list) # 리스트가 저장된 번지값이 전달

# 함수에 딕셔너리 전달
def show_info(info) :
    print(info)
    print('이름 : ', info['name'])

info_list = {'name':'kim', 'age':23}
show_info(info_list)
# show_info('aaa') # 딕셔너리가 아닌 문자열이 전달되어 함수에 전달하고 함수작업 과정에서 error
```

## 4.가변길이 매개변수

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210106095327218.png" alt="image-20210106095327218" style="zoom:50%;" />

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210106095446303.png" alt="image-20210106095446303" style="zoom: 50%;" />

```python
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
```

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210106095644485.png" alt="image-20210106095644485" style="zoom:50%;" />

```python
# 가변길이매개변수_kwargs.py

# key = value의 값을 받음(dict 형태로 전달)

def show_kewards(**kwargs) :
    print('----------------')
    for key in kwargs.keys() :
        print(key, end=' ')
    print('\n')

    for val in kwargs.values() :
        print(val, end= ' ')
    print('\n')

    for item in kwargs.items() :
        print(item)

show_kewards(id='sun',
             name='kim',
             phone='010-1234-1234')

show_kewards(n1=2,
             n2=2,
             n3=3,
             n4=4)

# show_kewards(1=2,2=2) # key는 숫자형을 쓸 수 없다.
```





## 5.위치 인수 vs 키워드 인수

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210106103629224.png" alt="image-20210106103629224" style="zoom:50%;" />



<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210106223546286.png" alt="image-20210106223546286" style="zoom:50%;" />



<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210106103834445.png" alt="image-20210106103834445" style="zoom:50%;" />

### 1.keward

```python
# 키워드 인수.py

# 위치인수 : 나열한 순서대로 매개변수에 전달 되는 인수(위치값으로 전달될 변수를 정함)
# add(1,2,3) -> 1은 첫번째 매개변수로 3은 마지막 매개변수로 전달
# 키워드 인수 : 인수들 앞에 키워드를 두어서 인수를 구별하는 방식
# add(a=1,c=3,b=2) -> 각 인수 앞에 키워드에 해당하는 변수로 전달(매개변수 순서를 변경할 수 있음)

def student_info(name,age,gender) :
    student = {
        'name' : name,
        'age' : age,
        'gender' : gender
    }
    return student

print(student_info('kim',23,'여')) # 위치 인수
print(student_info(age=23,name='kim',gender='여')) # 키워드 인수
print(student_info('lee',gender='남',age=22)) # 혼용사용

# 주의사항(혼용사용시) - 위치인수가 키워드 인수 앞에 있어야 한다
# print(student_info(gender='남',age=22,'lee')) SyntaxError: positional argument follows keyword argument
# print(student_info(name='lee',22,gender='남'))
print(student_info('lee',22,gender=22))
```



## 6. 지역변수와 전역변수

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210106105831409.png" alt="image-20210106105831409" style="zoom:50%;" />

### 1. 지역변수, 전역변수 개념

```python
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
```

### 2.전역변수

```python
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
```

### 3.지역변수 전역변수 예제



<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210106114727321.png" alt="image-20210106114727321" style="zoom:50%;" />

​																									7 3 4 3
​																									7 2 3 4

## 7.매개변수 딕셔너리

```python
# 딕셔너리 형태 반환.py

product_list = [{'name':'노트북', 'price':1200000},
                {'name':'냉장고', 'price':1700000},] # 리스트에 딕셔터리를 포함하는 구조

# 딕셔너리를 전달 받아서
# 일부만 추출해서 딕셔너리 형태로 반환하는 함수

def ge_product_inf(prd_dic) :
    name = prd_dic['name']
    price = prd_dic['price']

    # a = {'no1':name, 'no2':price}
    # return a #a dict 반환
    return {'no1':name, 'no2':price} # 반환의 형태가 dict 구조가 가능능

#리스트에서 딕셔너리를 함수에 전달
# 반환값 받아서 출력

for prd in product_list :
    prd_info = get_product_inf(prd)
    print(prd_info)
```

###  매개변수 리스트

```python
# 리스트를 함수에 전달.py

# 매개변수의 값으로 리스트를 전달 했을 경우
# 함수에서 리스트 요소 변경시 원본 리스트도 변경

def show_list(my_list) : # 매개변수 my_list - 지역변수
    print('전달된 리스트 변경 없음 : ', my_list)  # 변경 전 전달내용 출력
    my_list[0] = 10 # 첫번째 요소 변경
    print('첫번째 요소 변경후 : ', my_list)
    print('1. id(함수내): ', id(my_list)) #id는 변수가 생성된 메모리의 주소를 반환 하는 함수
    # 함수 외 전역변수(my_list)와 id가 동일하다

    ### 전체 리스트에 새로운 값을 저장 시
    # 원본리스트의 전체 요소가 변경되는 것이 아니라

    my_list = [100,200,300] # 새로운 리스트를 생성 - 공간도 새로 차지하게 됨
    print('함수 내에서 my_list의 전체 값을 다시 저장')
    print(my_list) # [100,200,300]
    print('3. id(함수내-매개변수) : ', id(my_list)) # 새로운 id가 출력

my_list = [1,2,3,4] # 함수 외부 선언 : 전역변수
print('함수 호출 전')
print(my_list) # 호출 전

print('함수 호출')
show_list(my_list)

print('함수 호출 후')
print(my_list) # 호출 후

print('2. id(함수내): ', id(my_list)) # 함수내 매개변수와 동일한 id

# 리스트를 매개변수로 전달하면 함수내 or 함수외부에서 동일한 리스트를 사용하게 된다.
# 전달된 리스트 요소의 일부를 함수내에서 변경하면 원본 리스트도 동일하게 변경된다.
# 단, 함수내에서 변수 = [값1,값2,값3] 리스트변수를 생성하면 해당변수는 완전한 지역변수로 처리 된다.
```

## 8.매개변수 연습문제

### order

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210106133439463.png" alt="image-20210106133439463" style="zoom:50%;" />

```python
# def order() :
#     def get_interest(price, amount):  # 매개변수 : 함수에서 사용할 실제 값을 전달받는 공간, 함수내에서만 사용
#         inter = price * amount
#         if int(inter
#
#         return int(inter)  # 정수 반환
#
#     # main(실행 시작 부분)
#     price = int(input('상품가격 입력 : '))
#     qty = int(input('주문 수량 입력 : '))
#
#     interest = format(get_interest(price, qty), ',')  # 천단위 구분자 설정(format 함수)
#     # 쉼표 추가한 복합문자 (문자)
#
#     print('주문액 : %s 원' % interest)

def order(price, qty) :
    amount = price * qty
    if amount >= 100000 :
        discount = amount * 0.1
    elif amount >= 5000 :
        discount = amount * 0.05
    else :
        discount = 0
    total = amount - discount
    return  amount, discount, total # 지역변수의 값이 반환

# main

price = int(input('상품 가격 입력 : ')) # 전역변수
qty = int(input('주문 수량 입력 : ')) # 전역변수

amount, discount, total = order(price,qty) # 전역변수 생성
print('-------------------')
print('주문액 : \t', amount)
print('할인액 : \t', int(discount))
print('총금액 : \t', int(total)
```

### gbb



<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210106140034806.png" alt="image-20210106140034806" style="zoom:50%;" />

```python
from random import randint

def gbb_game(you) :
    com = randint(1,3)
    if com - you == 1 or com - you == -2 :
        print("com 승")

    elif com == you :
        print('비김')

    else:
        print('you 승')

    print("com : %d " % com)

you = int(input("you 입력(1:가위, 2:바위, 3:보) : "))
gbb_game(you)
```



![image-20210106231532050](C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210106231532050.png)



### dic

<img src="C:%5CUsers%5Cchangdo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210106141622500.png" alt="image-20210106141622500" style="zoom:50%;" />

```python
# 매개변수 연습문제3

def show_info(name,year,age,phone) : # 사용자 정의 함수
    return  {'name':name, 'year':year, 'age':age, 'phon':phone}

print(show_info('홍길동',4,23,'010-1234-1234')) # Built_in_Functions


```

