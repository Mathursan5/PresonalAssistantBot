from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,'AI_Chatbot/index.html')

def specific(request):
    return HttpResponse(list)

# def article(requeset,article_id):
#     return render(requeset,'AI_Chatbot/index.html',{article_id:article_id})