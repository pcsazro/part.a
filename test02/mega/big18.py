# 네이버 로그인
# 판단을 할 때 조건을 가지고 판단을 한다.
# 조건이 하나가 아닌 경우 논리적으로 어떻게 판단할 것인가?
# 자하철을 타는 경우 1) 편함 2) 저렴함
# 조건들이 모두 맞야(all True) 논리적으로 판단
# => and조건(and)
# 조건들 중에 하나만 맞아도(one True) 논리적으로 판단
# => or조건(or)

id = "root"
pw = "pass"

id2 = input("아이디입력 = ")
pw2 = input("비밀번호 입력= ")

if (id == id2 and pw == pw2):
    print("로그인 ok")
else:
    print("로그인 not")

# 논리연산자
