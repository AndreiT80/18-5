from django.shortcuts import render
from .forms import UserRegister


def home(request):
    return render(request, 'home.html')


def sign_up_by_django(request):
    info = ""
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and age >= 18 and username not in users:
                info = f"Приветствуем, {username}!"
            else:
                info = "Ошибка: проверьте данные."

    context = {
        'form': form,
        'info': info,
    }

    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_html(request):
    info = ""
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and age >= 18 and username not in users:
                info = f"Приветствуем, {username}!"
            else:
                info = "Ошибка: проверьте данные."

    context = {
        'form': form,
        'info': info,
    }

    return render(request, 'fifth_task/registration_page.html', context)