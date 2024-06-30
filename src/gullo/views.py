from django.http import HttpResponse, HttpRequest
from django.shortcuts import render 
from gapp.models import Gapp


def home(request):

    print(request.path)
    context = {
        "name": "khubaib",
        "queryset": Gapp.objects.filter(path=request.path).count()
    }
    print(Gapp.objects.all())
    Gapp.objects.create(path=request.path)
    print(Gapp.objects.filter(path=request.path))
    
    return render(request, "index.html", context)

