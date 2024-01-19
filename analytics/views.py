from django.shortcuts import render, redirect
from .models import JurosTable, TableFutureFees, InsertValuesAporte
from horus.models import ValueMonthTotal
from django.contrib.auth.decorators import login_required

@login_required(login_url='user-login')
def future_values(request):
    user = request.user
    if request.method == 'POST':
        value_start = float(request.POST.get('value_start').replace(",", "."))
        value_by = float(request.POST.get('value_by').replace(",", "."))
        value_rentability = float(request.POST.get('value_rentability').replace(",", "."))
        value_format = "{:.2f}".format(value_rentability)

        existing_entry = JurosTable.objects.filter(
            user=user,
            value_start=value_start,
            value_month=value_by,
            value_rentability=value_format
        ).first()

        if existing_entry:
            existing_entry.value_start = value_start
            existing_entry.value_month = value_by
            existing_entry.value_rentability = value_format
            existing_entry.save()

        else:   
            JurosTable.objects.create(
                user=user,
                value_start=value_start,
                value_month=value_by,
                value_rentability=value_format
            )
        return redirect('analise')

    return render(request, 'analytics/analise_copy.html')

@login_required(login_url='user-login')
def analise(request):
    user = request.user
    data = JurosTable.objects.filter(user=user)
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
            juros_test = total_acumulado * (rentabilidade / 100)

            TableFutureFees.objects.get_or_create(
                user = user,
                total_investido = total_investido,
                juros = juros_test,
                total_acumulado= total_acumulado
            )
    data_juros = TableFutureFees.objects.all()
    juros_mensal = ValueMonthTotal.objects.all()
    data_aportes = InsertValuesAporte.objects.all()

    valor_patrimonio = _value_initial
    if request.method == 'POST':
        value_aporte = float(request.POST.get('value_aporte').replace(",", "."))
        value_juros =float(request.POST.get('value_juros').replace(",", "."))

        ultimo_aporte_obj = InsertValuesAporte.objects.order_by('-patrimonio_total').first()

        if ultimo_aporte_obj:
            novo_aporte_obj = InsertValuesAporte.objects.create(
                valor_patrimonio=ultimo_aporte_obj.valor_patrimonio + value_aporte,
                juros_recebido=value_juros,
                patrimonio_total=ultimo_aporte_obj.valor_patrimonio + value_aporte + value_juros
            )
        else:
            novo_aporte_obj = InsertValuesAporte.objects.create(
                valor_patrimonio= valor_patrimonio + value_aporte,
                juros_recebido= value_juros,
                patrimonio_total= valor_patrimonio + value_aporte + value_juros
            )
                

    return render(request, 'analytics/analise.html', {"data":data, "data_juros":data_juros, "juros_mensal":juros_mensal, 'data_aportes':data_aportes})

@login_required(login_url='user-login')
def delete_table(request):
    user = request.user
    if request.method == "GET":
        JurosTable.objects.filter(user=user).delete()
        TableFutureFees.objects.filter(user=user).delete()
        InsertValuesAporte.objects.filter(user=user).delete()
    return render(request, 'analytics/analise.html')