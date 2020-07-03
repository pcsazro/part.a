import pymysql
import sys
import argparse
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# DB 연결
HOST = 'localhost'
PORT = 3708
USER = 'root'
PASSWORD = '1234'

conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD)

if conn.open:
    with conn.cursor() as curs:
        print("connected")
conn.close()

# API 사용 인증
API_URL = 'https://kapi.kakao.com/v1/vision/product/detect'
MYAPP_KEY = '5b508e7c2d32ca2ac8a8fe3f083c36c7'


# API 사용 함수 1
def detect_product(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}
    try:
        data = {'image_url': image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)


# API 사용 함수 2
def show_products(image_url, detection_result):
    try:
        image_resp = requests.get(image_url)
        image_resp.raise_for_status()
        file_jpgdata = BytesIO(image_resp.content)
        image = Image.open(file_jpgdata)
    except Exception as e:
        print(str(e))
        sys.exit(0)
    draw = ImageDraw.Draw(image)
    for obj in detection_result['result']['objects']:
        x1 = int(obj['x1'] * image.width)
        y1 = int(obj['y1'] * image.height)
        x2 = int(obj['x2'] * image.width)
        y2 = int(obj['y2'] * image.height)
        draw.rectangle([(x1, y1), (x2, y2)], fill=None, outline=(255, 0, 0, 255))
        draw.text((x1 + 5, y1 + 5), obj['class'], (255, 0, 0))
    del draw
    return image

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Detect Products.')
#     parser.add_argument('image_url', type=str, nargs='?',
#     default="http://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/06.jpg",
#     help='image url to show product\'s rect')
#     args = parser.parse_args()

# 이 아래 있던 활성 main은 tkinter에서 사용하기 위해 main.py의 main()로 이동
