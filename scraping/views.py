from django.shortcuts import render, redirect
from .models import FundsHorus
from .spider_fii import colect_fund

def start(request):
    if request.method == 'POST':
        fund_name = request.POST.get('fundo')

        if fund_name:
            fund_value = colect_fund(fund_name)
            context = {
                'fund_value':fund_value,
                'fund_name':fund_name
            }
            return render(request, 'scraping/start.html', context)
        else:
            return redirect(request, 'start-fiis')

    return render(request, 'scraping/start.html')