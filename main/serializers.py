from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    sizes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Item
        exclude = ('id',)
