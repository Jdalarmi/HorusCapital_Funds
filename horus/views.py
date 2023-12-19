from django.shortcuts import render

def home(request):
    return render(request, 'horus/home.html')
