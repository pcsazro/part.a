# movie 패키지를 만드세요.
# price.py 모듈을 만드세요.
# info 함수 정의
        # 처리 내용은 같이 볼 사람 이름, 관계(ex.친구) 입력
        # 볼 사람 정보 (이름, 관계) 출력


#pay 함수 정의
        # price = 10000
        # 인원수 입력
        #지불할 금액 출력

def info():
    name = input("이름 ")
    rel = input("관계 ")
    print(name, rel)

    #강사님께서 한번에 입력하는 것으로 만들어 주신 부분
    # name, rel = input('이름과 관계입력>> ').split(',')
    # print(name, ' ', rel)



def pay():
    price = 10000
    num = int(input("인원수 "))
    print(num*price)