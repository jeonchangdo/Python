# 함수 정의 부분
def fram() :
    n1 = int(input('가로길이 입력 : '))
    n2 = int(input('세로길이 입력 : '))
    return  n1 * n2

# main(호출부분)

tot = fram()
# tot = 7
print('사각형의 면적 : ', tot)
print('사각형의 면적 : ', fram())