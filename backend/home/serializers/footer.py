from rest_framework import serializers
from ..models import FooterModel, ContactsModel, ApplicationModel, LocationModel, LinksModel


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsModel
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationModel
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = '__all__'


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinksModel
        fields = '__all__'


class FooterSerializer(serializers.ModelSerializer):
    footer_contacts = ContactsSerializer(read_only=True, many=True)
    footer_application = ApplicationSerializer(read_only=True, many=True)
    footer_location = LocationSerializer(read_only=True, many=True)
    footer_links = LinksSerializer(read_only=True, many=True)

    class Meta:
        model = FooterModel
        fields = '__all__'
