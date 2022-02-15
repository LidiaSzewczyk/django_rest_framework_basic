from django.urls import path

from . import views

urlpatterns = [
    path('static/', views.staticView, name='static'),
    path('plant/', views.plantView, name='plant'),
    path('', views.flowers_view, name='flowers'),
    path('create/', views.create_flower_view, name='flower-create'),
    path('list/', views.flowers_list, name='flower-list'),
    path('<int:pk>/', views.flower_detail, name='flower-detail'),

]
