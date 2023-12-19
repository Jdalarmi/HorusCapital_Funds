from django.shortcuts import render
from datetime import datetime
from .models import ValueMonthTotal, ValueYearTotal

def home(request):
    return render(request, 'horus/home.html')

def insert_value(request):
    if request.method == 'POST':
        data = request.POST.get("date")
        value = float(request.POST.get('value').replace(",", "."))

        data_obj = datetime.strptime(data, '%Y-%m-%d')
        month_name = data_obj.strftime('%B')
        year_name = data_obj.strftime('%Y')

        ValueMonthTotal.objects.create(
            month= month_name,
            value = value
        )

        data_year, created = ValueYearTotal.objects.get_or_create(
            year = year_name,
            defaults={'total':value}
        )
        if not created:
            data_year.total += value
        data_year.save()

    return render(request, 'horus/values.html')