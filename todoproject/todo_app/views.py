from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import remainder
from .forms import form
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class tasklistview(ListView):
    model = remainder
    template_name = 'index.html'
    context_object_name = 'task1'

class taskdetailview(DetailView):
     model = remainder
     template_name = 'detail.html'
     context_object_name = 'task'

class taskupdate(UpdateView):
     model = remainder
     template_name = 'update.html'
     context_object_name = 'task'
     fields = ('name','priority','date')

     def get_success_url(self):
         return reverse_lazy('cbvdetail',kwarg={'pk':self.object.id})

class taskdelete(DeleteView):
    model = remainder
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')








# Create your views here.
def index(request):
    details=remainder.objects.all()
    if request.method=='POST':
        name=request.POST.get('Task','')
        priority=request.POST.get('Priority','')
        date=request.POST.get('date','')
        task=remainder(name=name,priority=priority,date=date)
        task.save()

    return render(request,'index.html',{'task':details})

def delete(request,taskid):
    task=remainder.objects.get(id=taskid)
    if request.method =="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task1=remainder.objects.get(id=id)
    f= form(request.POST or None, instance=task1)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task1':task1})

