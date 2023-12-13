from django.shortcuts import render

from django.http import JsonResponse

from .models import Divisions

# Create your views here.

def index(request):

    return render(request,'admin/division.html')

def show(request):
    query = Divisions.objects.values()

    data = list(query)

    all_d = {'d':data}
    # print(div_name)


    return JsonResponse(all_d)

def insert(request):
    
    div_name = request.POST.get('div_name')
    div_obj = Divisions()
    div_obj.name = div_name
    div_obj.save()

    query = Divisions.objects.values()

    data = list(query)

    all_d = {'d':data}
    print(div_name)


    return JsonResponse(all_d)
