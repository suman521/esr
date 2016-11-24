from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"home.html",{})

def detail(request, album_id):
    return HttpResponse("<h2> Details forr a_id:"+ str(album_id)+"</h2>")