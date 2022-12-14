from django.db import models
import uuid


ITEM_TYPES = [
    ('job', 'job'),
    ('story', 'story'),
    ('comment', 'comment'),
    ('poll', 'poll'),
    ('pollopt', 'pollopt'),
]
# ITEM TYPES

# Create your models here.
class Item(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deleted = models.BooleanField(default=False, null=True)
    type = models.CharField(max_length=1000, choices=ITEM_TYPES)
    by = models.CharField(max_length=1000, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True)    
    dead = models.BooleanField(default=False, null=True)    
    kids = models.JSONField(default=list)
    text = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=1000, null=True, blank=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    score = models.IntegerField(null=True)
    descendants = models.IntegerField(null=True)
    parts = models.JSONField(default=list)
    parent = models.IntegerField(null=True)
    reference_id = models.IntegerField(null=True) # this is the reference id to any item from the hackerNews site
    
    
    def __str__(self):
        return f"ITEM {self.id}"
    