
from django.contrib import admin
from django.urls import path, include

# app_name = 'avto'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('avtoapp.urls', namespace='avto_avito'))
]
