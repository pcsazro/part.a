from tkinter import messagebox

messagebox.showinfo("안녕하세요.", "홍길동이요!")
# showinfo 앞부부은 제목, 뒷부분은 내용
messagebox.showwarning("졸음주의", "지금은 오후에요!!")
result = messagebox.askquestion("시간체크", "지금은 오후인가요?")
print(result)
