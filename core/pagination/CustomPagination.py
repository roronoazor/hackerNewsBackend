from rest_framework.response import Response
from rest_framework import pagination

class CustomPagination(pagination.PageNumberPagination):
    
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
            
        if self.page.has_previous():
            if self.page.has_next():
                page_number = int(self.page.next_page_number()) - 1
            else:
                page_number = 1
        else:
            page_number = 1
            
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'page': page_number,
            'last_page': self.page.paginator.num_pages,
            'results': data,
        })