from django.shortcuts import render,redirect
from user.models import User

# Create your views here.

def login(request):
    if 'user_id' in request.session:
        return redirect('index')
    return render(request,'login.html')

def logout(request):
    request.session.flush()
    return redirect('login')

def login_done(request):
    email = request.POST.get('email')
    pw = request.POST.get('pw')

    check = User.objects.get(email=email)
    if(check.pw==pw and check.v_status=='1'):
        request.session['user_id'] = check.id
        request.session['user_name'] = check.name
        return redirect('index')
    return redirect('login')