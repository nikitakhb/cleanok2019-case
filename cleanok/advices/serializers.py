from .models import Advice
from rest_framework import serializers

class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = ['title', 'text', 'link']