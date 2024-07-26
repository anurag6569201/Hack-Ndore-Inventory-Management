from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle
from .forms import VehicleForm
from .models import Asset

def assets_manage(request):
    context={

    }
    return render(request,'assets_manage/app/assets_manage.html',context)

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'assets_manage/app/vehicle_list.html', {'vehicles': vehicles})

def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'assets_manage/app/vehicle_detail.html', {'vehicle': vehicle})

def vehicle_add(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'assets_manage/app/vehicle_form.html', {'form': form})


def asset_location_view(request):
    assets = Asset.objects.all()
    return render(request, 'assets_manage/app/assets_location.html', {'assets': assets})
