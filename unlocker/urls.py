from django.urls import path
from .views import UnlockerViewSet

urlpatterns = [
    path('unlock/', UnlockerViewSet.as_view({'get': 'retrieve'}), name='data-retrieve'),
    path('unlock/api/', UnlockerViewSet.as_view({'get': 'api'}), name='data-api')
]
