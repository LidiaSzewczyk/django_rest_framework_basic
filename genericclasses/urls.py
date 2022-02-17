from django.urls import path

from . import views

urlpatterns = [
    path('', views.GenericStudentList.as_view(), name='student-list'),
    path('<int:pk>/', views.GenericStudentDetail.as_view(), name='student-detail'),
]
