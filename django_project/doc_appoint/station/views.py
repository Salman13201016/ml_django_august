from django.shortcuts import render, redirect,HttpResponse

from division.models import Divisions
from district.models import Districts
from .models import Stations

from django.contrib import messages

import json
from django.http import JsonResponse
from django.db import IntegrityError


def index(request):
    division_data = Divisions.objects.all()
    district_data = Districts.objects.all()

    all_station_data = Stations.objects.select_related("dis_id").all()

    if len(all_station_data) == 0:
        status = False

    else:
        status = True

    print(len(all_station_data))
    data = {
        "status": status,
        "station_data": all_station_data,
        "division": division_data,
        "district": district_data,
    }
    return render(request, "admin/station.html", data)




def get_districts(request):
    division_id = request.GET.get('division_id')
    districts = Districts.objects.filter(div_id=division_id).values('id', 'name')
    district_list = list(districts)
    json_data = json.dumps(district_list)

    return JsonResponse(json_data, safe=False, content_type='application/json')




def insert(request):
    if request.method == 'POST':
        division_id = request.POST.get("division_id")
        district_id = request.POST.get("district_id")
        station_name = request.POST.get("station_name")

        if not division_id or division_id == 'Select Division':
            messages.error(request, 'Please select a valid division.')
            return redirect("station_index")
        elif not district_id or district_id == 'Select District':
            messages.error(request, 'Please select a valid district or Add district to your database.')
            return redirect("station_index")
        elif not station_name:
            messages.error(request, 'Station name is required.')
            return redirect("station_index")
        else:
            try:
                # Convert division_id and district_id to integers
                div_obj = Divisions.objects.get(id=int(division_id))
                dis_obj = Districts.objects.get(id=int(district_id))

                # Check for duplicate station
                if Stations.objects.filter(name=station_name, div_id=div_obj, dis_id=dis_obj).exists():
                    messages.error(request, 'Duplicate station. Please enter a unique station name.')
                    return redirect("station_index")
                else:
                    # Attempt to create a new station
                    station_obj = Stations(name=station_name, div_id=div_obj, dis_id=dis_obj)
                    station_obj.save()
                    messages.success(request, 'Station added successfully.')
                    return redirect("station_index")

            except (Divisions.DoesNotExist, Districts.DoesNotExist, ValueError):
                messages.error(request, 'Invalid division or district value.')
                return redirect("station_index")
            except IntegrityError:
                messages.error(request, 'An error occurred. Please try again.')
                return redirect("station_index")

    # If there are errors or it's not a POST request, render the same page
    return render(request, 'station.html', {'division': Divisions.objects.all(), 'district': Districts.objects.all()})