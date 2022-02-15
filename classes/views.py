from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from classes.models import Tree
from classes.serializers import TreeSerializer


class TreeList(APIView):

    def get(self, request):
        trees = Tree.objects.all()
        serializer = TreeSerializer(trees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TreeDetail(APIView):

    def get_object(self, pk):
        try:
            return Tree.objects.get(pk=pk)
        except Tree.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tree = self.get_object(pk)
        serializer = TreeSerializer(tree)
        return Response(serializer.data)

    def put(self, request, pk):
        tree = self.get_object(pk)
        serializer = TreeSerializer(tree, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tree = self.get_object(pk)
        tree.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
