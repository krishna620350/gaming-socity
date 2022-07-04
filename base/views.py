# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'base/index.html')
    
def about(request):
    return render(request, 'base/about.html')

def share(request):
    return render(request, 'base/share.html')