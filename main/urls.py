from django.urls import path
from .views import *

urlpatterns = [
    path('' , index , name='main'),
    path('category/<int:pk>/' , category , name='category'),
]