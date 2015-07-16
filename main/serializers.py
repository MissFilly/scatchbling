from rest_framework import serializers
from .models import Item, Size


class SizeListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        try:
            return Size.objects.get(name=data)
        except Size.DoesNotExist:
            raise serializers.ValidationError('Invalid value for size: "{}".'.format(data))


class ItemSerializer(serializers.ModelSerializer):
    sizes = SizeListingField(many=True, queryset=Size.objects.all())

    class Meta:
        model = Item
        exclude = ('id',)
