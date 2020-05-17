from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import  static

# app_name = 'avto'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('avtoapp.urls', namespace='avto_avito')),
    path('users/', include('usersapp.urls', namespace='users'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns