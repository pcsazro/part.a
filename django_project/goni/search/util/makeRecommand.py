import math
from collections import Counter
def caculate(markList,planList) :

    markCnt = len(markList)
    markDic = dict()
    planCnt = len(planList)
    planDic = dict()

    # 배율을 더 큰 기반의 개수의 +1자리수인 10의배수로 해줌(ex.22개일 시, 100)
    # rate = 0
    # if markCnt > planCnt :
    #     rate = (math.ceil(math.log10(markCnt))+1) * 10
    # else :
    #     rate = (math.ceil(math.log10(planCnt)) + 1) * 10

    # mark기반 데이터dic에 가중치 등 연산해서 값 만들어줌
    print('-----mark기반 -----')
    for one in markList:
        id = one.get('place_id')
        # print(id)
        # 받은 리스트 각 카운트해서 Dictionary에 저장(가중치 30줌)
        if markDic.get(id):
            markDic[id] = markDic.get(id) + (3 / markCnt)
            # markDic[id] = (markDic.get(id)) + (3 * rate/markCnt)
            # float( 30 / markCnt)
        else:
            markDic[id] = 3 / markCnt
            # markDic[id] = 3 * (rate/markCnt)
            # float( 30 / markCnt)
    print(markCnt)
    print(markDic)

    # planner기반 데이터dic에 가중치 등 연산해서 값 만들어줌
    print('-----planner기반 -----')
    for one in planList:
        id = one.get('contentid')
        # print(id)
        # 받은 리스트 각 카운트해서 Dictionary에 저장
        if planDic.get(id):
            planDic[id] = planDic.get(id) + (7 / planCnt)
            # planDic[id] = (planDic.get(id)) +  (7 * rate/planCnt)
            # float( 70 / planCnt)
        else:
            planDic[id] = 7 / planCnt
            # planDic[id] = 7 * (rate/planCnt)
            # float( 70 / planCnt)
    print(planCnt)
    print(planDic)

    resultDic = dict()
    resultDic = Counter(planDic) + Counter(markDic)
    print(resultDic)
    # 가중치로 계산된 dic을 값기준으로 내림차순 정렬
    sortedList = sorted(resultDic.items()
                        , reverse=True
                        , key=lambda item: item[1])

    resultList = list()
    # 추천 장소가 9개 넘으면 9개로 추려서 resultList에 담기
    if len(sortedList) > 9:
        # resultList = sortedList[0:9]
        for items in sortedList:
            if (len(resultList)) == 9:
                break
            resultList.append(items[0])
    # 아니면 그냥 담기
    else:
        for items in sortedList:
            resultList.append(items[0])

    print('resultList보내기전 : ', resultList)

    return resultList