from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    head_news = models.Head_news.objects.all()
    popular_posts = models.Popular_post.objects.all()
    comments = models.Comment.objects.all()
    all_news = models.News_all.objects.all()
    mini_news = models.Mini_news.objects.all()
    extend = {
        'head_news':head_news,
        'popular_posts':popular_posts,
        'comments':comments,
        'all_news':all_news,
        'mini_news':mini_news
    }
    return render(request, 'index.html', extend)