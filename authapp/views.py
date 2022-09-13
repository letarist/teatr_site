from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import auth
from authapp.models import User
from authapp.forms import LoginForm


def authentication(request):
    title = 'Вход'
    login_form = LoginForm(data=request.POST or None)
    if request.method == 'POST' and login_form.is_valid:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('mainapp:main'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:main'))
