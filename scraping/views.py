from django.shortcuts import render

def start(request):
    return render(request, 'scraping/start.html')