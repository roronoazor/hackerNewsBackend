from django.shortcuts import render
from rest_framework import generics, status, response
from .queries.get_items import get_items_query
from .queries.delete_item import delete_items_query
from .serializers import GetItemSerializer, CreateItemSerializer
from .models import Item

# Create your views here.
class GetCreateItemView(generics.ListCreateAPIView):
    
    def get(self, request, *args, **kwargs):
        
        items = self.paginate_queryset(get_items_query(request))
        serializer = GetItemSerializer(items, many=True)
        
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, *args, **kwargs):
                
        serializer = CreateItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteItemView(generics.DestroyAPIView):
    
    def delete(self, request, *args, **kwargs):
        
        try:
          delete_items_query(request)
          return response.Response({'message': "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            # flesh out this error handling better, dont forget
            return response.Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)