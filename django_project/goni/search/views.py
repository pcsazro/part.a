from django.core import serializers
from django.db.models import Q, Subquery, Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from search.models import Place, Mark, RankWord
from planner.models import PlannerD
from search.util.api_addr2 import getAddr2
from search.util.api_area import GetAddr1
from search.util.makeFile import *
from search.util.makeRecommand import *
from datetime import datetime, timedelta


# 최초에 검색 폼 불러옴
def searchForm(request):
    addr1 = GetAddr1()
    addrList = addr1.list
    # request.session['id'] = 'erin'  # 임의로 넣어준 세션
    return render(request, "search/main.html", {"addrList": addrList})


# 검색조건에 맞추어서 결과 검색해서 반환함
def searching(request):
    model = Place
    areacode = request.POST.get('areacode')
    sigungucode = request.POST.get('sigungucode')
    contenttypeid = request.POST.getlist('contenttypeid[]')
    place_title = request.POST.get('place_title')
    q = Q()
    if areacode != '0':
        q.add(Q(areacode=areacode), q.AND)
        print("area있음: " + areacode)
    if sigungucode != '0':
        q.add(Q(sigungucode=sigungucode), q.AND)
        print("sigungucode있음: " + sigungucode)
    if len(place_title) != 0:
        q.add(Q(place_title__icontains=place_title), q.AND)
        print("place_title검색: " + place_title)
        # 검색어 파일에 저장해서 수집해줌
        collectWord(place_title)
    q.add(Q(contenttypeid__in=contenttypeid), q.AND)
    resultList = Place.objects.filter(q)
    return render(request, "search/result.html", {"resultList": resultList})


# 시/도 클릭시 거기에 맞는 시/군/구 가져옴(모듈사용)
def showAddr2(request):
    areacode = request.POST.get('areacode')
    addrList = getAddr2(areacode)
    return render(request, "search/addr2.html", {"addr2List": addrList})


# 검색페이지에서 하나의 장소 상세보기로 들어감
def showDetail(request, pk):
    place = Place.objects.get(contentid=pk)
    markAll = Mark.objects.all().filter(Q(place_id=pk))
    myMark = Mark.objects.filter(m_id=request.session.get('id'), place_id=pk)
    return render(request, "search/detail.html", {"pk": pk,
                                                  "object": place,
                                                  "mark": len(markAll),
                                                  "myMark": len(myMark)})


# 장소 찜등록
def addMark(request, contentid):
    model = Mark(m_id=request.session.get('id'), place_id=contentid, mark_date=datetime.now())
    model.save()
    return HttpResponseRedirect('/search/detail/' + contentid)


# 장소 찜해제
def delMark(request, contentid):
    markOne = Mark.objects.filter(m_id=request.session.get('id'), place_id=contentid)
    markOne.delete()
    return HttpResponseRedirect('/search/detail/' + contentid)


# 장소 추천
def recommand(request, contentid, areacode):
    # here = Place.objects.filter(contentid=contentid).values('contentid','areacode')

    # 추천 리스트(찜기반, 같은지역)
    markList = Mark.objects.filter(
        place_id__in=Subquery(
            Place.objects.filter(Q(areacode=areacode) & ~Q(contentid=contentid))
                .values('contentid')
        )
    ).order_by('place_id').values('place_id')
    # print('len ', str(len(markList)))

    # 추천 리스트(플래너에 공통 추가 기반)(가중치 70줌)
    # planList = PlannerD.objects.extra(tables=['search_place'], where=['search_place.contentid=search_plannerd.contentid'])
    planList = PlannerD.objects.filter(
        ~Q(contentid=contentid),
        p_id__in=Subquery(
            PlannerD.objects.filter(Q(contentid=contentid))
                .values('p_id')
        )
    ).order_by('contentid').values('contentid')
    # print('len ', str(len(planList)))

    recommandList = caculate(markList, planList)
    resultList = Place.objects.filter(
        Q(contentid__in=recommandList))
    print('resultList받아온 후 : ', resultList)

    return render(request, "search/recommand.html", {"resultList": resultList})


def rank(request):
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    # word, cnt Dic형태를 담은 QuerySet으로 반환됨
    # selectDic = RankWord.objects.filter(Q(sd_date=yesterday)).values('word').annotate(cnt=Count('word')).order_by('-cnt')[:5]
    selectDic = RankWord.objects.filter(Q(sd_date=yesterday)).order_by('-count')[:5]
    print(selectDic)

    rankList = list()
    for one in selectDic:
        rankList.append(one.word)
        # print(one.word,'..',str(one.count))
    print(rankList)

    return render(request, "search/rank.html", {"rankList": rankList
        , 'yesterday': yesterday.__str__()})


# def get_route(request):
#     p_id = request.POST.get('p_id')
#     routes = PlannerD.objects.filter(p_id=p_id).order_by('seq')
#     places = dict()
#     for r in routes:
#         place = Place.objects.filter(contentid=r.contentid_id)
#         places[r.contentid_id] = serializers.serialize('json', place, ensure_ascii=False)
#     return JsonResponse(places)
if __name__ == "__main__":
    addr1 = GetAddr1()
    addrList = addr1.trans()
    print(addrList)
