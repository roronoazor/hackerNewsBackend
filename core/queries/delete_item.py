from core.models import Item

"""
    function to delete items
"""


def delete_items_query(request):
    
    id_to_remove = request.data.get("id")
    if id_to_remove:
        Item.objects.filter(id=id).delete()
    return True