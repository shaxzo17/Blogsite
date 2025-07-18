from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

class News(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/' , default='default/news.jpg' , blank=True , null=True)

    class Meta:
        ordering = ['created_at']
        db_table = 'news'

    def __str__(self):
        return self.title

class Comment(models.Model):
    news = models.ForeignKey(News , on_delete=models.CASCADE)
    pos_text = models.TextField(blank=True , null=True)
    neg_text = models.TextField(blank=True , null=True)
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    rate = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'comment'

    def __str__(self):
        return self.news.title

class Contatc(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True , null=True)
    info = models.CharField(max_length=120 , blank=True , null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'contact'

    def __str__(self):
        return self.name
    
class Saved(models.Model):
    news = models.ForeignKey(News , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    class Meta:
        db_table = 'saved'

        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username
