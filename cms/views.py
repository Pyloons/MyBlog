from django.shortcuts import render
from django.views import View
from .models import Article

class IndexView(View):
    def get(self, request):
        return render(request,'index.html')

class DetailView(View):
    def get(self, request, article_id):
        article = Article.get_article_detail(article_id)
        if article != 'Not Found':
            return render(request,'detail.html', {'article_details':article})
        else:
            return render(request,'detail.html', {'article_not_found':'this is not exist'})
