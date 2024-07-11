from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/update', views.profile_update, name='profile_update')
]
