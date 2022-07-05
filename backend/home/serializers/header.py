from rest_framework import serializers
from ..models import HeaderModel
from ..settings import ALLOWED_IMAGE_EXTENSIONS
from django.core.validators import FileExtensionValidator


class HeaderSerializer(serializers.ModelSerializer):
    logo = serializers.FileField(validators=[FileExtensionValidator(ALLOWED_IMAGE_EXTENSIONS)])
    extended_logo = serializers.FileField(validators=[FileExtensionValidator(ALLOWED_IMAGE_EXTENSIONS)])

    class Meta:
        model = HeaderModel
        fields = '__all__'
