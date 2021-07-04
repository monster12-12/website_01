from django.shortcuts import render ,render
from Blogapp.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email= request.POST.get("email")
        phone= request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,phone=phone,email=email,desc=desc)
        contact.save()
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')