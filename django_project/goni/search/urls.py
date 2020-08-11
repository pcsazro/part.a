"""travel_project URL Configuration

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
from django.contrib import admin
from django.urls import path, include

import search
from search.views import *

app_name='search'

urlpatterns = [
    path('searching/', search.views.searching, name="search"),
    path('main/', search.views.searchForm, name="main"),
    path('addr2/', search.views.showAddr2, name="addr2"),
    path('detail/<str:pk>', search.views.showDetail, name="detail"),
    path('addMark/<str:contentid>', search.views.addMark, name="addMark"),
    path('delMark/<str:contentid>', search.views.delMark, name="delMark"),
    path('recommand/<str:contentid>/<str:areacode>', search.views.recommand, name="recommand"),
    path('rank/', search.views.rank, name="rank"),
]
