from rest_framework import serializers

from viewsetclasses.models import DrugCategory, Drug, Patient


class DrugCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugCategory
        fields = ('pk', 'name')
        depth = 1
        read_only_fields = ('name',)


class DrugSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='vievsets:drug-detail',
                                               lookup_field='pk')
    drug_category = serializers.SlugRelatedField(queryset=DrugCategory.objects.all(),
                                                 slug_field='name')

    class Meta:
        model = Drug
        fields = ('url', 'name', 'drug_category', 'use_by_date', 'delivered')


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('pk', 'name', 'gender', 'age', 'admited')
