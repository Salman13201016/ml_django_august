from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.db import IntegrityError

from division.models import Divisions
from district.models import Districts
from hospital_category.models import Hospital_Category
from .models import Hospitals
from station.models import Stations

# Create your views here.
def hospital_index(request):
    category_data = Hospital_Category.objects.all()
    division_data = Divisions.objects.all()
    district_data = Districts.objects.select_related('div_id').all()
    station_data = Stations.objects.select_related('dis_id').all()
    hospital_data = Hospitals.objects.all()

    if(len(hospital_data)==0):
        status = False
    
    else:
        status = True

    data = {'all_data': hospital_data,'division':division_data,'district': district_data,'category':category_data,'station': station_data, 'status':status}
    return render(request,'admin/hospital.html', data)

def hospital_insert(request):
    name = request.POST.get('hospital_name')
    zip_code = request.POST.get('zip_code')
    web_link = request.POST.get('web_link')
    hospital_address = request.POST.get('hospital_address')
    hospital_description = request.POST.get('hospital_description')
    image = request.FILES.get('image')
    div_id = request.POST.get('division_id')
    dis_id = request.POST.get('district_id')
    cat_id = request.POST.get('cat_id')
    stat_id = request.POST.get('station_id')

    dis_obj = Districts.objects.get(id=dis_id)
    div_obj = Divisions.objects.get(id=div_id)
    stat_obj = Stations.objects.get(id=stat_id)

    cat_obj = Hospital_Category.objects.get(id=cat_id)

    Hospitals.objects.create(name=name, zip_code=zip_code, web_link=web_link, address=hospital_address, description=hospital_description,hos_image=image, div_id=div_obj, dis_id=dis_obj, cat_id=cat_obj, station_id=stat_obj)
    
    # hospital_obj.name = name
    # hospital_obj.zip_code = zip_code
    # hospital_obj.web_link = web_link
    # hospital_obj.hospital_address = hospital_address
    # hospital_obj.hospital_description = hospital_description
    # hospital_obj.save()

    return redirect('hospital_index')

def get_districts(request):
    division_id = request.GET.get('division_id')
    districts = Districts.objects.filter(div_id=division_id).values('id', 'name')
    # districts = Districts.objects.select_related('div_id').filter(div_id=division_id)
    print(districts)
    district_list = list(districts)
    json_data = json.dumps(district_list)

    return JsonResponse(json_data, safe=False, content_type='application/json')

def get_stations(request):
    district_id = request.GET.get('district_id')
    stations = Stations.objects.filter(dis_id=district_id).values('id', 'name')
    # districts = Districts.objects.select_related('div_id').filter(div_id=division_id)
    print(stations)
    stations_list = list(stations)
    json_data_station = json.dumps(stations_list)

    return JsonResponse(json_data_station, safe=False, content_type='application/json')