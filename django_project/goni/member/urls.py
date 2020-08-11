"""goni_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

import member
from member.views import MemberUpdate

app_name = 'member'

urlpatterns = [
    path('', member.views.index, name='index'),
    path('memberupdate/<str:pk>', MemberUpdate.as_view(), name='update'),
    path('checkid', member.views.checkid, name='check'),
    path('member_login/', member.views.member_login, name='member_login'),
    path('login/', member.views.login, name='login'),
    path('logout/', member.views.logout, name='logout'),
    path('joinsuccess/', member.views.joinsuccess, name='joinsuccess'),
    path('membercreate/', member.views.MemberCreate, name='create'),
    path('membercreate2/', member.views.MemberCreate2, name='create2'),
]
