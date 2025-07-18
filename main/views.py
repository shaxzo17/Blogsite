from django.shortcuts import render , get_object_or_404 , HttpResponse
from .models import Category, News, Profile, Comment
from django.contrib.auth.decorators import login_required
import random , string
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
#
# #
@login_required(login_url='login')
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

@login_required(login_url='login')
def category(request , pk):
    category = get_object_or_404(Category, pk=pk)
    news = News.objects.filter(category=category).order_by('-created_at')
    main_news = news.first()
    sub_news = news[1:5]
    print(sub_news)
    return render(request , 'category-01.html' , {"news" : news , "main_news": main_news,
    "sub_news": sub_news})

def news_detail(request, pk):
    # post = get_object_or_404(News, id=pk)
    # comments = Comment.objects.filter(news=post).order_by('-id')[:3]
    # if request.method == "POST":
    #     if not request.user.is_authenticated:
    #         messages.error(request, "Fikr qoldirish uchun tizimga kiring.")
    #         return redirect('login')
    #     comment = request.POST.get('msg')
    #     if comment:
    #         Comment.objects.create(
    #             news=post,
    #             pos_text=comment,
    #             user=request.user
    #         )
    #         messages.success(request, 'Kommentariya muvaffaqiyatli qo‘shildi.')
    #     else:
    #         messages.warning(request, 'Kommentariya bo‘sh bo‘lishi mumkin emas.')
    #
    #     return redirect('news_detail', pk=pk)
    # comments = Comment.objects.filter(news=post)
    # return render(request, 'blog-detail-01.html', {'posts': post, 'comments': comments})

        post = get_object_or_404(News, id=pk)
        if request.method == "POST":
            if not request.user.is_authenticated:
                messages.error(request, "Comment yozish uchun login qiling !")
                return redirect('login')
            comment = request.POST.get('msg')
            if comment:
                Comment.objects.create(
                    news=post,
                    pos_text=comment,
                    user=request.user
                )
                messages.success(request, 'COmment muvaffaqiyatli qo‘shildi.')
            else:
                messages.warning(request, 'COmment bosh bolishi mumkin emas !')
            return redirect('news_detail', pk=pk)
        comments = Comment.objects.filter(news=post).order_by('-id')[:3]

        return render(request, 'blog-detail-01.html', {'posts': post, 'comments': comments})

@login_required(login_url='login')
def profile_view(request):
    return render(request, 'account/profile.html', {'user': request.user})
