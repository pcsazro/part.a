from django.forms import model_to_dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, request
from member.models import *


def MemberCreate(request):
    return render(request, 'member/member_create.html')


def MemberCreate2(request):
    member = Member()
    member.id = request.POST['id']
    member.pw = request.POST['pw']
    member.name = request.POST['name']
    member.tel = request.POST['tel']
    member.email = request.POST['email']
    member.gender = request.POST['gender']
    member.save()
    return render(request, 'member/joinsuccess.html')


def joinsuccess(request):
    return render(request, 'member/joinsuccess.html')


class MemberUpdate(UpdateView):
    model = Member
    fields = ['id', 'pw', 'name', 'tel', 'email']
    template_name_suffix = '_update'
    # return HttpResponseRedirect('index')
    success_url = reverse_lazy('planner:planList')  # 뭐들어가야하는지 확인
    # render(request, 'main/place_list.html')


def checkid(request):
    try:
        member = Member.objects.get(id=request.GET['id'])
    except Exception as e:
        member = None
    result = {
        'result': 'success',
        # 'data': model_to_dict(planner)
        'data': "not exist" if member is None else "exist"
    }
    return JsonResponse(result)


def member_login(request):
    return render(request, 'member/member_login.html')


def login(request):
    results = Member.objects.filter(id=request.POST['id']).filter(pw=request.POST['pw'])
    # 로그인 실패
    if len(results) == 0:
        return HttpResponseRedirect('/member_login?results=fail')

    # 로그인 처리
    id = results[0]
    request.session['id'] = id.id
    return HttpResponseRedirect('/planner/')


def logout(request):
    del request.session['id']
    return HttpResponseRedirect('/planner/')


def index(request):
    return render(request, 'member/index.html')
