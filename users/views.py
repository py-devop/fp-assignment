from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import DocumentForm
from .models import Document
from django.core.files.storage import FileSystemStorage

def inside(request):
    return render(request,"users/index.html")

def upload_file(request):
    if request.method== 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        uploaded_file_url = fs.url(filename)
        return render(request,'users/index.html',{'uploaded_file_url' : uploaded_file_url})

    return render(request,'users/index.html')

def dashboard(request):
    return render(request,"users/dashboard.html")
