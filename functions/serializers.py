from rest_framework import serializers

from functions.models import Flower


class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        # fields = '__all__'
        fields= ['id', 'name', 'number']