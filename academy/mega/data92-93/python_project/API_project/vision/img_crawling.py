from bs4 import *
from urllib import request, parse


# url을 가져오기 위한 함수
def img_crawling():
    # web page 지정
    url = 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000'
    # url을 사용해 연결 open
    req = request.urlopen(url)
    # 한글을 사용하기 위해 utf-8 encoding 하여 문서 읽어 가져오기
    html = req.read().decode('utf-8')
    # 가져온 html을 분석
    soup = BeautifulSoup(html, 'html.parser')
    # 분석된 html 중 필요한 값을 모두 찾기
    a = soup.find_all('img', {'class': '_productLazyImg'})
    print(a)
    img_url = []
    for x in a:
        # 좀 더 세부적인 항목을 분리하여 리스트에 추가
        img_url.append(x.get('data-original'))
    print(img_url)
    # 리스트값 반환
    return img_url

# 이 페이지를 활성 시키기 위한 main
# if __name__ == '__main__':
#     img_crawling()
