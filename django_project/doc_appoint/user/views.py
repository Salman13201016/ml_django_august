
from django.shortcuts import render,redirect 
from django.http import HttpResponse

from role.models import Role
from . models import User

def index(request):
    #prefetch_related
    all_data = Role.objects.all().order_by('pk')
    all_user_data = User.objects.select_related('role_id').all()
    if(len(all_data)==0):
        status = False
    
    else:
        status = True
    
    if(len(all_user_data)==0):
        status_user = False
    
    else:
        status_user = True
    
    print(len(all_data))
    data ={'all_data':all_data,'status':status,'user_data':all_user_data,'status_u':status_user}
    return render(request,'admin/user.html',data)

def insert(request):
    role_id = request.POST.get('role_id')
    # return HttpResponse(type(role_id))
    name = request.POST.get('fname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    pw = request.POST.get('pw')
    conpw = request.POST.get('conpw')
    # HttpResponse(len(role))
    if(len(role_id)==0 or len(email) == 0 or len(phone) == 0 or len(address) == 0  or len(pw) == 0 or len(conpw) == 0):
        return HttpResponse('Empty field not accepted')
    else:
        if(len(name)<3 or len(pw)<3):
            return HttpResponse('The field length must be minimum 3')
        elif (pw!=conpw):
            return HttpResponse('The password and confirm password does not match')
        elif(len(phone)!=11):
            return HttpResponse('The phone number must be at 11 digit')
        
        else:
            user_obj = User()
            role_obj = Role.objects.get(id=role_id)
            user_obj.name = name
            user_obj.email = email
            user_obj.phone = phone
            user_obj.address = address
            user_obj.pw = pw
            user_obj.role_id = role_obj
            user_obj.save()
            return redirect('user_index')

    

    # else:
    #     role_obj = Role()
    #     role_obj.name = role 
    #     role_obj.save()
    #     return redirect('index')