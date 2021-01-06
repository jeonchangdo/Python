# 03_Function_param_four.py
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












