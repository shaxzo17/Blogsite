from django.urls import path
from .views import *

urlpatterns = [
    path('' , index , name='main'),
    path('category/<int:pk>/' , category , name='category'),
    path('profile/', profile_view, name='profile'),
    path('detail/<int:pk>/' , news_detail , name='news_detail')
]