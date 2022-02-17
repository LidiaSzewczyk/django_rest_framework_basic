from django.urls import path

from . import views

urlpatterns = [
    path('', views.MixinStudentList.as_view(), name='student-list'),
    path('<int:pk>/', views.MixinStudentDetail.as_view(), name='student-detail'),
]