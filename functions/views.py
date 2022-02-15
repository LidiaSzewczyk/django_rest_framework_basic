from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from functions.models import Flower, Herb
from functions.serializers import FlowerSerializer


def staticView(request):
    flower = {
        'id': 1,
        'name': 'bratek',
        'number': 10.4,
    }
    return JsonResponse(flower)


def plantView(request):
    flowers = Flower.objects.all()
    herbs = Herb.objects.all()
    response = {
        'flowers': list(flowers.values('name', 'number')),
        'herbs': list(herbs.values('name', 'number')),
    }
    return JsonResponse(response)


@api_view(['GET'])
def flowers_view(request):
    flowers = Flower.objects.all()
    serializer = FlowerSerializer(flowers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_flower_view(request):
    flowers = FlowerSerializer(data=request.data)
    if flowers.is_valid():
        flowers.save()
        return Response(flowers.data, status=status.HTTP_201_CREATED)
    return Response(flowers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def flowers_list(request):
    if request.method == 'GET':
        flowers = Flower.objects.all()
        serializer = FlowerSerializer(flowers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FlowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def flower_detail(request, pk):
    flowers = get_object_or_404(Flower, pk=pk)
    if request.method == 'GET':
        serializer = FlowerSerializer(flowers)
        return Response(serializer.data)

    elif request.method == 'PUT' or request.method == 'PATCH':
        partial = request.method == 'PATCH'
        serializer = FlowerSerializer(flowers, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        flowers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)