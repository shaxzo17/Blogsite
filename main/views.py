from django.shortcuts import render , get_object_or_404
from .models import Category, News


def index(request):
    categories = Category.objects.all()
    first_news = []
    for category in categories:
        category_first_post = News.objects.filter(category=category).order_by('-created_at').first()
        if category_first_post is not None:
            first_news.append(category_first_post)
    if len(first_news) < 4:
        news = News.objects.all()
        first_news.extend(news[len(news) - 4: len(news) - len(first_news)])

    news = News.objects.all().order_by('-created_at')

    return render(request, 'index.html', {'categories': categories, 'first_news': first_news , 'news': news})

def category(request , pk):
    category = get_object_or_404(Category, pk=pk)
    news = News.objects.filter(category=category).order_by('-created_at')
    main_news = news.first()
    sub_news = news[1:5]
    print(sub_news)
    return render(request , 'category-01.html' , {"news" : news , "main_news": main_news,
    "sub_news": sub_news})

