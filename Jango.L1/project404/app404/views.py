from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'index.html')
def about_page(request):
    return render(request,"about.html")
def phone_page(request):
    return render(request, "phone.html")