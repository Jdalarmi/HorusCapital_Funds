from django.shortcuts import render
from .models import JurosTable, TableFutureFees

list_month = ['Janeiro', 'Fevereiro']


def future_values(request):
    if request.method == 'POST':
        value_start = float(request.POST.get('value_start').replace(",", "."))
        value_by = float(request.POST.get('value_by').replace(",", "."))
        value_rentability = float(request.POST.get('value_rentability').replace(",", "."))
        value_format ="{:.2f}".format(value_rentability)

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
        lista_initial.append(value.value_start)
        lista_initial.append(value.value_month)
        lista_initial.append(value.value_rentability)

    start = lista_initial[0]
    aporte = lista_initial[1]
    rentabilidade = lista_initial[2]
    total_juros = 0


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


    return render(request, 'analytics/analise.html', {"data":data, "data_juros":data_juros})