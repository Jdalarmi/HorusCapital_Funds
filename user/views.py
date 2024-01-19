from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if len(username) < 4:
            messages.error(request, "Por favor insira usuario com mais de 4 caracteres")
            return redirect('register-user-finance')
        for i in username:
            if i.isdigit():
                messages.error(request, "Nome de usuario não pode conter numeros!")
                return redirect('register-user-finance')
        if len(password) < 5:
            messages.error(request, "Favor insira senha maior que 8 digitos!")
            return redirect('register-user-finance')
        user = User.objects.create_user(
            username=username,
            password=password
            )
        print(user)

        user.save() 
        return redirect('user-login')
    return render(request, 'register.html')
