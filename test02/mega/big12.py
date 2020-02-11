# 원래 가입한 아이디는 root임.
# 로그인할 id를 입력 >> root
# 로그인 되었습니다.

# 로그인할 id를 입력 >> root1
# 로그인 되지 않았습니다.

id = str("root")

ida = input("로그인할 id를 입력: ")
if ida == id:
    print("로그인 되었습니다.")
else:
    print("로그인 되지 않았습니다.")