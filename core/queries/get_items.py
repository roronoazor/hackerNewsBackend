from core.models import Item

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
        
        
    return Item.objects.filter(**filters)