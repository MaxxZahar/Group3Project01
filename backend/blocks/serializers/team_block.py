from rest_framework import serializers
from ..models import TeamBlockModel, TeamItemModel


class TeamItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamItemModel
        fields = '__all__'


class TeamBlockSerializer(serializers.ModelSerializer):
    block_team_member = TeamItemSerializer(read_only=True, many=True)

    class Meta:
        model = TeamBlockModel
        fields = '__all__'
