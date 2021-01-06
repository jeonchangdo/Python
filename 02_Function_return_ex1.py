# 함수 정의 부분
def get_area() :
    width = int(input("가로길이 입력 : "))
    height = int(input("세로길이 입력 : "))
    area = width * height
    return area # 결과값 반환

rect_area = get_area() # 함수 호출하고 반환값 받기
print("사각형의 면적 : %d" % rect_area)