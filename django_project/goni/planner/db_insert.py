from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import xml.etree.ElementTree as ET
import pymysql

conn = pymysql.connect(host='localhost',
                       port=3708,
                       user='root',
                       password='1234',
                       db='travelPlan',
                       charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)

key = unquote('xs%2BaeIM%2BWhHB4upL7z214MewPZIKyqDICmqDXuQYrViGGjgzZ1rvw8CXsl8D2aoAUX1WqH6IysfC0ECuRBflKw%3D%3D')

url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList'
queryParams = '?' + urlencode(
    {quote_plus('ServiceKey'): key, quote_plus('ServiceKey'): key, quote_plus('pageNo'): '',
     quote_plus('numOfRows'): '300', quote_plus('MobileApp'): 'AppTest', quote_plus('MobileOS'): 'ETC',
     quote_plus('arrange'): 'B', quote_plus('cat1'): '', quote_plus('contentTypeId'): '12', quote_plus('areaCode'): '',
     quote_plus('sigunguCode'): '', quote_plus('cat2'): '', quote_plus('cat3'): '', quote_plus('listYN'): 'Y',
     quote_plus('modifiedtime'): ''})
request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read().decode('UTF-8')

tree = ET.fromstring(response_body).find('body')
items = tree.find('items')
data = ['', '', '', '', '', '', '', '', '', '']
for item in items:
    data[0] = item.findtext('contentid')
    data[1] = item.findtext('addr1')
    data[2] = item.findtext('areacode')
    data[3] = item.findtext('sigungucode')
    data[4] = item.findtext('firstimage')
    data[5] = item.findtext('mapx')
    data[6] = item.findtext('mapy')
    data[7] = item.findtext('title')
    data[8] = item.findtext('contenttypeid')
    data[9] = item.findtext('tel')
    sql = '''INSERT INTO search_place (contentid, addr, areacode, sigungucode, firstimage, mapx, mapy, place_title, contenttypeid, tel)
    VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' % (
        data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])
    cursor.execute(sql)
conn.commit()
conn.close()
