from django.shortcuts import render
from article.models import Article

def article(request):
    articleData = Article.objects.all()
    context = {
        "article" : articleData

    }
    return render(request, "article.html", context)
# Create your views here.
