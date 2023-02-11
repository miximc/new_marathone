from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
            password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Успешная авторизация')
                else:
                    return HttpResponse('Дизайблед аккаунт')
            else:
                return('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'homepage/index.html', {'form': form})        
#def index(request):
#    context = {
#        'nomer_okowko': 25,
#        'phone': 2,
#        'slovar': [1,2,3,4,5,6]}

#    return render(
#        request,                # Запрос
#        'homepage/index.html',
#        context,                 # подстановки


#    )