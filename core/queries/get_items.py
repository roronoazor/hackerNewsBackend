from core.models import Item
from django.db.models import Q
"""
    function to get items from the data store
"""

PARAM_QUERY_BY_TYPE = 'type'
PARAM_QUERY_BY_TEXT = 'text'

def get_items_query(request):
    
    filters = dict()
    
    if request.query_params.get(PARAM_QUERY_BY_TYPE):
        filters['type'] = request.query_params.get(PARAM_QUERY_BY_TYPE)
        
    if request.query_params.get(PARAM_QUERY_BY_TEXT):
        filters['text__icontains'] = request.query_params.get(PARAM_QUERY_BY_TEXT)
        filters['title__icontains'] = request.query_params.get(PARAM_QUERY_BY_TEXT)
        
    return Item.objects.filter( 
                               Q(type=request.query_params.get('type')) |
                               Q(text__icontains=filters.get('text__icontains')) |
                               Q(title__icontains=filters.get('title__icontains'))
                               ).order_by("-id")
