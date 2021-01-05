# 여러개의 반환값 _ 여러개의 return.py

# 다른 언어는 함수구성시 반환되는 값은 항상 하나여야 함

# 파이썬에서는 함수가 여러개의 값을 반환할 수 있음

def multi_ruturn() :
    return 1,2,3

# 반환된 여러개의 값을 각 변수에 저장
a,b,c = multi_ruturn()
print(a,b,c) #1 2 3

# 반환된 여러개의 값을 하나의 변수에 저장
result = multi_ruturn()
print(result) #(1, 2, 3) 튜플 형태로 들어감

## 여러개의 return 문
def multi_return_1() :
    return 1 # 1을 반환하고 포커스가 main으로 넘어간다
    return 2 # 실행되지 않음
    return 3 # 실행되지 않음

res = multi_return_1()
print(res) #1

