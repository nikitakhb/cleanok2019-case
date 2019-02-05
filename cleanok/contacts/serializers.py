from .models import Contact

from rest_framework import serializers


class TypeContactSerializer(serializers.ModelSerializer):
    """TypeContact serializer."""

    def to_representation(self, obj):
        resp = {
            'title': obj.name,
            'list': [],
        }
        for contact in obj.contacts.all():
            cont = {
                'label': contact.text
            }
            if contact.link is not None:
                cont['link'] = contact.link

            resp['list'].append(cont)
        return obj.eng_name, resp

    class Meta:
        """TypeContact serializer fields."""

        model = Contact
        fields = ('text', 'type')
