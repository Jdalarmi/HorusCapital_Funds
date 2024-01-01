from django.shortcuts import render

def start(request):
    if request.method == 'POST':
        fundo = request.POST.get('fundo')
    return render(request, 'scraping/start.html')