from rest_framework import serializers
from ..models import ImplementationBlockModel, FunctionalityColumnModel, FunctionalityModel, BottomSlide


class BottomSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomSlide
        fields = '__all__'


class FunctionalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FunctionalityModel
        fields = '__all__'


class FunctionalityColumnSerializer(serializers.ModelSerializer):
    column_functionality = FunctionalitySerializer(read_only=True, many=True)

    class Meta:
        model = FunctionalityColumnModel
        fields = '__all__'


class ImplementationBlockSerializer(serializers.ModelSerializer):
    block_column = FunctionalityColumnSerializer(read_only=True, many=True)
    block_slider_image = BottomSlideSerializer(read_only=True, manu=True)

    class Meta:
        model = ImplementationBlockModel
        fields = '__all__'
