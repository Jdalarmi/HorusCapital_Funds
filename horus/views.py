from django.shortcuts import render, redirect
from datetime import datetime
from .models import ValueMonthTotal, ValueYearTotal
from .matplot import generate_bar
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required(login_url='user-login')
def home(request):
    user = request.user
    range_month = ValueMonthTotal.objects.filter(user=user)
    range_year = ValueYearTotal.objects.filter(user=user)

    total = 0

    for i in range_year:
        total += i.total

    categories = [obj.year for obj in range_year]
    values = [obj.total for obj in range_year]

    chart_data = generate_bar(categories, values)

    context ={
        "range_month": range_month,
        "range_year": range_year,
        "chart_data": chart_data,
        "total": total
    }

    return render(request, 'horus/home.html', context)

@login_required(login_url='user-login')
def insert_value(request):
    if request.method == 'POST':
        user = request.user
        data = request.POST.get("date")
        value = float(request.POST.get('value').replace(",", "."))

        data_obj = datetime.strptime(data, '%Y-%m-%d')
        month_name = data_obj.strftime('%B')
        year_name = data_obj.strftime('%Y')

        ValueMonthTotal.objects.create(
            user=user,
            month=month_name,
            value=value
        )

        data_year, created = ValueYearTotal.objects.get_or_create(
            user=user,
            year=year_name,
            defaults={'total': value}
        )
        if not created:
            data_year.total += value
        data_year.save()
        return redirect('home')

    return render(request, 'horus/values.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario não existe! Favor registre seu usuario.')
            return redirect('user-login')
    return render(request, 'horus/user_login.html')

def logout_user(request):
    auth.logout(request)

    return redirect('user-login')

@login_required(login_url='user-login')
def delete_chartjs(request):
    user = request.user
    ValueMonthTotal.objects.filter(user=user).delete()
    return render(request, 'horus/values.html')