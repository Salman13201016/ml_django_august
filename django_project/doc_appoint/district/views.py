from django.shortcuts import render,redirect

from division.models import Divisions
from .models import Districts

# Create your views here.


def index(request):
    division_data = Divisions.objects.all()
    

    all_dis_data = Districts.objects.select_related('div_id').all()

    if(len(all_dis_data)==0):
        status = False
    
    else:
        status = True
    
    
    print(len(all_dis_data))
    data ={'status':status,'district_data':all_dis_data,'division':division_data}
    return render(request,'admin/district.html',data)
def insert(request):
    div_id = request.POST.get('div_id')
    district_name = request.POST.get('dis_name')

    dis_obj = Districts()
    div_obj = Divisions.objects.get(id=div_id)

    dis_obj.name = district_name
    dis_obj.div_id = div_obj
    dis_obj.save()
    return redirect('district_index')