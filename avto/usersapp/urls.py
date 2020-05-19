from django.urls import path
from usersapp import views
from django.conf import settings
from django.conf.urls.static import  static
from django.contrib.auth.views import LogoutView

app_name = 'avto'

urlpatterns = [
     path('login/', views.UserLoginView.as_view(), name = 'login'),
     path('logout/', LogoutView.as_view(),name = 'logout'),
     path('register/', views.UserCreateView.as_view(), name = 'register'),
     path('profile/<int:pk>/', views.UserDetailView.as_view(), name = 'profile')
]

