from django.shortcuts import render

def analise(request):
    return render(request, 'analytics/analise.html')

def future_values(request):
    return render(request, 'analytics/analise_copy.html')