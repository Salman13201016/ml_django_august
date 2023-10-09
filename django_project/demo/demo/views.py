
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import demo_user

def index(request):
    all_data = demo_user.objects.all() #select * FROM demo_user
    data = {"user_data":all_data}
    return render(request,'demo/demo.html',data)
def user(request):
    u_name = request.POST.get('name')
    u_email = request.POST.get('email')
    u_image = request.FILES.get('image')
    user_obj = demo_user()
    user_obj.name = u_name
    user_obj.email = u_email
    user_obj.image = u_image
    user_obj.save()
    return redirect('demo_index')