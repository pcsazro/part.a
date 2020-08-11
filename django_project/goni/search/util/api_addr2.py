from urllib import parse, request
from urllib.parse import quote_plus
import xml.etree.ElementTree as ET
def getAddr2(areacode):
    key = parse.unquote('oa%2F1vuTxTlRxv4qJL7CXdGh7DZZ%2F6roM6wVqM4TmqyaebeDsW9AbPnTaOvINCAUDit1G5balshdfnNzxYsEQtA%3D%3D')
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode'
    queryParams = '?' + parse.urlencode({parse.quote_plus('ServiceKey'): key, parse.quote_plus('ServiceKey'): key
                                            , parse.quote_plus('numOfRows'): '100', parse.quote_plus('pageNo'): '1',
                                         parse.quote_plus('MobileOS'): 'ETC', parse.quote_plus('MobileApp'): 'AppTest'
                                         , parse.quote_plus('areaCode') : areacode })
    request.get_method = lambda: 'GET'
    aa = request.Request(url + queryParams)
    response_body = request.urlopen(aa).read().decode('utf8')
    # print(type(response_body))
    # print (response_body)
#
    root = ET.fromstring(response_body)

    addrList = list()
    item = root.find('body').find('items')
    # print(type(item))
    # print(item.text)
    for child in item :
        addrList.append({'code': child.findtext('code'),'name':child.findtext('name')})
    return addrList
    # print(list)
