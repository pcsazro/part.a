# 교보문고에 가서 1000원 짜리 스티커 3장과
# 2500원 짜리 책갈피를 4개 샀습니다.
# 우수회원 할인으로 100% 할인을 받았습니다.
# 내가 낸 금액은 얼마일까요?

s_price = int(input("스티커는 할 장당 얼마인가요? "))
s_per = int(input("스티커 몇 장을 구매하셨나요? "))
b_price = int(input("책갈피는 한 개당 얼마인가요?"))
b_per = int(input("책갈패 몇 개를 구매하셨나요?"))

vip = input("당신은 우수회원입니까?(네/아니오) ")

tot = s_price*s_per+b_price*b_per

if vip == "네" :
    print("총 금액은 ", int(tot*0.9), "원 입니다.")
else :
    print("총 금액은 ", tot, "원 입니다.")