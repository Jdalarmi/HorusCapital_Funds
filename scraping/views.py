from django.shortcuts import render, redirect
from .models import FundsHorus
from .spider_fii import colect_fund
from django.contrib import messages

def start(request):
    data = FundsHorus.objects.all()
    if request.method == 'POST':
        fund_name = request.POST.get('fundo')

        if fund_name:
            fund_value = colect_fund(fund_name)
            context = {
                'fund_value':fund_value,
            }
            return render(request, 'scraping/start.html', context)
        else:
            return redirect(request, 'start-fiis')
    context = {
        'data': data
    }
    return render(request, 'scraping/start.html', context)

def get_fund(request):
    if request.method == 'POST':
        name_fund = request.POST.get('fundo')
        value_fund = request.POST.get('value')
        FundsHorus.objects.get_or_create(
            fund = name_fund,
            value = value_fund
        )
        messages.success(request, 'Fundo cadastrado com Sucesso!')
        return redirect('start-fiis')
        
    return render(request, 'scraping/new_fund.html')