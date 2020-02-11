# 메세지 박스에는 두 개만 들어갈 수 있다.

from tkinter import messagebox
# 콘솔에서 당신의 짝이름을 입력 받으세요.
name = input("짝이름: ")
# 콘솔에서 당신의 짝관심사를 입력 받으세요.
want = input("짝 관심사: ")
# 메세지 박스로 당신의 짝이름과 관심사를 확인하여 출력
messagebox.showinfo(name, want)
# 관심사가 파이썬이라고 한다면, "프로그래머가 되실 거군요."
#                   아니라면, "데이터 분석가가 되실 거군요." 출력
if want == "파이썬":
    messagebox.showinfo("결과", "프로그래머가 되실 거군요.")
else:
    messagebox.showinfo("결과", "데이터 분석가가 되실 거군요.")

# 메세지 박스로 파이썬이 확실한가요?
result = messagebox.askquestion("질문", "파이썬이 확실한가요?")
if result == "yes":
    # 맞다라고 하면, 열심히 하세요!
    messagebox.showinfo("답", "열심히 하세요!")
else:
    # 아니라고 하면, 그럼 생각중이시군요!
    messagebox.showinfo("답", "그럼 생각중이시군요!")

