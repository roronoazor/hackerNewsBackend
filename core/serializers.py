from rest_framework import serializers
from .models import Item


class GetItemSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Item
        fields = '__all__'
        
        
class CreateItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        exclude = ['id', 'deleted', 'reference_id']