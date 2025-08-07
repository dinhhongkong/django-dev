from rest_framework import serializers


class FilmSerializer(serializers.Serializer):
    fields = '__all__'

