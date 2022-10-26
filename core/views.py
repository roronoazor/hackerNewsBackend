from django.shortcuts import render
from rest_framework import generics, status, response
from .queries.get_items import get_items_query
from .serializers import GetItemSerializer

# Create your views here.
class GetCreateItemView(generics.ListCreateAPIView):
    
    def get(self, request, *args, **kwargs):
        
        items = self.paginate_queryset(get_items_query(request))
        serializer = GetItemSerializer(items, many=True)
        
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        pass
    
    
        return response.Response({'data': 'ok'}, status=status.HTTP_201_CREATED)
    
