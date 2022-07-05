from rest_framework import serializers
from ..models import FormModel, ServiceModel


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = '__all__'


class FormSerializer(serializers.ModelSerializer):
    form_service = ServiceSerializer(read_only=True, many=True)

    class Meta:
        model = FormModel
        fields = '__all__'
