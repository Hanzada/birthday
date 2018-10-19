from django.shortcuts import render,redirect
from .models import Tost
from .form import TostForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def index2(request):
    form=TostForm()
    if request.method=='POST':
        form=TostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=TostForm()
    return render(request,'index2.html',{'form':form})

def index3(request):
    tosts=Tost.objects.all()
    return render(request,'index3.html',{'tosts':tosts})

