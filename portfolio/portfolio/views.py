from django.http import HttpResponse
from django.shortcuts import render


def aboutus(request):

    return HttpResponse("Welcome Django!")
    # return render(request,"index3.html")

def home(request):
    # return HttpResponse("Home Page.")
    return render (request,'index.html')