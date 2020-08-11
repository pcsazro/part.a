from django.urls import path

from planner import views

app_name = 'planner'

urlpatterns = [
    path('', views.PlanList.as_view(), name='planList'),
    path('createPlan/', views.create_plan, name='create_plan'),
    path('createPlan2/', views.create_plan2, name='create_plan2'),
    path('updatePlan/<int:pk>', views.UpdatePlan.as_view(), name='updatePlan'),
    path('insertRoute/<int:pk>', views.InsertRoute.as_view(), name='insertRoute'),
    path('place_list/', views.place_list, name='place_list'),
    path('planDetail/<int:pk>', views.PlanDetail.as_view(), name='planDetail'),
    path('getRoute/', views.get_route, name='get_route'),
    path('planDelete/<int:pk>', views.delete_plan, name='planDelete'),
    path('myPlan/<str:m_id>', views.my_plan, name='my_plan'),
    path('deleteRoute/', views.delete_route, name='delete_route'),
]
