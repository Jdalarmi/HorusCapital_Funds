from django.shortcuts import render
from .models import FundsHorus
from .spider_fii import colect_fund

def start(request):
    print(colect_fund('VRTA11'))
    if request.method == 'POST':
        fundo = request.POST.get('fundo')
        # dados_fund = FundsHorus.objects.get_or_create(
        #     fund = fundo
        # )
    return render(request, 'scraping/start.html')