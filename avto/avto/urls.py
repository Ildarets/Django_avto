from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import  static
from rest_framework import routers
from avtoapp.api_views import AvtoViewSet, MarksViewSet, MestoViewSet

# app_name = 'avto'
router = routers.DefaultRouter()
router.register(r'avto', AvtoViewSet)
router.register(r'marks', MarksViewSet)
router.register(r'mesto', MestoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('avtoapp.urls', namespace='avto_avito')),
    path('users/', include('usersapp.urls', namespace='users')),
    path('api_auth/', include('rest_framework.urls')),
    path('categories/', include(router.urls)),
    # path('marks/', include(router.urls)),
    # path('mesto/', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns