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












