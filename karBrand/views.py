from django.shortcuts import render, redirect
from . import forms

def add_brand(request):
    if request.method == 'POST':
        form = forms.BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.BrandForm()

    return render(request, 'brand.html', {'form':form})
