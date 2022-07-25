import email
from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from cards.models import Cards
from articles.models import Articles
from loginSignup.models import LoginSignup
from django.contrib.auth.models import User
from django.shortcuts import redirect
from article.models import Article

# Create your views here.


def loginSignup(request):
    loginSignupData = LoginSignup.objects.all()
    data={
        "loginSignup" : loginSignup
    }
    return render(request,"index.html",data)

def article(request):
    articleData = Article.objects.all()
    context = {
        "article" : articleData
    }
    return render(request, "article.html", context)

def index(request):
    cardsData = Cards.objects.all()
    # articlesData = Articles.object.all()
    # articleData = Article.objects.all()
    # data={
    #     'cardsData' : cardsData
    # }
    context = {
        "varible1":"Hello",
        "varible2":"World",

        "heading" : "Google",
        "date": "13Mar",
        "desc": "This is the description part  in CardGameOver",
        "linke": "https://www.google.com/",
        "cardsData" : cardsData
        # 'articlesData' : articlesData

        # "article" : articleData

    }
    return render(request, "index.html", context)
def handleSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        exampleInputEmail1 = request.POST['exampleInputEmail1']
        exampleInputPassword1 = request.POST['exampleInputPassword1']
        cexampleInputPassword1 = request.POST['cexampleInputPassword1']

        #check for errorneous inputs


        #Create the user
        myuser = User.objects.create_user(username, email, exampleInputPassword1)
        myuser.save()
        messages.success(request,"Your Learnys Account has been successfully created")
        return redirect('')

    else:
        return HttpResponse('404 - Not Found')



def about(request):
    articlesData = Articles.objects.all()
    data = {
        'articlesData' : articlesData
    }
    return render(request, "about.html" , data)
    # return HttpResponse("This is Aboutpage")
def services(request):
    return render(request, "services.html" )
    # return HttpResponse("This is Servicespage")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email,phone=phone, desc= desc, date=datetime.today())
        contact.save()
        messages.succes(request, 'Profile details updated..')
    return render(request, "contact.html")
    # return HttpResponse("This is Contactpage")