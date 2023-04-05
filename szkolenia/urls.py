from django.urls import path
from .views import ostatnie_wpisy

urlpatterns = [
    path('', ostatnie_wpisy, name='ostatnie_wpisy'),
]