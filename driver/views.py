from django.shortcuts import render

def index_driver(request):
    return render(request,'main/driver.html')