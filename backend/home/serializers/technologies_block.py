from rest_framework import serializers
from ..models import TechnologiesBlockModel, TechnologyModel


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyModel
        fields = '__all__'


class TechnologiesBlockSerializer(serializers.ModelSerializer):
    block_technology = TechnologySerializer(read_only=True, many=True)

    class Meta:
        model = TechnologiesBlockModel
        fields = '__all__'
