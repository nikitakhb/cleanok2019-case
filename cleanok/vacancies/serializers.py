from .models import *
from rest_framework import serializers


class VacancySerializer(serializers.ModelSerializer):
    # cities = CitySerializer(many=True, read_only=True)
    job = serializers.CharField(source='name')
    loc = serializers.SerializerMethodField('get_alternative_loc')
    req = serializers.CharField(source='requirements')
    resp = serializers.CharField(source='main_responsibilities')
    cond = serializers.CharField(source='condition')

    class Meta:
        model = Vacancy
        fields = ('id', 'job', 'loc', 'req', 'resp', 'cond', 'contact')

    def get_alternative_loc(self, obj):
        return ''.join([f'{city.name}; ' for city in obj.cities.all()])[:-2]
