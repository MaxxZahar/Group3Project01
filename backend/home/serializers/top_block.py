from rest_framework import serializers
from ..models import TopBlockModel


class TopBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopBlockModel
        fields = '__all__'
