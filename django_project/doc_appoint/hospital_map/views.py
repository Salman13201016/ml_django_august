from django.shortcuts import render,redirect

from hospital.models import Hospitals
from .models import Hospital_Maps
#Importing the Nominatim geocoder class 
from geopy.geocoders import Nominatim
# Create your views here.


def index(request):
    hospital_data = Hospitals.objects.all()
    for i in hospital_data:
        print(i.name) 
    
    if(len(hospital_data)==0):
        status = False
    
    else:
        status = True
    
    data ={'status':status,'hospital_data':hospital_data}
    return render(request,'admin/hospital-map.html', data)



def insert(request):
    hos_id = request.POST.get('hosmap_id')
    lat = request.POST.get('lat')
    long = request.POST.get('long')

    hos_map_obj = Hospital_Maps()
    hos_obj = Hospitals.objects.get(id=hos_id)

    hos_map_obj. lat =  lat
    hos_map_obj. long =  long
    hos_map_obj.hos_id = hos_obj
    hos_map_obj.save()
    return redirect('hospital_map_index')



       
# Update the latitude and longitude fiel

# # Create a geolocator instance
# geolocator = Nominatim(user_agent="my_geocoder")

# # Declare an address or location
# all_hos_data = Hospitals.objects.select_related('hos_id').all()
# location_address = all_hos_data

# # Get the latitude and longitude coordinates
# location = geolocator.geocode(location_address)

# if location:
#     latitude = location.latitude
#     longitude = location.longitude

#     print(f"Latitude: {latitude}, Longitude: {longitude}")
# else:
#     print(f"Could not retrieve coordinates for the address: {location_address}")