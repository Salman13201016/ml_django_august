from django.shortcuts import render, redirect
from .models import Hospital_Category
# Create your views here.
def hospital_cat_index(request):
    category_data = Hospital_Category.objects.all()

    if(len(category_data)==0):
        status = False
    
    else:
        status = True
    data = {'all_data':category_data, 'status':status}
    return render(request, 'admin/hospital_cat.html',data)

def hospital_cat_insert(request):

    category_name = request.POST.get('hos_cat_name')
    cat_obj = Hospital_Category()
    cat_obj.name = category_name
    cat_obj.save()
    return redirect('hospital_cat_index')
