from rest_framework import serializers
from ..models import DescriptionBlockModel, Problem, ProblemPart


class ProblemPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemPart
        fields = '__all__'


class ProblemSerializer(serializers.ModelSerializer):
    problem_part = ProblemPartSerializer(read_only=True, many=True)

    class Meta:
        model = Problem
        fields = '__all__'


class DescriptionBlockSerializer(serializers.ModelSerializer):
    description_block_problem = ProblemSerializer(read_only=True, many=True)

    class Meta:
        model = DescriptionBlockModel
        fields = '__all__'
