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
ids = list()
sql = "SELECT contentid FROM search_place;"
cursor.execute(sql)
ids = cursor.fetchall()

for id in ids:
    key = unquote('xs%2BaeIM%2BWhHB4upL7z214MewPZIKyqDICmqDXuQYrViGGjgzZ1rvw8CXsl8D2aoAUX1WqH6IysfC0ECuRBflKw%3D%3D')

    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailCommon'
    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): key, quote_plus('ServiceKey'): key, quote_plus('numOfRows'): '10',
         quote_plus('pageNo'): '1', quote_plus('MobileOS'): 'ETC', quote_plus('MobileApp'): 'AppTest',
         quote_plus('contentId'): id['contentid'], quote_plus('contentTypeId'): '', quote_plus('defaultYN'): 'Y',
         quote_plus('firstImageYN'): 'Y', quote_plus('areacodeYN'): 'Y', quote_plus('catcodeYN'): 'Y',
         quote_plus('addrinfoYN'): 'Y', quote_plus('mapinfoYN'): 'Y', quote_plus('overviewYN'): 'Y'})

    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('UTF-8')

    tree = ET.fromstring(response_body).find('body')
    items = tree.find('items')
    for item in items:
        overview = item.findtext('overview').replace('"', "'")
        sql = '''UPDATE search_place
          SET homepage = '%s', overview = "%s"
          WHERE contentid = '%s';''' % (item.findtext('homepage'), overview, id['contentid'])
        cursor.execute(sql)
        # print("%s" % item.findtext('homepage'))
        # print("%s" % item.findtext('overview'))

conn.commit()
conn.close()
