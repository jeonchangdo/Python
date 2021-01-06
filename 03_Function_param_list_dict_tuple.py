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