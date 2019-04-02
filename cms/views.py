from django.shortcuts import render
from django.views import View
from .models import Article, NavLinkModel, FriendLinkModel

class IndexView(View):
    def get(self, request):
        fls = FriendLinkModel.get_all_fl()
        navs = NavLinkModel.get_all_nav()
        posts = Article.show_posts()
        return render(request,'index.html', {
            'posts': posts,
            'navs': navs,
            'fls': fls,
        })

class DetailView(View):
    def get(self, request, article_id):
        article = Article.get_article_detail(article_id)
        if article != 'Not Found':
            return render(request,'detail.html', {'article_details':article})
        else:
            return render(request,'detail.html', {'article_not_found':'this is not exist'})

class FakeGenView(View):
    def get(self, request):
        from faker import Faker
        f = Faker()
        for _ in range(20):
            t = ' '.join(f.words())
            c = f.text()
            s = 'publish'
            a = Article.objects.create(title=t,content=c,status=s)
            a.save()

