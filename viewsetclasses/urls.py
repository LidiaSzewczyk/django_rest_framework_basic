from rest_framework.routers import SimpleRouter

from viewsetclasses import views

app_name = 'vievsets'

router = SimpleRouter()
router.register('drug-category', views.DrugCategoryViewSet, basename='drug-category')
router.register('drug', views.DrugViewSet, basename='drug')
router.register('patient', views.PatientViewSet, basename='patient')

urlpatterns = router.urls
