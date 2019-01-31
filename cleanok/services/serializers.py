from .models import Service, WorkItem
from rest_framework import serializers


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


class ServiceListSerializer(serializers.ModelSerializer):
    # name: 'Уборка помещений',
    # link: '/uslugi/uborka',
    # list: {
    #     '/1': 'Комплексная убока',
    #     '/2': 'Генеральная убока',
    #     '/3': 'Поддерживающая убока',
    #     '/4': 'Уборка после пожара, затопления',
    #     '/5': 'Уборка после строительства, ремонта, банкетов и т.д.'
    # }
    def to_representation(self, obj):
        r_list = dict()
        for service in obj.services.all():
            r_list[f'/{service.id}'] = service.name
        return {
            'name': obj.name,
            'link': f'/uslugi/{obj.url_link}',
            'list': r_list
        }


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
