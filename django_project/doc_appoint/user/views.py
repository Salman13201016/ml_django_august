import re
from django.shortcuts import render,redirect 
from django.http import HttpResponse

from role.models import Role
from . models import User
from datetime import datetime
import random

from django.core.signing import Signer

from django.core.mail import send_mail

from django.utils.html import format_html

def email_verify(request,id):

    v_code = id
    user = User.objects.get(v_code=v_code)
    user.v_status = 1 #Update User set v_status=1 Where v_code=v_code
    user.save()
    user_data = {"u_data":user}
    return render(request,'admin/congrats.html',user_data)

def email_generate(name):
    current_time = datetime.now().strftime("%H:%M:%S")
    h, m, s =  map(int, current_time.split(':'))
    t_s = h*3600 + m*60 + s
    t_s = str(t_s)
    random_number = random.choices('123456790',k=4)
    random_number = ''.join(random_number)
    v_c = t_s + random_number
    signer = Signer()
    encrypted_value = signer.sign(v_c)
    encrypted_value1 = signer.sign(v_c).split(":")[1]
    decrypted_value = signer.unsign(encrypted_value)


    link = f"<p>Congratulations Mr {name} ! For registering as a user in our doctor appointment system. To confirm the registration </p><a href='http://127.0.0.1:8000/admin/user/email_verification/"+encrypted_value1+"' target='_blank'>please click this Activation link</a>"
    formatted_link = format_html(link)
    return encrypted_value1,formatted_link

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
    pattern = r"^[a-zA-Z0-9_.]+@gmail\.com$"
    
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
        elif not re.match(pattern, email):
            return HttpResponse('Email is not validated')

        
        else:
            user_obj = User()
            role_obj = Role.objects.get(id=role_id)
            vcode, link = email_generate(name) 
            User.objects.create(name=name,email=email,phone=phone,address=address,pw=pw,v_code =vcode, v_status=0, role_id=role_obj)

               
            send_mail(f"Mr. {name} Please Confirm Your Registration - Doc.com",link,'salmanmdsmdsultan92@gmail.com',[email],html_message=link)
            # user_obj.name = name
            # user_obj.email = email
            # user_obj.phone = phone
            # user_obj.address = address
            # user_obj.pw = pw
            # user_obj.role_id = role_obj
            # user_obj.save()
            return redirect('user_index')

    

    # else:
    #     role_obj = Role()
    #     role_obj.name = role 
    #     role_obj.save()
    #     return redirect('index')