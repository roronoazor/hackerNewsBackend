from .views import GetCreateItemView
from django.urls import path


urlpatterns = [
    path('items/', GetCreateItemView.as_view(), name='items')
]
