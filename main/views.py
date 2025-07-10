from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    category = Category.objects.all()
    return render(request , 'index.html' , {'category': category})