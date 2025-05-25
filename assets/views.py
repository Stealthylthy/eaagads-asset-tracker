from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Asset, Maintenance
from .forms import AssetForm
@login_required
def home(request):
    assets = Asset.objects.all()
    return render(request, 'assets/index.html', {'assets': assets})
@login_required
def add_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AssetForm()
    return render(request, 'assets/asset_form.html', {'form': form})
@login_required
def edit_asset(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AssetForm(instance=asset)
    return render(request, 'assets/asset_form.html', {'form': form})
@login_required
def maintenance_list(request):
    maintenance = Maintenance.objects.all()
    return render(request, 'assets/maintenance_list.html', {'maintenance': maintenance})
@login_required
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'assets/register.html', {'form': form})
