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


