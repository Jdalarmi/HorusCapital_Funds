from django.shortcuts import render
from .models import JurosTable

list_month = ['Janeiro', 'Fevereiro']


def future_values(request):
    if request.method == 'POST':
        value_start = float(request.POST.get('value_start').replace(",", "."))
        value_by = float(request.POST.get('value_by').replace(",", "."))
        value_rentability = float(request.POST.get('value_rentability').replace(",", "."))
        

    return render(request, 'analytics/analise_copy.html')

def analise(request):
    return render(request, 'analytics/analise.html')