from django.shortcuts import render
from rest_framework import generics

from genericclasses.serializers import StudentSerializer
from mixinclasses.models import Student


class GenericStudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GenericStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

