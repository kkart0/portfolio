from django.shortcuts import render
from page.models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        message=request.POST.get("message","")
        print(name,email)
        userdet=Contact(name=name,email=email,message=message)
        userdet.save()
    return render(request,"index3.html")
    