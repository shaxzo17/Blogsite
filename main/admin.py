from django.contrib import admin
from .models import Category , News , Comment , Contatc , Saved
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['category' , 'title' , 'user' , 'created_at']
    list_filter = ['category']
    search_fields = ['title__icontains' ]
admin.site.register(News , NewsAdmin)

admin.site.register(Category)