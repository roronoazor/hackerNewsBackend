from core.models import Item
from django.db.models import Q
"""
    function to get items from the data store
"""

PARAM_QUERY_BY_TYPE = 'type'
PARAM_QUERY_BY_TEXT = 'search'

def get_items_query(request):
    
    filters = dict()
    
    # evaluate queryset lazily
    all_items = Item.objects.all()
    
    if request.query_params.get(PARAM_QUERY_BY_TYPE):
        all_items = all_items.filter(type=request.query_params.get(PARAM_QUERY_BY_TYPE))
        
    if request.query_params.get(PARAM_QUERY_BY_TEXT):
        all_items = all_items.filter(
            Q(text__icontains=filters.get('text__icontains', '')) |
            Q(title__icontains=filters.get('title__icontains', ''))
        )
        
    return all_items.order_by('-id')
