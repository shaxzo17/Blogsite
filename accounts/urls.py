from django.urls import path
from .views import *

urlpatterns = [
    path('signup/' , signup_view , name='signup'),
    path('login/' , login_view , name='login'),
    path('logout/' , logout_view , name='logout'),
    path('profile/update/', profile_update_view, name='profile-update'),
    path('profile/change-password/', change_pass_view, name='change-pass'),
    path('reset1/' , reset_pass , name='reset1'),
    path('reset2/' , reset2 , name='reset2')
]