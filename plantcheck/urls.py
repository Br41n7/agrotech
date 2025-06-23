from django.urls import URLPattern, path
from .views import Det

urlpattern = [
    path('detect/', Det, name='PlantDetect'),
]
