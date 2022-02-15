from rest_framework import serializers

from classes.models import Tree


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ['id', 'name', 'number']