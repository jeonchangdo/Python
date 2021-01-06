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