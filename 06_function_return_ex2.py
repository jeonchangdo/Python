# 정의

def order() :
    pr = int(input('상품가격입력 : '))
    qt = int(input('주문수량입력 : '))
    amt = pr * qt
    return pr,qt,amt

# main(호출)
price,qty,amount = order()
print('-----------')
print('상품가격 : ', price, '원')
print('주문수량 : %d개' % qty)
print('주문액 : %d개' % amount)




