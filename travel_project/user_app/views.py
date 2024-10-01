from django.shortcuts import render,redirect
from travel_app.models import*


# Create your views here.
def index1(request):
    data=Form.objects.all()
    return render(request,'index1.html',{'data':data,})
def cart(request):
    return render(request,'cart.html')