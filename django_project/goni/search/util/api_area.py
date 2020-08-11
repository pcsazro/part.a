from urllib import parse, request
import xml.etree.ElementTree as ET
class GetAddr1 :
    key = parse.unquote('oa%2F1vuTxTlRxv4qJL7CXdGh7DZZ%2F6roM6wVqM4TmqyaebeDsW9AbPnTaOvINCAUDit1G5balshdfnNzxYsEQtA%3D%3D')
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode'
    queryParams = '?' + parse.urlencode({ parse.quote_plus('ServiceKey') : key, parse.quote_plus('ServiceKey') : key
                    , parse.quote_plus('numOfRows') : '100', parse.quote_plus('pageNo') : '1', parse.quote_plus('MobileOS') : 'ETC', parse.quote_plus('MobileApp') : 'AppTest'})

    aa = request.Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = request.urlopen(aa).read().decode('utf8')
    print(type(response_body))
    #print (response_body)

    root = ET.fromstring(response_body)
    list = list()
    items = root.find('body').find('items')
    #print(type(items))
    #print(items.text)
    for item in items :
       # print(child.findtext('code'), end=' ')
       # print(child.findtext('name'))
        list.append({'code': item.findtext('code'),'name':item.findtext('name')})
    #print(list)

    def trans(self):
        return list