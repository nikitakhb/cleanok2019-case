from rest_framework import serializers

from .models import Service, ServiceCategory, WorkItem


class ServiceCategorySerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        resp = {
            'default': {
                'title': obj.name,
            },
        }
        for service in obj.services.all():
            resp[service.id] = {
                'title': service.name,
                'desc': service.description,
                'cont': [item.name for item in service.items.all()],
                'price': service.min_price,
                'note': service.note,
                'warn': service.warn,
            }
        return {
            obj.url_link: resp
        }

    class Meta:
        model = ServiceCategory
        fields = ('name', 'url_link')


class ServiceListSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        r_list = dict()
        for service in obj.services.all():
            r_list[f'/{service.id}'] = service.name
        return {
            'name': obj.name,
            'link': f'/uslugi/{obj.url_link}',
            'list': r_list
        }

    class Meta:
        model = Service
        fields = ('category', 'name', 'description',
                  'min_price', 'note', 'warn')


class WorkItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkItem
        fields = ('name',)


class ServiceField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class ServiceSerializer(serializers.ModelSerializer):
    items = WorkItemSerializer(many=True, read_only=True)
    category = ServiceField(many=False, read_only=True)

    class Meta:
        model = Service
        fields = ('id', 'category', 'name', 'description', 'min_price', 'items')
