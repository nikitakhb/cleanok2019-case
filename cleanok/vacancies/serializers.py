from .models import *
from rest_framework import serializers


class VacancyField(serializers.RelatedField):

    def to_representation(self, value):
        return {
            'id': value.id,
            'name': value.name
        }


class CitySerializer(serializers.ModelSerializer):
    vacancies = VacancyField(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'vacancies')


class VacancySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'cities', 'requirements', 'main_responsibilities',)
