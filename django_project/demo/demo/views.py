
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'demo/demo.html')
def user(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    return HttpResponse(email)