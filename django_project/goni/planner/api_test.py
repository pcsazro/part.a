import xml
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

key = unquote('xs%2BaeIM%2BWhHB4upL7z214MewPZIKyqDICmqDXuQYrViGGjgzZ1rvw8CXsl8D2aoAUX1WqH6IysfC0ECuRBflKw%3D%3D')
import xml.etree.ElementTree as ET

# key = unquote('oa%2F1vuTxTlRxv4qJL7CXdGh7DZZ%2F6roM6wVqM4TmqyaebeDsW9AbPnTaOvINCAUDit1G5balshdfnNzxYsEQtA%3D%3D')

url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList'
queryParams = '?' + urlencode(
    {quote_plus('ServiceKey'): key, quote_plus('ServiceKey'): key, quote_plus('pageNo'): '',
     quote_plus('numOfRows'): '50', quote_plus('MobileApp'): 'AppTest', quote_plus('MobileOS'): 'ETC',
     quote_plus('arrange'): 'A', quote_plus('cat1'): '', quote_plus('contentTypeId'): '12', quote_plus('areaCode'): '',
     quote_plus('sigunguCode'): '', quote_plus('cat2'): '', quote_plus('cat3'): '', quote_plus('listYN'): 'Y',
     quote_plus('modifiedtime'): ''})
request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read().decode('UTF-8')
# print(response_body)

tree = ET.fromstring(response_body).find('body')
items = tree.find('items')
for item in items:
    print('주소: %s' % item.findtext('addr1'))
    print('지역코드: %s' % item.findtext('areacode'))
    print('시군구코드: %s' % item.findtext('sigungucode'))
    print('대표이미지: %s' % item.findtext('firstimage'))
    print('경도: %s' % item.findtext('mapx'))
    print('위도: %s' % item.findtext('mapy'))
    print('제목: %s' % item.findtext('place_title'))
    print('컨텐츠아이디: %s' % item.findtext('contentid'))
    print('컨텐츠타입: %s' % item.findtext('contenttypeid'))
    print('-----------------------------------')
