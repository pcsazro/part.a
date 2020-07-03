import sys
import requests

API_URL = 'https://dapi.kakao.com/v2/search/image'
MYAPP_KEY = '5b508e7c2d32ca2ac8a8fe3f083c36c7'


def searching():
    from vision import main
    pro_list = main.main()
    print(pro_list)
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}
    try:
        for x in pro_list:
            data = {'query': x}
            resp = requests.post(API_URL, headers=headers, data=data)
            resp.raise_for_status()
            return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)

if __name__ == '__main__':
    searching()