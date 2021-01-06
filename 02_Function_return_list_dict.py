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