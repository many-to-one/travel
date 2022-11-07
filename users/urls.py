from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('create_user/', CreateUser.as_view(), name='create_user'),
    path('update_user/<pk>', UpdateUser.as_view(), name='update_user'),
    path('profile_view/<pk>', ProfileView.as_view(), name='profile_view'),
    path('success/', success, name='success'),
]