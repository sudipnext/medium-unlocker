from django.urls import path, include
from .views import UnlockerViewSet

urlpatterns = [
    path('', UnlockerViewSet.as_view({'get': 'retrieve'}), name='data-retrieve')
]
