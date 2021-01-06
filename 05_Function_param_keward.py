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