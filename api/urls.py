from django.urls import path
from .views import register_user,user_login,user_logout,get_all_users

urlpatterns = [
    path('register/', register_user,name='register'),
    path('login/', user_login,name='register'),
    path('logout/', user_logout,name='logout'),
    path('users/', get_all_users, name='get-all-users'),
]