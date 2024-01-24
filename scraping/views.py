from django.shortcuts import render, redirect
from .models import FundsHorus
from .spider_fii import colect_fund
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='user-login')
def start(request):
    user = request.user
    data = FundsHorus.objects.filter(user=user)
    if request.method == 'POST':
        fund_name = request.POST.get('fundo')
        if fund_name == '':
            messages.error(request,'Insira nome do fundo por favor!')
            return redirect('start-fiis')
        if fund_name:
            fund_value = colect_fund(fund_name)
            context = {
                'fund_value':fund_value,
            }
            return render(request, 'scraping/start.html', context)
        else:
            return redirect(request, 'start-fiis')
    else:
        last_name = FundsHorus.objects.all()
        for name in last_name:
            fund_name = name.fund

            fund = colect_fund(fund_name)
        number_fund = fund[-1]
        print(number_fund)
    context = {
        'data': data,
        'number_fund':number_fund
    }
    return render(request, 'scraping/start.html', context)

@login_required(login_url='user-login')
def get_fund(request):
    if request.method == 'POST':
        user = request.user
        name_fund = request.POST.get('fundo')
        value_fund = request.POST.get('value')
        FundsHorus.objects.get_or_create(
            user = user,
            fund = name_fund,
            value = value_fund
        )
        messages.success(request, 'Fundo cadastrado com Sucesso!')
        return redirect('start-fiis')
    return render(request, 'scraping/new_fund.html')