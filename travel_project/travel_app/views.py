from django.shortcuts import render,redirect
from .models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def adddestinaton(request):
    return render(request,'addDestination.html')
def viewdestination(request):
    data=Form.objects.all()
    return render(request,'viewDestination.html',{'data':data})
def getdata(request):
    if request.method=="POST":
        dest1=request.POST['destination']
        disc1=request.POST['discription']
        p1=request.POST['price']
        im1=request.FILES['image']
        data=Form( Destination_Name=dest1,Description=disc1,Price=p1,image=im1)
        data.save()
        return redirect('add_destination')
def edit(request,id):
    data=Form.objects.filter(id=id)
    return render(request,'edit.html',{'data':data})
def update(request,id):
    if request.method=="POST":
        dest1=request.POST['destination']
        disc1=request.POST['discription']
        p1=request.POST['price']
        try:
            im1 = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(im1.name, im1)
        except MultiValueDictKeyError:
            file = Form.objects.get(id=id).image
        Form.objects.filter(id=id).update(Destination_Name=dest1,Description=disc1,Price=p1,image=file)
    return redirect('view_destination')
def delete(request,id):
    Form.objects.filter(id=id).delete()
    return redirect('view_destination')
def login(request):
    if request.method=="POST":
        name=request.POST['username']
        password=request.POST['password']
        if Register.objects.filter(name=name,password=password).exists():
            return redirect('index')
        else:
            return render(request, 'login.html',{'msg':"sorry invalid user credinatials"})
    return render(request,'login.html')

    return render(request,'login.html')
def registration(request):
    return render(request,'registration.html')
def table(request):
    data=Register.objects.all()
    return render(request,'table.html',{'data':data})
def getdata2(request):
    if request.method=="POST":
        name1=request.POST['name']
        pass1=request.POST['password']
        email1=request.POST['email']
        phone1=request.POST['phone']
        data=Register(name=name1,password=pass1,email=email1,phone=phone1)
        data.save()
        return redirect('registration')
def index(request):
    return render(request,'index.html')
def add_destination(request):
    return render(request,'add_destination.html')
def view_destination(request):
    data=Form.objects.all()
    return render(request,'view_destination.html',{'data':data})
def index1(request):
    return render(request,'index1.html')
    

