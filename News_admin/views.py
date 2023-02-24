from django.shortcuts import render
from .forms import Newsform
from .models import news
# Create your views here.
def add_news(request):
    if request.method == "POST":
        form=Newsform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"home.html",{"form":form})
    else:
        form=Newsform()
        return render(request,"content.html",{"form":form})

def view_news(request):
    newob=news.objects.all()
    return render(request,"view.html",{"news":newob})

def news_detils(request,id):
    context={}
    context["news"]=news.objects.get(id=id)
    print(context["news"])
    return render(request,"page.html",context)