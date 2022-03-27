from xml.etree.ElementInclude import include

from django.urls import include, path

urlpatterns = [
    path('', include('recipes.urls')),
    path('recipes/', include('recipes.urls')),
]
