
from django.shortcuts import render,redirect 
from django.http import HttpResponse
from .models import Role
from django.contrib import messages
from django.core.mail import send_mail


def index(request):
    if 'user_id' in request.session:

        duplicate_entries = Role.objects.filter(id='1')
        duplicate_entries.delete()
        send_mail("write you subject","How are you?",'salmanmdsmdsultan92@gmail.com',['aminulmahi12@gmail.com'])
        all_data = Role.objects.all()
        if(len(all_data)==0):
            status = False
        else:
            status = True
        
        msg = messages.get_messages(request)
        print(type(msg))
        print(request.session.get('user_name'))

        data ={'all_data':all_data,'status':status,'msg':msg,'name':request.session.get('user_name')}
        return render(request,'admin/role.html',data)
    return redirect('login')

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