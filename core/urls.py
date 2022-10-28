from .views import GetCreateItemView, DeleteItemView
from django.urls import path


urlpatterns = [
    path('items/', GetCreateItemView.as_view(), name='items'),
    path('items/<uuid:id>/delete/', DeleteItemView.as_view(), name='delete')
]
