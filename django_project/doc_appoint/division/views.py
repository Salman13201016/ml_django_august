from django.shortcuts import render

from django.http import JsonResponse

from .models import Divisions

# Create your views here.

def index(request):
    return render(request,'admin/division.html')

def insert(request):
    
    div_name = request.POST.get('div_name')
    div_obj = Divisions()
    div_obj.name = div_name
    div_obj.save()
    print(div_name)


    return JsonResponse({'message':"success"})
