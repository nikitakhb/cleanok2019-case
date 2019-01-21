from rest_framework import serializers
from .models import Recomend


class RecomendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomend
        fields = ('title', 'subt', 'url')
