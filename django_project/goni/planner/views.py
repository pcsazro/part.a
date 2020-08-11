import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from planner.models import PlannerM, PlannerD
from search.models import Place


class PlanList(ListView):
    model = PlannerM
    paginate_by = 4
    template_name = 'planner/planList.html'


def create_plan(request):
    return render(request, 'planner/createPlan.html')


def create_plan2(request):
    p_title = request.POST.get('p_title')
    m_id = request.POST.get('m_id')
    open_flag = request.POST.get('open_flag')
    t_start = request.POST.get('t_start')
    t_end = request.POST.get('t_end')
    concept = request.POST.get('concept')
    planner_m = PlannerM(p_title=p_title,
                         m_id=m_id,
                         open_flag=open_flag,
                         t_start=t_start,
                         t_end=t_end,
                         concept=concept)
    planner_m.save()
    data = PlannerM.objects.latest('id')
    print(data)
    return HttpResponse(data)


class UpdatePlan(UpdateView):
    model = PlannerM
    fields = ['p_title',
              'm_id',
              'open_flag',
              't_start',
              't_end',
              'concept']
    template_name = 'planner/updatePlan.html'

    success_url = reverse_lazy('planner:planList')


class InsertRoute(CreateView):
    model = PlannerD
    fields = ['p_id',
              'seq',
              'contentid']
    template_name = 'planner/updatePlan3.html'
    success_url = reverse_lazy('planner:planList')


def place_list(request):
    places = Place.objects.order_by('contentid')
    place_list = serializers.serialize('json', places)
    return HttpResponse(place_list, content_type="text/json-comment-filtered")


class PlanDetail(DetailView):
    model = PlannerM
    template_name = 'planner/planDetail.html'


def get_route(request):
    p_id = request.POST.get('p_id')
    routes = PlannerD.objects.filter(p_id=p_id).order_by('seq')
    places = list()
    for r in routes:
        place = Place.objects.filter(contentid=r.contentid_id)
        places.append(serializers.serialize('json', place, ensure_ascii=False))
    return JsonResponse(places, safe=False)


def delete_plan(request, pk):
    queryset = PlannerM.objects.filter(id=pk)
    queryset.delete()
    return HttpResponse()


def my_plan(request, m_id):
    myPlan = PlannerM.objects.filter(m_id=m_id)
    return render(request, 'planner/myPlan.html', {'myPlan': myPlan})


def delete_route(request):
    p_id = request.POST.get('p_id')
    queryset = PlannerD.objects.filter(p_id=p_id)
    queryset.delete()
    return HttpResponse()
