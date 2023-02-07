from django.shortcuts import render

def index(request):
    context = {
        'nomer_okowko': 25,
        'phone': 2,
        'slovar': [1,2,3,4,5,6]}

    return render(
        request,                # Запрос
        'homepage/index.html',
        context,                 # подстановки


    )