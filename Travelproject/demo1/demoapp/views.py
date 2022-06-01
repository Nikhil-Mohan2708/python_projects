# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from . models import team


def demo (request):
    obj=team.objects.all()
    return render(request,'index.html',{"result":obj})
