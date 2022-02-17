from rest_framework import viewsets

from viewsetclasses.models import DrugCategory, Drug, Patient
from viewsetclasses.serializers import DrugCategorySerializer, DrugSerializer, PatientSerializer


class DrugCategoryViewSet(viewsets.ModelViewSet):
    queryset = DrugCategory.objects.all()
    serializer_class = DrugCategorySerializer


class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
