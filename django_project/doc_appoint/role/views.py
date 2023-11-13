
from django.shortcuts import render,redirect 
from django.http import HttpResponse
from .models import Role
from django.contrib import messages

def index(request):
    all_data = Role.objects.all()
    if(len(all_data)==0):
        status = False
    else:
        status = True
    
    msg = messages.get_messages(request)
    print(type(msg))

    data ={'all_data':all_data,'status':status,'msg':msg}
    return render(request,'admin/role.html',data)

def insert(request):
    role = request.POST.get('role')
    # HttpResponse(len(role))
    if(len(role)==0):
        messages.success(request,"The field can not be empty")
    else:
        role_obj = Role()
        role_obj.name = role 
        role_obj.save()
        messages.success(request,"User Role has been created Successfully")
    
    
    return redirect('index')