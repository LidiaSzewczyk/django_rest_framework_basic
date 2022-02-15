from django.urls import path
from . import views

app_name = 'classes'

urlpatterns = [
    path('', views.TreeList.as_view(), name="tree-list"),
    path('<int:pk>/', views.TreeDetail.as_view(), name="tree-detail"),
]