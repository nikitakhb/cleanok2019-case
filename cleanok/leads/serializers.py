from rest_framework.serializers import ModelSerializer

from .models import Lead


class LeadSerializer(ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'phone', 'service', 'comment')
