from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from .forms import movieform


# Create your views here.
def index(request):
    obj=movie.objects.all()
    context={
        'movie_list':obj
    }
    return render(request,'index.html',context)

def details(request,movie_id):
    entertainment=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':entertainment})
    # return HttpResponse('tis is movie %s' % movie_id)

def add (request):
    if request.method=="POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        images = request.FILES['images']
        film = movie(name=name,description=description,year=year,images=images)
        film.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    film = movie.objects.get(id=id)
    form = movieform(request.POST or None,request.FILES,instance=film)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':film})

def delete(request,id):
    if request.method=="POST":
        film=movie.objects.get(id=id)
        film.delete()
        return redirect('/')
    return render(request,'delete.html')

