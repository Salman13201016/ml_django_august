
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

        created_role = Role.objects.get_or_create(name=role)
        print(created_role)
        # role_obj = Role()
        # role_obj.name = role 
        # role_obj.save()
        if(created_role==True):
            print(1)

            messages.success(request,"User Role has been created Successfully")
        else:
            print(2)

            messages.success(request,"User Role Already Existed")
    
    
    return redirect('index')