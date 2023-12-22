from django.shortcuts import render, redirect
from .models import JurosTable, TableFutureFees, InsertValuesAporte
from horus.models import ValueMonthTotal

list_month = ['Janeiro', 'Fevereiro']


def future_values(request):
    if request.method == 'POST':
        value_start = float(request.POST.get('value_start').replace(",", "."))
        value_by = float(request.POST.get('value_by').replace(",", "."))
        value_rentability = float(request.POST.get('value_rentability').replace(",", "."))
        value_format ="{:.2f}".format(value_rentability)

        existing_entry = JurosTable.objects.filter(
            value_start = value_start,
            value_month = value_by,
            value_rentability = value_format
        ).first

        if existing_entry:
            existing_entry.value_start = value_start
            existing_entry.value_month = value_by
            existing_entry.value_rentability = value_format
            existing_entry.save()

        else:   
            JurosTable.objects.create(
                value_start = value_start,
                value_month = value_by,
                value_rentability = value_format
        )

    return render(request, 'analytics/analise_copy.html')

def analise(request):
    data = JurosTable.objects.all()
    lista_initial = []
    for value in data:
        _value_initial = value.value_start
        lista_initial.append(value.value_start)
        lista_initial.append(value.value_month)
        lista_initial.append(value.value_rentability)
    try:
        start = lista_initial[0]
        aporte = lista_initial[1]
        rentabilidade = lista_initial[2]
        total_juros = 0
    except IndexError:
        return redirect('analise-copy')


    if not TableFutureFees.objects.exists():
        for i in range(1, 13):
            total_investido = start + aporte * i
            juros =total_investido * (rentabilidade / 100)
            total_juros += juros
            total_acumulado = total_investido + total_juros

            TableFutureFees.objects.get_or_create(
                total_investido = total_investido,
                juros = juros,
                total_acumulado= total_acumulado
            )
    data_juros = TableFutureFees.objects.all()
    juros_mensal = ValueMonthTotal.objects.all()


    if request.method == 'POST':
        value_aporte = float(request.POST.get('value_aporte').replace(",", "."))
        value_juros =float(request.POST.get('value_juros').replace(",", "."))
        
    

    return render(request, 'analytics/analise.html', {"data":data, "data_juros":data_juros, "juros_mensal":juros_mensal})