from django.urls import path, include
from avtoapp import views
from django.conf import settings
from django.conf.urls.static import  static


app_name = 'avto'



urlpatterns = [
    path('', views.main_view, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('create/', views.create_post, name='create'),
    path('post/<int:id>/', views.post, name='post'),
    path('avto_list/', views.AvtoListView.as_view(), name = 'avto_list'),
    path('post_detail/<int:pk>/', views.AvtoDetailView.as_view(), name = 'post_detail'),
    path('create_avto/', views.AvtoCreateView.as_view(), name = 'create_avto'),
    path('avto_update/<int:pk>/', views.AvtoUpdateView.as_view(), name = 'avto_update'),
    path('avto_delete/<int:pk>/', views.AvtoDeleteView.as_view(), name = 'avto_delete'),
]

