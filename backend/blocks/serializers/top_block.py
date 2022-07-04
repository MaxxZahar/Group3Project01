from rest_framework import serializers
from ..models import TopBlockModel
from ..settings import ALLOWED_IMAGE_EXTENSIONS
from django.core.validators import FileExtensionValidator


class TopBlockSerializer(serializers.ModelSerializer):
    img = serializers.FileField(validators=[FileExtensionValidator(ALLOWED_IMAGE_EXTENSIONS)])
    logo = serializers.FileField(validators=[FileExtensionValidator(ALLOWED_IMAGE_EXTENSIONS)])

    class Meta:
        model = TopBlockModel
        fields = '__all__'
