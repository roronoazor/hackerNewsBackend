from core.models import Item

"""
    function to delete items
"""


def delete_items_query(id):
    
    # only allow for delete of items referenced from hacker news
    Item.objects.filter(id=id, reference_id__isnull=True).delete()
    return True