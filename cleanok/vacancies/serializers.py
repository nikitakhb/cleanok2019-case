from rest_framework import serializers

from .models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    job = serializers.CharField(source='name')
    loc = serializers.SerializerMethodField('get_alternative_loc')
    req = serializers.CharField(source='requirements')
    resp = serializers.CharField(source='main_responsibilities')
    cond = serializers.CharField(source='condition')

    class Meta:
        """Vacancy API fields."""

        model = Vacancy
        fields = ('id', 'job', 'loc', 'req', 'resp', 'cond', 'contact')

    def get_alternative_loc(self, obj):
        """Return alternative locations."""
        return ''.join([f'{city.name}; ' for city in obj.cities.all()])[:-2]
