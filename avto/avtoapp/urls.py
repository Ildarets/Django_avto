from django.urls import path
from avtoapp import views
from django.conf import settings
from django.conf.urls.static import  static

app_name = 'avtoapp'

urlpatterns = [
    path('', views.main_view, name = 'index'),
    path('create/', views.create_post, name = 'create'),
    path('post/<int:id>/', views.post, name = 'post')
]

