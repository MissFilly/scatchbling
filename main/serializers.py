from rest_framework import serializers
from .models import Item, Size


class SizeListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        return Size.objects.get(name=data)


class ItemSerializer(serializers.ModelSerializer):
    sizes = SizeListingField(many=True, queryset=Size.objects.all())

    class Meta:
        model = Item
        exclude = ('id',)
