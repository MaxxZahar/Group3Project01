from rest_framework import serializers
from ..models import ColorModel


def rgba(hex_str):
    r = int(hex_str[1:3], 16)
    g = int(hex_str[3:5], 16)
    b = int(hex_str[5:], 16)
    return f'rgba({r}, {g}, {b}, 0.05)'


class ColorSerializer(serializers.ModelSerializer):
    rgba = serializers.SerializerMethodField()

    class Meta:
        model = ColorModel
        fields = '__all__'

    def get_rgba(self, obj):
        return rgba(obj.color)
