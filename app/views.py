from django.shortcuts import render
from app.forms import AppSuccessForm
from app.models import AppSuccess
from app import app_ml
# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def check(request):
    return render(request,'check.html')

def form(request):
    form=AppSuccessForm()
    if request.method=='POST':
        form=AppSuccessForm(request.POST)
        if form.is_valid():
            new_form=form.save()
            data=AppSuccess.objects.get(pk=new_form.pk)
            pred=app_ml.predict(data)
            
            return render(request,'result.html',{'predicted':pred})
           
    else:     
        return render(request,'try.html',{'form':form})