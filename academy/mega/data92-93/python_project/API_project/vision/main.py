import tkinter
from vision import SearchAPI
from vision import openAPI

tk = tkinter.Tk()

tk.title("title")
tk.geometry("1000x800+310+10")

# img_url = img_crawling()

# for x in img_url:
#     response = requests.get(x)
#     이미지를 다운받으면 for문 끝

# 다운 받은 이미지 들을 png로 변환 (tkinter can show only png files)

# 변환한 png를 list에 넣어 img_file 생성
# img_file = []

# 기존 url과 다운 받은 이미지를 매치시켜 dictionary 형태로 만든다. 
img = {'https://image.msscdn.net/images/event_banner/2020062616121100000021386.jpg': 'test1.png',
       'https://image.msscdn.net/images/event_banner/2020062911375200000085332.jpg': 'test2.png',
       'https://image.msscdn.net/images/event_banner/2020062315055400000004380.jpg': 'test3.png',
       'https://image.msscdn.net/images/event_banner/2020062616182800000032896.jpg': 'test4.png',
       'https://image.msscdn.net/mfile_s01/_shopstaff/list.staff_5ef55d98d9a43.jpg': 'test5.png',
       'https://image.msscdn.net/images/img/2020062310105300000075487.jpg': 'test6.png',
       'https://image.musinsa.com/mfile_s01/2020/06/25/2de40e0d504f583cda7465979f958a98160715.jpg': 'test7.png',
       'https://www.ggilbo.com/news/photo/202005/765064_598433_407.jpg': 'test8.png',
       'https://www.topdaily.kr/news/photo/202003/65332_30875_2452.jpg': 'test9.png',
       'https://www.isstime.co.kr/news/data/20141216/p179567428425990_495.jpg': 'test10.png'}

# tkinter에 올리기 위한 png만 선택
img_values = list(img.values())

# 인덱스로 사용하기 위한 변수 x
x = 0

# 시작 페이지에 사용할 파일 지정
ph = tkinter.PhotoImage(file="test1.png")
# 라벨에 올려주기
label = tkinter.Label(tk, image=ph)


def search():
    s = SearchAPI.searching()
    print(s)


# 앞으로 버튼
def prev():
    global x
    x -= 1
    if x < 0:
        x = 9
    pho = tkinter.PhotoImage(file=img_values[x])
    label.configure(image=pho)
    label.image = pho


# 뒤로 버튼
def nex():
    global x
    x += 1
    if x > 9:
        x = 0
    pho = tkinter.PhotoImage(file=img_values[x])
    label.configure(image=pho)
    label.image = pho


# 분석을 실행할 함수
def main():
    # 1. API에 사용하기 위한 변수 지정
    image_url = list(img.keys())[x]

    # 2. API 실행(위에 한 변수 사용)
    detection_result = openAPI.detect_product(image_url)
    # print(detection_result)

    # 3. API 실행(위에 두 변수 사용)
    image = openAPI.show_products(image_url, detection_result)

    # API 결과를 보여줌
    image.show()

    # 재활용할 text 값을 저장할 리스트 생성
    product_list = []
    for i in detection_result['result']['objects']:
        # print(i['class'])
        # 필요한 class들을 리스트에 추가
        product_list.append(i['class'])
    # print(product_list)
    return product_list


# 라벨을 위치시키는 함수
label.pack()

# 버튼 생성
button_search = tkinter.Button(tk, text="가장 많이 검색된 단어로 검색", command=search)
button_search.pack()
button_pre = tkinter.Button(tk, text="<<", command=prev)
button_pre.place(x=460, y=760)
button_analysis = tkinter.Button(tk, text='분석', command=main)
button_analysis.place(x=491, y=760)
button_nex = tkinter.Button(tk, text=">>", command=nex)
button_nex.place(x=529, y=760)

# 프레임 활성
tk.mainloop()
