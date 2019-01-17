from .models import *
from rest_framework import serializers


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ('id', 'name')


class WorkItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkItem
        fields = ('id', 'service', 'name')


class ServiceSerializer(serializers.ModelSerializer):
    work_items = WorkItemSerializer(many=True, read_only=True)
    category = ServiceCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Service
        fields = ('id', 'category', 'name', 'description', 'min_price', 'work_items')
