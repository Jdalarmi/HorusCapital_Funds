from django.shortcuts import render

def home(request):
    return render(request, 'horus/home.html')

def insert_value(request):
    return render(request, 'horus/values.html')